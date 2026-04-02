---
name: tdp-silent-channels
description: Alert when any active TDP customer Slack channel (format: #____customername) has had no messages in the last 3+ days. Posts a summary of silent channels.
disable-model-invocation: true
allowed-tools: Bash
---

Check all active TDP customer channels for silence (no messages in 3+ days). Follow these steps exactly:

## Step 1 — Switch to the TDP workspace

```bash
slackdump workspace select thedesignprojecthq
```

## Step 2 — Get active customer channel IDs

```bash
slackdump list channels 2>&1 | grep "____internal-" | grep -v "(archived)"
```

Extract only the channel IDs (first column) for channels whose name matches `#____internal-*` and are not archived.

## Step 3 — Compute the date 3 days ago

Today's date: run `date -u +%Y-%m-%dT%H:%M:%S`

Subtract 3 days to get the `--time-from` value (format: `YYYY-MM-DDTHH:MM:SS`).

## Step 4 — Dump the last 3 days of messages (no file downloads)

```bash
rm -rf /tmp/tdp-silent-dump && mkdir -p /tmp/tdp-silent-dump
slackdump dump -files=false -time-from <3-days-ago> -o /tmp/tdp-silent-dump/channels.zip <all channel IDs>
```

Replace `<3-days-ago>` with the timestamp computed in Step 3, and `<all channel IDs>` with the space-separated list from Step 2.

## Step 5 — Detect silent channels (Python script)

Run the following Python script to parse the dump, filter out bot/join/leave messages, find channels with no human messages in 3+ days, and print a sorted table:

```bash
python3 - <<'EOF'
import zipfile, json, os, sys
from datetime import datetime, timezone

DUMP_PATH = "/tmp/tdp-silent-dump/channels.zip"
CUTOFF_DAYS = 3

now = datetime.now(timezone.utc)
silent = []

with zipfile.ZipFile(DUMP_PATH) as zf:
    channel_files = [f for f in zf.namelist() if f.endswith(".json") and "/" not in f.strip("/")]
    for fname in channel_files:
        channel_name = os.path.splitext(os.path.basename(fname))[0]
        with zf.open(fname) as fh:
            messages = json.load(fh)
        # Filter to human messages only (exclude bots, joins, leaves, channel_join subtypes)
        human_msgs = [
            m for m in messages
            if m.get("type") == "message"
            and not m.get("bot_id")
            and m.get("subtype") not in ("channel_join", "channel_leave", "bot_message", None.__class__)
            and "subtype" not in m
        ]
        if not human_msgs:
            silent.append((channel_name, None, None))
            continue
        latest_ts = max(float(m["ts"]) for m in human_msgs)
        latest_dt = datetime.fromtimestamp(latest_ts, tz=timezone.utc)
        days_silent = (now - latest_dt).days
        if days_silent >= CUTOFF_DAYS:
            silent.append((channel_name, latest_dt.strftime("%Y-%m-%d"), days_silent))

silent.sort(key=lambda x: (x[2] is None, -(x[2] or 9999)))

if not silent:
    print("No silent channels found. All customer channels have recent activity.")
    sys.exit(0)

print(f"\n{'Channel':<40} {'Last Human Message':<22} {'Days Silent'}")
print("-" * 72)
for name, last_date, days in silent:
    last_str = last_date if last_date else "No messages found"
    days_str = str(days) if days is not None else "N/A"
    print(f"#{name:<39} {last_str:<22} {days_str}")
print(f"\nTotal silent channels: {len(silent)}")
EOF
```

## Step 6 — Output

Present the results table to the user. For each silent channel:

- **Highlight** channels silent for 7+ days as high priority.
- **Suggest** pinging the customer directly in the channel, or flagging the account manager for a check-in.
- If no channels are silent, confirm that all active customer channels have recent activity.
