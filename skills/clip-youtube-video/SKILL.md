---
name: clip-youtube-video
description: Splits a long YouTube video into strategic ~2-minute clips based on a transcript. Use when asked to clip a video, cut a video into parts, create clips from a YouTube episode, split a video into segments, or chop up a long video for social media.
argument-hint: [video-path] [transcript-path]
allowed-tools: Bash(ffprobe *), Bash(ffmpeg *), Bash(mkdir *), Bash(ls *), Bash(mv *), Read
---

# Clip YouTube Video

Split a long video into strategic, self-contained clips (~2 minutes each) using the transcript to find natural topic breaks. Each clip starts clean with no black frames.

## Inputs

- `$ARGUMENTS[0]` — path to the video file (.mp4)
- `$ARGUMENTS[1]` — path to the transcript file (.txt)

If arguments are not provided, ask the user for both the video path and transcript path.

## Workflow

### 1. Validate inputs

- Confirm both files exist using `ls -la`
- Get the video duration using `ffprobe`:

```bash
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "<video-path>"
```

- Read the transcript file using the Read tool
- If the transcript is empty (0 bytes), tell the user and ask them to re-export it

### 2. Analyze the transcript and plan cuts

Read the full transcript carefully. Then:

- **Identify distinct topics/sections** — look for natural shifts in subject matter, new phases, transitions ("so now," "next," "let's move on"), recaps, or new demonstrations
- **Calculate target clip count** — divide total duration by 120 seconds (2 minutes), round to nearest whole number
- **Map topics to time ranges** — distribute the total duration across the identified topics proportionally based on transcript content density (longer sections of transcript = more time)
- **Place cuts at topic boundaries** — each clip should be a self-contained piece that makes sense on its own

Guidelines for good cuts:
- Each clip should have a clear, standalone topic or takeaway
- The first clip should include the hook/intro
- The last clip should include the recap/CTA
- **NEVER cut mid-sentence** — every clip must end on a completed sentence. Cross-reference the transcript to ensure the last word of each clip's time range lands at a sentence boundary, not in the middle of a thought. If a sentence extends past the target cut point, extend the clip to include the full sentence (or start the next clip earlier). This applies to ALL clips, not just the first one.
- Clips can vary between 1:45 and 2:15 — don't force exact 2:00 if it breaks a topic

### 3. Present the plan to the user

Before cutting, show the user a table:

| Clip | Time Range | Duration | Topic |
|------|------------|----------|-------|

Ask if they want to adjust any cuts before proceeding.

### 4. Create the output directory

Ask the user where to save the clips. Create the output directory:

```bash
mkdir -p "<output-path>"
```

### 5. Cut the clips with re-encoding

**CRITICAL: Always re-encode. Never use `-c copy`.**

Using `-c copy` causes black frames at the start of clips because it can only cut at keyframes. Always re-encode for frame-accurate cuts.

Use this ffmpeg pattern for each clip:

```bash
ffmpeg -y -ss <START> -i "<video-path>" -t <DURATION> -c:v libx264 -preset fast -crf 18 -c:a aac -b:a 192k "<output-path>/clip<N>_<slug>.mp4"
```

Key flags:
- `-ss` BEFORE `-i` — enables fast seeking to the start point
- `-t` — specifies duration (not end time), avoids confusion with `-to`
- `-c:v libx264 -preset fast -crf 18` — high quality re-encode (CRF 18 = near-lossless)
- `-c:a aac -b:a 192k` — clean audio re-encode

**Run all clips in parallel** using background execution to speed up the process. Wait for all to complete before verifying.

### 6. File naming

Name clips with this pattern:
```
clip<N>_<short-descriptive-slug>.mp4
```

Examples:
- `clip1_hook_intro_and_setup.mp4`
- `clip2_planning_component_strategy.mp4`
- `clip3_building_first_feature.mp4`

Use lowercase, underscores, no spaces. The slug should describe the clip's topic in 3-5 words.

### 7. Verify the output

After all clips finish encoding, verify:

```bash
for f in <output-path>/clip*.mp4; do
  dur=$(ffprobe -v quiet -show_entries format=duration -of csv=p=0 "$f")
  size=$(ls -lh "$f" | awk '{print $5}')
  name=$(basename "$f")
  printf "%-50s %6s  %s sec\n" "$name" "$size" "$(printf '%.0f' "$dur")"
done
```

### 8. Present final summary

Show the user a clean summary table with:
- Clip number and filename
- File size
- Duration
- Topic/content description

Confirm all clips are saved and where they can find them.
