---
name: tdp-weekly-check
description: Generate a weekly activity table showing how many messages each TDP team member sent in each active customer Slack channel (#tdp-*) over the last 7 days, and pull the latest Fireflies meeting updates for each customer.
allowed-tools: Bash(slackdump *), Bash(date *), Bash(rm *), Bash(mkdir *), Bash(python3 *), mcp__Fireflies__fireflies_get_transcripts, mcp__Fireflies__fireflies_get_transcript, mcp__Fireflies__fireflies_get_summary, mcp__Fireflies__fireflies_search
---

# TDP Weekly Check

Generates a weekly customer activity report from two sources:

1. **Slack** — a markdown table of TDP team message activity across the active `#tdp-*` customer Slack channels over the last 7 days (archived and internal/non-customer channels are excluded — see Step 2).
2. **Fireflies** — the latest meeting updates (summaries and action items) for each customer over the same window.

---

## Step 1 — Switch to the TDP workspace

Run:
```bash
slackdump workspace select thedesignprojecthq
```

---

## Step 2 — List active customer channels

Run the following and capture the channel IDs (first column):

```bash
slackdump list channels 2>&1 | grep "tdp-" | grep -v "(archived)" | grep -v "^C049\|scalestack-tdp\|caba-accounting"
```

This intentionally excludes archived channels and a few non-customer `tdp-` channels (`scalestack-tdp`, `caba-accounting`, and the `C049…` internal channel). Adjust these exclusions if the set of internal channels changes.

Extract only the channel IDs (first whitespace-delimited token on each line) for use in Step 4.

Keep the customer name from each channel (the part after `tdp-`) — you'll reuse it in Step 7 to match Fireflies meetings to each customer.

---

## Step 3 — Compute the 7-day lookback date

Slack (`slackdump`) wants a full timestamp; Fireflies wants a date-only ISO string. Compute both:

```bash
date -u -d "7 days ago" +%Y-%m-%dT%H:%M:%S   # <7-days-ago-ts>  -> Step 4 (slackdump)
date -u -d "7 days ago" +%Y-%m-%d            # <7-days-ago>     -> Step 7 (Fireflies fromDate)
```

Use `<7-days-ago-ts>` in Step 4 and the date-only `<7-days-ago>` as the Fireflies `fromDate` in Step 7.

---

## Step 4 — Dump messages (no file downloads)

```bash
rm -rf /tmp/tdp-weekly-dump && mkdir -p /tmp/tdp-weekly-dump
slackdump dump -files=false -time-from <7-days-ago-ts> -o /tmp/tdp-weekly-dump/channels.zip <channel IDs...>
```

Pass all channel IDs from Step 2 as space-separated arguments.

---

## Step 5 — Parse and count messages with Python

Run the following Python script to count messages per TDP team member per channel:

```python
import zipfile, json, collections, os

ROSTER = {
    "U0AGPF4EZ4L": "agos",
    "U0AJ11W381F": "agustin",
    "UFJV2AP0Q":   "alex",
    "U04DDET9B98": "amanda",
    "U085F9X1B7Y": "arnie",
    "U038BL272D7": "delfi",
    "UFLNVR5L7":   "dianne",
    "U08JW699NKY": "juli",
    "U0APS7P9JRF": "lara",
    "U06N15KDYS3": "leomar",
    "U0A7BLWA464": "pili",
    "U0AEQDBHSF4": "pranav",
    "U09NG1Y5Q30": "tomas",
    "U08H04AECTU": "vasu",
}

SKIP_SUBTYPES = {"channel_join", "channel_leave", "bot_message"}

zip_path = "/tmp/tdp-weekly-dump/channels.zip"
results = {}  # channel_name -> Counter

with zipfile.ZipFile(zip_path) as zf:
    for name in zf.namelist():
        if not name.endswith(".json"):
            continue
        channel_name = os.path.splitext(os.path.basename(name))[0]
        with zf.open(name) as f:
            messages = json.load(f)
        counts = collections.Counter()
        for msg in messages:
            if msg.get("subtype") in SKIP_SUBTYPES:
                continue
            uid = msg.get("user", "")
            if uid in ROSTER:
                counts[ROSTER[uid]] += 1
        results[channel_name] = counts

# Sort channels alphabetically
rows = []
for channel in sorted(results.keys()):
    counts = results[channel]
    if counts:
        members = ", ".join(
            f"{name}: {n}"
            for name, n in sorted(counts.items(), key=lambda x: -x[1])
        )
    else:
        members = "—"
    rows.append((channel, members))

# Print markdown table
print("| Channel | TDP messages (last 7 days) |")
print("|---------|---------------------------|")
for channel, members in rows:
    print(f"| #{channel} | {members} |")
```

---

## Step 6 — Slack output

Print the resulting markdown table to the user. Channels with no TDP activity show `—`. Results are sorted alphabetically by channel name; members within each row are sorted descending by message count.

---

## Step 7 — Fireflies updates per customer

Aside from Slack, also pull the latest meeting updates from Fireflies for each customer. Slack shows message volume; Fireflies shows what was actually discussed on customer calls.

For the same 7-day window (use the date-only `<7-days-ago>` from Step 3 as `fromDate`):

1. Fetch recent meetings with `fireflies_get_transcripts`, passing `fromDate` = `<7-days-ago>` (ISO date, e.g. `2026-07-06`). To narrow to one customer, add `keyword` = the customer name with `scope: "title"`, or filter by the customer's email domain via `participants`.
2. For each customer from Step 2, match the returned meetings by customer name in the meeting title (or by participant email domain).
3. For each matched meeting, pull the summary with `fireflies_get_summary` (or `fireflies_get_transcript`) to get the overview and action items.

Present a short per-customer block under the Slack table:

```
### <customer> — Fireflies
- <meeting title> (<date>): <one-line summary>
  - Action items: <key action items, if any>
```

If a customer has no Fireflies meetings in the window, note `No meetings this week`.

---

## Retention — keep important events even when they're old

The Slack dump under `/tmp/tdp-weekly-dump` is scratch data and is cleared at the start of each run (Step 4). This report is regenerated fresh each week and does not delete anything from Slack or Fireflies.

The rule below applies when you decide **what to include vs. drop from the Fireflies section** (Step 7), and to any weekly archive of these reports you keep:

- The default window is 7 days. If you ever widen it, apply an age cutoff (e.g. 30 days) **only** to routine, low-signal meetings — status syncs with no decisions or action items.
- **Always include an important update, regardless of age — even if it's older than 30 days.** An update is important if it involves any of: a signed / renewed / churned contract or pricing change, an escalation or at-risk signal, a scope or milestone decision, a new commitment or deadline, or open action items that are still unresolved.
- When in doubt, keep it. Err toward preserving customer history, not pruning it.

If you keep a running archive of these weekly reports, never delete an entry that surfaced an important event, no matter how old it is.
