---
name: tdp-weekly-check
description: Generate a weekly activity table showing how many messages each TDP team member sent in each active customer Slack channel (#tdp-*) over the last 7 days, and pull the latest Fireflies meeting updates for each customer.
allowed-tools: Bash(slackdump *), Bash(date *), Bash(rm *), Bash(mkdir *), Bash(python3 *), mcp__Fireflies__fireflies_get_transcripts, mcp__Fireflies__fireflies_get_transcript, mcp__Fireflies__fireflies_get_summary, mcp__Fireflies__fireflies_search
---

# TDP Weekly Check

Generates a weekly customer activity report from two sources:

1. **Slack** — a markdown table of TDP team message activity across all active `#tdp-*` customer Slack channels over the last 7 days.
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

Extract only the channel IDs (first whitespace-delimited token on each line) for use in Step 4.

Keep the customer name from each channel (the part after `tdp-`) — you'll reuse it in Step 7 to match Fireflies meetings to each customer.

---

## Step 3 — Compute the 7-day lookback date

```bash
date -u -d "7 days ago" +%Y-%m-%dT%H:%M:%S
```

Use this value as `<7-days-ago>` in Step 4 and as the Fireflies `fromDate` in Step 7.

---

## Step 4 — Dump messages (no file downloads)

```bash
rm -rf /tmp/tdp-weekly-dump && mkdir -p /tmp/tdp-weekly-dump
slackdump dump -files=false -time-from <7-days-ago> -o /tmp/tdp-weekly-dump/channels.zip <channel IDs...>
```

Pass all channel IDs from Step 2 as space-separated arguments.

---

## Step 5 — Parse and count messages with Python

Run the following Python script to count messages per TDP team member per channel:

```python
import zipfile, json, collections, os, re

ROSTER = {
    "U0AGPF4EZ4L": "agos",
    "U0AJ11W381F": "agustin",
    "UFJV2AP0Q":   "alex",
    "U04DDET9B98": "amanda",
    "U085F9X1B7Y": "arnie",
    "U038BL272D7": "delfi",
    "UFLNVR5L7":   "dianne",
    "U03LWUCJ83H": "isa",
    "U08JW699NKY": "juli",
    "U06N15KDYS3": "leomar",
    "U039NQBUJLV": "mariano",
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

For the same 7-day window (use `<7-days-ago>` from Step 3 as `fromDate`):

1. Fetch recent meetings with `fireflies_get_transcripts` (pass `fromDate` = `<7-days-ago>`). For a specific customer you can also use `fireflies_search` with the customer name.
2. For each customer from Step 2, match meetings by customer name in the meeting title or participant domain.
3. For each matched meeting, pull the summary with `fireflies_get_summary` (or `fireflies_get_transcript`) to get the overview and action items.

Present a short per-customer block under the Slack table:

```
### <customer> — Fireflies
- <meeting title> (<date>): <one-line summary>
  - Action items: <key action items, if any>
```

If a customer has no Fireflies meetings in the window, note `No meetings this week`.

---

## Retention — do not delete important events

The Slack dump under `/tmp/tdp-weekly-dump` is scratch data and is safe to clear at the start of each run (Step 4 already does this).

**Fireflies meeting updates are different — never delete an important event, even if it is older than 30 days.** When deciding what to drop from the report or from any local cache of Fireflies updates:

- Apply the 30-day age cutoff **only** to routine, low-signal updates (e.g. status syncs with no decisions or action items).
- **Keep any update flagged as important regardless of age.** An update is important if it contains any of: a signed/renewed/churned contract or pricing change, an escalation or at-risk signal, a scope or milestone decision, a new commitment or deadline, or open action items that are still unresolved.
- When in doubt, keep it. Retention errs toward preserving customer history, not pruning it.

If you maintain a running archive of these updates across weeks, prune only routine items past 30 days and leave important events in place indefinitely.
