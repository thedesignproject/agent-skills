---
name: tdp-weekly-check
description: Generate a weekly activity table showing how many messages each TDP team member sent in each active customer Slack channel (#tdp-*) over the last 7 days.
allowed-tools: Bash(slackdump *), Bash(date *), Bash(rm *), Bash(mkdir *), Bash(python3 *)
---

# TDP Weekly Check

Generates a markdown table of TDP team message activity across all active `#tdp-*` customer Slack channels over the last 7 days.

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

---

## Step 3 — Compute the 7-day lookback date

```bash
date -u -d "7 days ago" +%Y-%m-%dT%H:%M:%S
```

Use this value as `<7-days-ago>` in Step 4.

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
    "U0A5XU1JJ6N": "florencia",
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

## Step 6 — Output

Print the resulting markdown table to the user. Channels with no TDP activity show `—`. Results are sorted alphabetically by channel name; members within each row are sorted descending by message count.
