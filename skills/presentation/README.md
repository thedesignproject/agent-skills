# Presentation Skill for Claude Code

A Claude Code skill that creates polished single-file HTML/CSS/JS slide deck presentations with animations, keyboard/click/swipe navigation, and progressive bullet reveal.

## Installation

1. Copy this folder into your repo's `.claude/skills/` directory:

```bash
cp -r presentation/ your-repo/.claude/skills/presentation/
```

2. Use it:

```
/presentation Design to Code Workshop
```

or just:

```
/presentation
```

Claude will walk you through gathering requirements, building the outline, and generating slides.

## What's inside

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition — the 7-step workflow Claude follows |
| `framework-reference.md` | CSS architecture + JS navigation engine templates |
| `slide-types.md` | HTML templates for 10 slide types |
| `learnings.md` | Design patterns and hard-won insights |

## Two modes

- **Full generation**: Provide content/outline upfront, Claude generates the entire deck in one shot
- **Interactive step-by-step**: Claude scaffolds the framework, then you build slides one at a time

## Slide types

| Type | Use Case |
|------|----------|
| Title | Opening slide — large heading, decorative shapes |
| Speaker/Bio | Introduce presenter — avatar, name, role |
| Question | Audience engagement — large centered question |
| Bullet Reveal | Progressive disclosure — points appear on click |
| Tool/Badge Grid | Tools, tech, logos — grid of badge cards |
| Workflow/Flow | Processes — connected boxes with arrows |
| Two-Column | Text + image — split layout |
| Team/Grid | Meet the team — photo grid |
| Glossary | Definitions — large term + explanation |
| Closing/CTA | Final slide — large text, call to action |

## Features

- Single standalone HTML file — no build tools, no dependencies
- CSS animations with stagger delays and expo-out easing
- Keyboard navigation (arrows, Space, PgUp/Dn, Home, End)
- Click zones (left 30% = back, right 70% = forward)
- Touch/swipe support
- Progressive bullet reveal
- Mouse parallax on decorative shapes
- Glassmorphism and floating shape decorations
- Progress bar and slide counter
- Responsive at 768px breakpoint
- Base64-embedded assets for true standalone export
