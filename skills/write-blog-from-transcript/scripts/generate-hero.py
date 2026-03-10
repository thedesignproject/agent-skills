#!/usr/bin/env python3
"""
Generate a TDP-branded hero image for blog posts.
Output: 1200x630 PNG (standard OG/social sharing + Ghost feature image size)

Usage:
    python3 generate-hero.py "Blog Post Title" --output /path/to/output/
    python3 generate-hero.py "Blog Post Title" --output /path/to/output/ --color purple
"""

import argparse
import hashlib
import math
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

# === TDP BRAND COLORS ===
TDP_CHARCOAL = (37, 35, 35)        # #252323
TDP_PURPLE = (89, 85, 255)         # #5955FF
TDP_ORANGE = (255, 97, 58)         # #FF613A
TDP_LIME = (199, 244, 148)         # #C7F494
TDP_LIGHT_BLUE = (185, 226, 249)   # #B9E2F9
TDP_PEACH = (255, 226, 218)        # #FFE2DA
WHITE = (254, 254, 254)            # #FEFEFE

# Background/accent color pairs — rotated based on title hash
COLOR_THEMES = [
    {"bg": TDP_CHARCOAL, "title": WHITE, "accent": TDP_PURPLE, "decor": TDP_LIGHT_BLUE, "credit": (*WHITE[:3], 150)},
    {"bg": TDP_PURPLE, "title": WHITE, "accent": TDP_PEACH, "decor": TDP_LIGHT_BLUE, "credit": (*WHITE[:3], 150)},
    {"bg": TDP_ORANGE, "title": WHITE, "accent": TDP_CHARCOAL, "decor": TDP_PEACH, "credit": (*WHITE[:3], 180)},
    {"bg": TDP_LIME, "title": TDP_CHARCOAL, "accent": TDP_PURPLE, "decor": TDP_ORANGE, "credit": (*TDP_CHARCOAL[:3], 150)},
]

COLOR_NAME_MAP = {
    "charcoal": 0,
    "purple": 1,
    "orange": 2,
    "lime": 3,
}

# Canvas dimensions
WIDTH = 1200
HEIGHT = 630


def get_font(size, weight="bold"):
    """Get font with fallbacks — same pattern as carousel scripts."""
    font_paths = {
        "regular": [
            "/Library/Fonts/HalyardDisplay-Regular.otf",
            os.path.expanduser("~/Library/Fonts/HalyardDisplay-Regular.otf"),
            "/System/Library/Fonts/SFNS.ttf",
            "/System/Library/Fonts/HelveticaNeue.ttc",
        ],
        "semibold": [
            "/Library/Fonts/HalyardDisplay-SemiBold.otf",
            os.path.expanduser("~/Library/Fonts/HalyardDisplay-SemiBold.otf"),
            "/System/Library/Fonts/SFNS.ttf",
        ],
        "bold": [
            "/Library/Fonts/HalyardDisplay-Bold.otf",
            os.path.expanduser("~/Library/Fonts/HalyardDisplay-Bold.otf"),
            "/System/Library/Fonts/SFNS.ttf",
        ],
    }
    paths = font_paths.get(weight, font_paths["bold"])
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def draw_star(draw, cx, cy, size, color, points=4):
    """Draw a decorative star shape."""
    pts = []
    for i in range(points * 2):
        angle = math.pi * i / points - math.pi / 2
        r = size if i % 2 == 0 else size * 0.4
        pts.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    draw.polygon(pts, fill=color)


def draw_blob(draw, x, y, size, color):
    """Draw decorative blob shape."""
    circles = [
        (x, y, size * 0.4),
        (x + size * 0.3, y - size * 0.2, size * 0.35),
        (x + size * 0.5, y + size * 0.1, size * 0.3),
        (x + size * 0.1, y + size * 0.3, size * 0.25),
    ]
    for cx, cy, r in circles:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def pick_theme(title, color_override=None):
    """Pick a color theme — deterministic based on title, or manual override."""
    if color_override and color_override in COLOR_NAME_MAP:
        return COLOR_THEMES[COLOR_NAME_MAP[color_override]]
    # Hash the title to get a stable index
    idx = int(hashlib.md5(title.encode()).hexdigest(), 16) % len(COLOR_THEMES)
    return COLOR_THEMES[idx]


def fit_title(draw, title, font_weight, max_width, max_height):
    """Find the largest font size that fits the title within bounds.
    Returns (wrapped_lines, font, line_height)."""
    # Try sizes from large to small
    for size in range(72, 28, -2):
        font = get_font(size, font_weight)
        # Estimate chars per line based on average char width
        avg_char_w = font.getbbox("M")[2]
        chars_per_line = max(1, int(max_width / avg_char_w))
        lines = textwrap.wrap(title.upper(), width=chars_per_line)

        # Measure actual height
        line_height = int(size * 1.2)
        total_height = line_height * len(lines)

        if total_height <= max_height and len(lines) <= 4:
            # Verify no line exceeds max_width
            fits = True
            for line in lines:
                bbox = draw.textbbox((0, 0), line, font=font)
                if (bbox[2] - bbox[0]) > max_width:
                    fits = False
                    break
            if fits:
                return lines, font, line_height

    # Fallback: small font, more wrapping
    font = get_font(30, font_weight)
    avg_char_w = font.getbbox("M")[2]
    chars_per_line = max(1, int(max_width / avg_char_w))
    lines = textwrap.wrap(title.upper(), width=chars_per_line)
    return lines, font, int(30 * 1.2)


def generate_hero(title, output_dir, color_override=None):
    """Generate a 1200x630 hero image with the given title."""
    theme = pick_theme(title, color_override)

    canvas = Image.new("RGBA", (WIDTH, HEIGHT), theme["bg"])
    draw = ImageDraw.Draw(canvas)

    # --- Decorative elements ---
    # Top-right star
    draw_star(draw, WIDTH - 80, 60, 30, theme["decor"], points=4)
    # Bottom-left blob (subtle)
    decor_with_alpha = theme["decor"] + (80,) if len(theme["decor"]) == 3 else theme["decor"][:3] + (80,)
    draw_blob(draw, -30, HEIGHT - 120, 140, decor_with_alpha)
    # Small accent star
    draw_star(draw, 100, HEIGHT - 60, 18, theme["accent"], points=4)

    # --- Title ---
    margin_x = 80
    margin_top = 80
    max_text_width = WIDTH - margin_x * 2
    max_text_height = HEIGHT - margin_top - 140  # leave room for credit

    lines, font, line_height = fit_title(draw, title, "bold", max_text_width, max_text_height)

    # Vertically center the text block
    total_text_height = line_height * len(lines)
    y_start = margin_top + (max_text_height - total_text_height) // 2

    for i, line in enumerate(lines):
        y = y_start + i * line_height
        draw.text((margin_x, y), line, font=font, fill=theme["title"])

    # --- "by TDP" credit ---
    credit_font = get_font(18, "semibold")
    draw.text((WIDTH - 120, HEIGHT - 45), "by TDP", font=credit_font, fill=theme["credit"])

    # --- Accent bar along bottom ---
    bar_height = 6
    draw.rectangle(
        [0, HEIGHT - bar_height, WIDTH, HEIGHT],
        fill=theme["accent"],
    )

    # --- Save ---
    # Convert to RGB for PNG output
    final = Image.new("RGB", canvas.size, theme["bg"])
    final.paste(canvas, mask=canvas.split()[3])

    # Build filename from slug
    slug = title.lower()
    slug = "".join(c if c.isalnum() or c == " " else "" for c in slug)
    slug = "-".join(slug.split())[:60]
    filename = f"{slug}.png"

    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, filename)
    final.save(out_path, "PNG", dpi=(150, 150))
    print(f"Hero image saved: {out_path}")
    print(f"  Size: {WIDTH}x{HEIGHT}")
    print(f"  Theme: {color_override or 'auto'}")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="Generate a TDP-branded blog hero image")
    parser.add_argument("title", help="Blog post title")
    parser.add_argument("--output", "-o", default=".", help="Output directory (default: current dir)")
    parser.add_argument(
        "--color", "-c",
        choices=["charcoal", "purple", "orange", "lime"],
        default=None,
        help="Override background color (default: auto-rotate based on title)",
    )
    args = parser.parse_args()
    generate_hero(args.title, args.output, args.color)


if __name__ == "__main__":
    main()
