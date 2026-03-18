#!/usr/bin/env python3
"""Fetch recent videos from YouTube channels and rank by performance."""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timedelta

def fetch_channel(url, max_videos=10, date_after=None):
    """Fetch recent videos from a channel using yt-dlp."""
    cmd = [
        "yt-dlp",
        "--dump-json",
        "--no-download",
        "--skip-download",
        "--playlist-end", str(max_videos),
    ]
    if date_after:
        cmd += ["--dateafter", date_after]
    cmd.append(url)

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    videos = []
    for line in result.stdout.strip().split("\n"):
        if not line:
            continue
        try:
            data = json.loads(line)
            videos.append({
                "title": data.get("title", "Unknown"),
                "url": data.get("webpage_url", data.get("url", "")),
                "view_count": data.get("view_count", 0),
                "upload_date": data.get("upload_date", ""),
                "channel": data.get("channel", data.get("uploader", "Unknown")),
                "duration": data.get("duration", 0),
            })
        except json.JSONDecodeError:
            continue
    return videos

def main():
    channels_file = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).parent.parent / "channels.txt")
    days_back = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    date_after = (datetime.now() - timedelta(days=days_back)).strftime("%Y%m%d")
    output_file = sys.argv[3] if len(sys.argv) > 3 else str(Path(__file__).parent.parent / "latest_results.json")

    channels = [line.strip() for line in Path(channels_file).read_text().splitlines() if line.strip() and not line.startswith("#")]

    all_videos = []
    errors = []
    for ch in channels:
        print(f"Fetching: {ch}", file=sys.stderr)
        try:
            videos = fetch_channel(ch, max_videos=10, date_after=date_after)
            all_videos.extend(videos)
            print(f"  Found {len(videos)} videos", file=sys.stderr)
        except Exception as e:
            errors.append({"channel": ch, "error": str(e)})
            print(f"  Error: {e}", file=sys.stderr)

    all_videos.sort(key=lambda v: v.get("view_count") or 0, reverse=True)

    result = {
        "fetched_at": datetime.now().isoformat(),
        "days_back": days_back,
        "channels_queried": len(channels),
        "total_videos": len(all_videos),
        "errors": errors,
        "top_videos": all_videos[:50],
        "all_videos": all_videos,
    }

    Path(output_file).write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nResults saved to {output_file}", file=sys.stderr)
    print(f"Total: {len(all_videos)} videos from {len(channels)} channels", file=sys.stderr)
    print(f"Top 50 saved for analysis", file=sys.stderr)

    # Print summary to stdout for Claude
    print(json.dumps({
        "fetched_at": result["fetched_at"],
        "channels_queried": result["channels_queried"],
        "total_videos": result["total_videos"],
        "errors": result["errors"],
        "top_videos": result["top_videos"],
    }, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
