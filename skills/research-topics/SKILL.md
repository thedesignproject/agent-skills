---
name: research-topics
description: Analyzes top-performing videos from competitor YouTube channels and proposes video topic ideas for our channel. Use when asked to research video ideas, find trending topics, analyze competitor channels, or brainstorm video content.
argument-hint: [days-back]
disable-model-invocation: true
allowed-tools: Bash(python3 *), Bash(yt-dlp *), Bash(brew install *), Bash(which *), Read
---

# Research Video Topics

Fetch recent videos from competitor channels, identify top performers, and propose video topic ideas.

## Inputs

- `$0` — (optional) number of days to look back. Defaults to 7 (one week).

## Workflow

### 1. Check dependencies

Verify `yt-dlp` is installed:

```bash
which yt-dlp
```

If not found, install it:

```bash
brew install yt-dlp
```

### 2. Fetch video data

Run the fetch script to pull recent videos from all competitor channels:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/fetch_videos.py ${CLAUDE_SKILL_DIR}/channels.txt $0 ${CLAUDE_SKILL_DIR}/latest_results.json
```

This fetches up to 30 recent videos per channel, filters to the specified time window (default: last 7 days), and returns the top 50 by view count.

### 3. Analyze the results

From the top 50 videos, identify:

- **Common themes**: What topics appear repeatedly among high-performers?
- **Format patterns**: What video formats work (tutorials, comparisons, reviews, listicles, deep dives)?
- **Title patterns**: What title structures get the most views (numbers, questions, "how to", provocative statements)?
- **Duration sweet spots**: What video lengths perform best?
- **Velocity**: Which videos are gaining views fastest relative to their age?

### 4. Propose video topics

Suggest **10 video topic ideas** for our channel. For each topic:

| # | Topic | Angle | Why It Works | Inspired By |
|---|-------|-------|-------------|-------------|
| 1 | ... | ... | ... | Top video(s) that inspired this idea |

Guidelines for proposals:
- Don't copy — find a unique angle or combine trends
- Mix proven evergreen topics with timely trends
- Include a range of formats (tutorial, opinion, comparison, etc.)
- Consider what gaps exist that competitors haven't covered well
- Prioritize topics where multiple channels have proven demand

### 5. Quick wins

Highlight **3 "quick win" topics** — ideas where:
- Multiple competitor videos already prove audience demand
- Our channel can offer a differentiated perspective
- The video could be produced relatively quickly

## Channel list

The competitor channels are defined in [channels.txt](channels.txt). Edit this file to add or remove channels.
