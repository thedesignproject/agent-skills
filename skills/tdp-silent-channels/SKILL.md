---
name: tdp-silent-channels
description: Enforce two TDP comms SOPs in one pass. (1) Shared customer channels #tdp-* must have a team message on each Mon/Thu (run Tue → verify Mon, run Fri → verify Thu). (2) Internal channels #____internal-* must receive an Associate daily status update every weekday — flag any expected weekday since the last run that had no human message. After detection, drafts a concise per-customer cadence report and (with explicit EA confirmation) posts it as "TDP Police" into each #____internal-* channel — never into customer-facing channels. Also verifies the skill's assumptions remain aligned with the TDP-handbook SOPs and surfaces drift.
disable-model-invocation: true
allowed-tools: Bash, Read, Grep
---

Run on **Tuesday** (verifies Monday status update) or **Friday** (verifies Thursday check-in). Follow these steps exactly.

## Encoded SOP assumptions (reference for Step 0)

This skill's behavior depends on these facts being true in the handbook. Step 0 validates them each run; when you edit this skill, keep this list in sync.

1. **Shared customer channel name format:** `#tdp-[customer]`
2. **Internal customer channel name format:** `#____internal-[customer]`
3. **Shared-channel comms cadence:** twice per week — **Monday** and **Thursday**
4. **Internal-channel comms cadence:** daily Associate → Lead status update, **every weekday**, posted end of workday (5–6 pm Associate's TZ), as a **human message** (no bot)
5. **Who runs this skill:** the executive assistant
6. **When this skill runs:** **Tuesday** and **Friday** (the day after each expected cadence slot)

## Step 0 — Verify SOP alignment with the handbook

The handbook is expected at `/Users/aalter/coding/TDP-handbook`. If that directory does not exist, **stop and ask the user for the correct path** before continuing.

1. Check that the handbook repo is up to date with origin:

   ```bash
   git -C /Users/aalter/coding/TDP-handbook fetch origin main --quiet && \
   git -C /Users/aalter/coding/TDP-handbook rev-list --left-right --count HEAD...origin/main
   ```

   If the right-hand count is non-zero, warn the user that the local handbook is behind `origin/main` and may not reflect the latest SOPs. Continue anyway.

2. Read the following SOP files in full:
   - `content/docs/sop/process/communication-standards.mdx`
   - `content/docs/sop/process/meeting-cadence.mdx`
   - `content/docs/sop/playbooks/daily-status.mdx`
   - `content/docs/sop/playbooks/daily-status-associate.mdx`
   - `content/docs/sop/playbooks/daily-status-lead.mdx`

3. Compare each of the six assumptions above against what the SOPs actually say. For each mismatch, produce a recommendation in this format:

   > **⚠ SOP drift — assumption #N:** Skill assumes *"<assumption>"* but `<file>:<line>` says *"<quoted SOP text>"*. Recommended skill change: `<concrete edit>`.

4. If any drift is found, **print all drift recommendations before continuing**, then ask the user whether to proceed with the check using the skill's current behavior, update the skill first, or abort. If no drift, print `SOP alignment: OK` and continue to Step 1.

## Step 1 — Switch to the TDP workspace

```bash
slackdump workspace select thedesignprojecthq
```

## Step 2 — Get active customer channel IDs (shared + internal)

```bash
slackdump list channels 2>&1 | grep -E "(^|\s)(tdp-|____internal-)" | grep -v "(archived)"
```

Extract each row's channel ID **and** name. Classify each:
- **Shared** — name starts with `tdp-` (customer-facing; SOP-critical)
- **Internal** — name starts with `____internal-` (team-only; daily SOP)

Save the mapping to `/tmp/tdp-silent-dump/channel_map.json` in this shape so later steps can both classify messages and post to the right channel ID:

```json
{
  "tdp-acme":          {"kind": "shared",   "id": "C0ABC1234"},
  "____internal-acme": {"kind": "internal", "id": "C0ABC5678"}
}
```

## Step 3 — Compute the dump window

Run `date -u +%Y-%m-%dT%H:%M:%S` and `date -u +%u` (1=Mon … 7=Sun).

Dump the last **7 days** of messages so the script can report escalation (days silent).
`--time-from` = now − 7 days, format `YYYY-MM-DDTHH:MM:SS`.

## Step 4 — Dump messages (no file downloads)

```bash
rm -rf /tmp/tdp-silent-dump && mkdir -p /tmp/tdp-silent-dump
slackdump dump -files=false -time-from <7-days-ago> -o /tmp/tdp-silent-dump/channels.zip <all channel IDs>
```

## Step 5 — Detect cadence misses and build per-customer reports

This script reads the dump, identifies SOP violations, prints the EA-facing summary, and also writes `/tmp/tdp-silent-dump/reports.json` — one draft Slack message per customer for Step 7 to post.

```bash
python3 - <<'EOF'
import zipfile, json, os, sys
from datetime import datetime, timezone, timedelta

DUMP_PATH = "/tmp/tdp-silent-dump/channels.zip"
MAP_PATH = "/tmp/tdp-silent-dump/channel_map.json"
REPORTS_PATH = "/tmp/tdp-silent-dump/reports.json"

with open(MAP_PATH) as fh:
    channel_map = json.load(fh)
# Expose a flat {name: kind} view for backwards compat below
classification = {name: meta["kind"] for name, meta in channel_map.items()}

now = datetime.now(timezone.utc)
weekday = now.weekday()  # Mon=0 … Sun=6
today = now.date()

# ---- Shared-channel cadence slot (Mon/Thu via Tue/Fri runs) ----
if weekday == 1:      # Tuesday → Monday slot
    slot_date = today - timedelta(days=1)
    slot_label = "Monday status update"
elif weekday == 4:    # Friday → Thursday slot
    slot_date = today - timedelta(days=1)
    slot_label = "Thursday check-in"
else:
    slot_date = None
    slot_label = f"(run on weekday {weekday} — not Tue/Fri; skipping shared cadence check)"

# ---- Internal daily-status expected weekdays since last run ----
# Tue run → expect status on Mon.
# Fri run → expect status on Tue, Wed, Thu.
# Other days → fallback: check most recent 2 weekdays before today.
def previous_weekdays(anchor, n):
    """Return the N most recent weekdays strictly before `anchor`."""
    out, d = [], anchor
    while len(out) < n:
        d = d - timedelta(days=1)
        if d.weekday() < 5:
            out.append(d)
    return sorted(out)

if weekday == 1:
    expected_weekdays = previous_weekdays(today, 1)   # Mon
elif weekday == 4:
    expected_weekdays = previous_weekdays(today, 3)   # Tue, Wed, Thu
else:
    expected_weekdays = previous_weekdays(today, 2)

# ---- Message filters ----
def is_human_message(m):
    return (
        m.get("type") == "message"
        and not m.get("bot_id")
        and "subtype" not in m
    )

# Per-channel status (everything, not just misses)
shared_status = {}     # name -> {hit_slot, last_str, days_silent}
internal_status = {}   # name -> {missed:[dates], last_str}

with zipfile.ZipFile(DUMP_PATH) as zf:
    channel_files = [f for f in zf.namelist() if f.endswith(".json") and "/" not in f.strip("/")]
    for fname in channel_files:
        channel_name = os.path.splitext(os.path.basename(fname))[0]
        kind = classification.get(channel_name)
        if kind is None:
            if channel_name.startswith("____internal-"):
                kind = "internal"
            elif channel_name.startswith("tdp-"):
                kind = "shared"
            else:
                continue

        with zf.open(fname) as fh:
            messages = json.load(fh)
        human = [m for m in messages if is_human_message(m)]

        if human:
            latest_ts = max(float(m["ts"]) for m in human)
            latest_dt = datetime.fromtimestamp(latest_ts, tz=timezone.utc)
            last_str = latest_dt.strftime("%Y-%m-%d")
            days_silent = (today - latest_dt.date()).days
        else:
            last_str = "no messages in window"
            days_silent = 99

        if kind == "shared":
            hit_slot = (
                slot_date is not None
                and any(
                    datetime.fromtimestamp(float(m["ts"]), tz=timezone.utc).date() == slot_date
                    for m in human
                )
            )
            shared_status[channel_name] = {
                "hit_slot": hit_slot,
                "last_str": last_str,
                "days_silent": days_silent,
            }
        elif kind == "internal":
            active_dates = {
                datetime.fromtimestamp(float(m["ts"]), tz=timezone.utc).date()
                for m in human
            }
            missed = [d for d in expected_weekdays if d not in active_dates]
            internal_status[channel_name] = {
                "missed": missed,
                "last_str": last_str,
            }

# ---- EA-facing terminal summary ----
shared_misses = sorted(
    [(n, s["last_str"], s["days_silent"]) for n, s in shared_status.items() if not s["hit_slot"]],
    key=lambda x: -x[2],
)
internal_misses = sorted(
    [(n, s["missed"], s["last_str"]) for n, s in internal_status.items() if s["missed"]],
    key=lambda x: -len(x[1]),
)

print(f"\n=== SHARED-CHANNEL SOP: {slot_label} ===\n")
if slot_date is None:
    print("Skipped — run this skill on Tuesday or Friday.\n")
elif not shared_misses:
    print(f"All active shared channels had a team message on {slot_date.isoformat()}.\n")
else:
    print(f"Shared channels missing a team message on {slot_date.isoformat()}:\n")
    print(f"{'Channel':<40} {'Last Human Msg':<22} {'Days Silent'}")
    print("-" * 74)
    for name, last, days in shared_misses:
        flag = "  ⚠ 7+d" if days >= 7 else ""
        print(f"#{name:<39} {last:<22} {days}{flag}")
    print(f"\nShared channels in violation: {len(shared_misses)}")

expected_str = ", ".join(d.isoformat() for d in expected_weekdays) or "(none)"
print(f"\n=== INTERNAL-CHANNEL SOP: Daily status on {expected_str} ===\n")
if not internal_misses:
    print("Every active internal channel had activity on each expected weekday.\n")
else:
    print(f"Internal channels missing daily status on one+ weekdays:\n")
    print(f"{'Channel':<40} {'Missed Weekdays':<30} {'Last Activity'}")
    print("-" * 84)
    for name, missed, last in internal_misses:
        missed_str = ", ".join(d.strftime("%a %m-%d") for d in missed)
        flag = "  ⚠" if len(missed) >= 2 else ""
        print(f"#{name:<39} {missed_str:<30} {last}{flag}")
    print(f"\nInternal channels in violation: {len(internal_misses)}")

# ---- Per-customer draft reports (one per internal channel) ----
run_day_label = now.strftime("%a, %b %-d")
slot_day_name = slot_date.strftime("%A") if slot_date else None

def compose_message(shared_name, shared_s, missed_weekdays):
    header = f"*SOP cadence check — {run_day_label}*"
    missed_labels = ", ".join(d.strftime("%a") for d in missed_weekdays)
    internal_ok = len(missed_weekdays) == 0
    shared_applicable = shared_s is not None and slot_day_name is not None
    shared_ok = shared_applicable and shared_s["hit_slot"]
    all_ok = internal_ok and (not shared_applicable or shared_ok)

    if all_ok:
        wins = []
        if shared_ok:
            wins.append(f"{slot_day_name} customer check-in landed in `#{shared_name}`")
        if expected_weekdays:
            wins.append("daily internal status on every expected weekday")
        wins_text = " and ".join(wins) if wins else "all tracked cadence slots hit"
        return (
            f":white_check_mark: {header}\n"
            f"All good this week — {wins_text}.\n"
            f"Great consistency. Keep it up. :raised_hands:"
        )

    lines = [f":warning: {header}"]
    gaps, actions = [], []
    if shared_applicable and not shared_ok:
        gaps.append(f"no {slot_day_name} customer check-in in `#{shared_name}`")
        actions.append("post a recap + next-steps to the customer today")
    if not internal_ok:
        gaps.append(f"missed daily status on: {missed_labels}")
        actions.append("drop the missed daily status(es) with any blockers, then resume tomorrow's EOD as usual")
    lines.append("Gaps: " + "; ".join(gaps) + ".")
    if actions:
        lines.append("*Action:* " + "; ".join(actions) + ".")
    return "\n".join(lines)

reports = []
for internal_name, meta in channel_map.items():
    if meta["kind"] != "internal":
        continue
    # Extra safety: never consider a channel whose name doesn't start with ____internal-
    if not internal_name.startswith("____internal-"):
        continue
    customer = internal_name[len("____internal-"):]
    shared_name = f"tdp-{customer}"
    shared_s = shared_status.get(shared_name)  # None if no shared channel exists
    int_s = internal_status.get(internal_name, {"missed": [], "last_str": ""})
    message = compose_message(shared_name if shared_s else None, shared_s, int_s["missed"])
    reports.append({
        "customer": customer,
        "internal_channel_name": internal_name,
        "internal_channel_id": meta["id"],
        "shared_channel_name": shared_name if shared_s else None,
        "shared_hit_slot": bool(shared_s and shared_s["hit_slot"]),
        "internal_missed_weekdays": [d.isoformat() for d in int_s["missed"]],
        "message": message,
    })

reports.sort(key=lambda r: r["customer"])
with open(REPORTS_PATH, "w") as fh:
    json.dump(reports, fh, indent=2)
print(f"\nDraft reports written: {len(reports)} — see {REPORTS_PATH}")
EOF
```

## Step 6 — Output & escalation

Present both sections to the user (the EA running this skill):

- **Shared-channel violations:** designer missed the Mon or Thu cadence slot with the customer. Nudge the responsible designer; flag the AM for channels silent 7+ days (⚠).
- **Internal-channel violations:** associate skipped the Daily Status update on one or more weekdays. Per SOP, "Never skip the daily sync." Channels missing 2+ weekdays (⚠) escalate to the Lead for that account.
- If both sections are empty, confirm: every active channel met cadence.

## Step 7 — Preview per-channel reports (dry-run, always first)

Show the EA every message that will be sent **before** anything is posted. This step is always safe; it does not call Slack.

```bash
python3 - <<'EOF'
import json
with open("/tmp/tdp-silent-dump/reports.json") as fh:
    reports = json.load(fh)
if not reports:
    print("No internal channels found — nothing to post.")
    raise SystemExit
for r in reports:
    status = "GREEN" if (r["shared_hit_slot"] and not r["internal_missed_weekdays"]) else "GAP"
    print(f"\n--- [{status}] #{r['internal_channel_name']} (id={r['internal_channel_id']}) ---")
    print(r["message"])
print(f"\n{len(reports)} drafts ready. Review above.")
EOF
```

**Stop here.** Ask the EA explicitly: *"Post these to Slack?"* Do not continue to Step 8 without a clear yes.

## Step 8 — Post to Slack (live; only after explicit confirmation)

This actually sends messages. **Never run this step automatically.** Only run it after the EA reviews the drafts from Step 7 and explicitly confirms.

The posting script enforces two safety invariants:
- The target channel name must start with `____internal-`. Any other name is refused.
- The channel ID must match the one from `channel_map.json` for that internal name.

```bash
set -a; source /Users/aalter/coding/tdp-agent-skills/skills/tdp-silent-channels/.env; set +a
python3 - <<'EOF'
import json, os, urllib.request, urllib.parse, sys

TOKEN = os.environ.get("SLACK_BOT_TOKEN")
if not TOKEN or not TOKEN.startswith("xoxb-"):
    sys.exit("SLACK_BOT_TOKEN missing or not a bot token — aborting.")

with open("/tmp/tdp-silent-dump/channel_map.json") as fh:
    channel_map = json.load(fh)
with open("/tmp/tdp-silent-dump/reports.json") as fh:
    reports = json.load(fh)

sent = 0
for r in reports:
    name = r["internal_channel_name"]
    ch_id = r["internal_channel_id"]

    if not name.startswith("____internal-"):
        print(f"REFUSED (non-internal name): {name}")
        continue
    expected = channel_map.get(name, {}).get("id")
    if expected != ch_id:
        print(f"REFUSED (id mismatch for {name}: report={ch_id} map={expected})")
        continue

    data = urllib.parse.urlencode({
        "channel": ch_id,
        "text": r["message"],
        "unfurl_links": "false",
        "unfurl_media": "false",
    }).encode()
    req = urllib.request.Request(
        "https://slack.com/api/chat.postMessage",
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = json.loads(resp.read())
    except Exception as exc:
        print(f"FAIL #{name}: {exc}")
        continue
    if body.get("ok"):
        print(f"OK   #{name}")
        sent += 1
    else:
        print(f"FAIL #{name}: {body.get('error')}")

print(f"\nPosted {sent}/{len(reports)} messages.")
EOF
```

The bot must be invited to every `#____internal-*` channel (confirmed by EA at setup). If any post returns `not_in_channel`, invite **TDP Police** to that channel and re-run Step 8 — previously-posted channels will receive a duplicate unless you narrow the `reports.json` first.

## Known limitations

- **Shared-channel author attribution.** The script counts any non-bot human message as hitting the cadence slot, so a customer-only post (with no designer reply) currently reads as compliant. Resolving this requires a TDP team-member user-ID allowlist.
- **Response timeline & Morning Context checks** (Lead → Associate) are not yet verified; those would require thread/author analysis and role metadata.
