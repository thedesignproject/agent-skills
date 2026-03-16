---
name: presentation
description: Creates polished single-file HTML/CSS/JS slide deck presentations with animations, keyboard/click/swipe navigation, and progressive bullet reveal. Use when the user wants to create a presentation, slide deck, pitch deck, or wants to present content as slides.
argument-hint: "[topic]"
---

# Presentation Skill

Creates standalone HTML slide deck presentations with CSS animations, keyboard/click/swipe navigation, bullet reveal, mouse parallax, and polished visual design. Single file, no dependencies, works anywhere.

---

## Step 1: Choose a Mode

Ask the user how they want to work:

- **Full generation**: User provides content/outline upfront → Claude generates the entire presentation in one shot. Best when the user already knows what they want to say.
- **Interactive step-by-step**: Claude scaffolds the framework first, then builds slides one at a time — user reviews each slide before moving to the next. Best when the user is still figuring out the story or wants tight control.

---

## Step 2: Content & Structure (THE MOST IMPORTANT STEP)

Before writing any code, deeply understand what the presentation is actually saying.

Ask the user to provide source material — any of:
- A document, outline, or notes about the topic
- A rough slide-by-slide outline
- Key talking points, stats, or quotes
- An existing presentation to redesign
- A brain dump of everything they want to cover

Then collaboratively build the slide outline:
- For each slide: choose a type, headline, body content, and special elements
- Suggest a narrative arc: **hook → context → key content → details → closing**
- Flag where bullet-reveal slides help (dense content needing progressive disclosure)
- Identify which slides need images/assets vs. pure text
- Confirm final slide count and order before proceeding

**This step makes or breaks the presentation.** Spend the most time here.

### Available slide types

| Type | Class | Use Case |
|---|---|---|
| Title | `.slide-title` | Opening — large heading, subtitle, decorative shapes |
| Speaker/Bio | `.slide-speaker` | Introduce presenter — avatar, name, role, glass card |
| Question | `.slide-familiar` | Audience engagement — large centered question |
| Bullet Reveal | `.slide-learn` | Key points, agendas — progressive reveal with `data-bullets` |
| Tool/Badge Grid | `.slide-setup` | Tools, tech, logos — grid of badge cards |
| Workflow/Flow | `.slide-flow` | Processes, steps — connected boxes with arrows |
| Two-Column | `.slide-llm` | Text + image — split layout |
| Team/Grid | `.slide-speakers` | Meet the team — photo grid with names/roles |
| Glossary | `.slide-gloss` | Definitions — large term + definition |
| Closing/CTA | `.slide-closing` | Final slide — large text, call to action |

For detailed HTML templates of each type, see [slide-types.md](slide-types.md).

---

## Step 3: Design Brief

Gather style direction from the user:
- **Colors**: brand colors, or suggest a palette (5-6 hex values with roles: primary, secondary, accent, background-light, background-dark, text)
- **Fonts**: heading + body font families (Google Fonts or system fonts)
- **Vibe**: minimal / editorial / glassmorphism / bold / corporate
- **Assets**: logos, images, photos to embed

Produce a brief with:
- Color palette with CSS variable names and hex values
- Typography scale (heading-xl, heading-lg, heading-md, subtitle, body-text)
- Font families and weights
- Spacing rhythm (slide padding, element gaps)
- Animation style (subtle vs. dramatic)
- One-sentence visual direction
- Slide-to-theme mapping (which slides get which background color)

For CSS/typography/animation defaults and templates, see [framework-reference.md](framework-reference.md).

---

## Step 4: Generate the Framework

Create a single standalone HTML file with embedded `<style>` and `<script>`.

The file structure is:
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Presentation Title]</title>
  [Google Fonts link]
  <style>
    /* Reset, design tokens, slide system, themes, shapes,
       animations, typography, UI chrome, slide-specific styles,
       responsive breakpoint */
  </style>
</head>
<body>
  <div class="presentation">
    <!-- Slides go here -->
  </div>
  <!-- Progress bar, slide counter, nav hint -->
  <script>
    /* IIFE-based navigation engine */
  </script>
</body>
</html>
```

For the complete CSS architecture and JS navigation engine templates, see [framework-reference.md](framework-reference.md).

---

## Step 5: Build Slides

Using the templates from [slide-types.md](slide-types.md):

- **Full generation mode:** Create all slides at once based on the outline from Step 2
- **Interactive mode:** One slide at a time — write the HTML, let the user review, adjust, then move to the next

For every slide:
1. Use the appropriate `section.slide` with theme class (`.slide--primary`, `.slide--secondary`, `.slide--light`)
2. Set `data-theme="dark"` or `data-theme="light"` for nav UI color adaptation
3. Add `.anim` classes to all content elements for entrance animations
4. Apply stagger delays (`.anim-d1` through `.anim-d8`) in visual reading order
5. Add decorative shapes with entrance directions (`.shape-enter-left`, etc.)
6. Include `.slide-footer` with consistent content on every slide
7. For bullet-reveal slides: set `data-bullets="N"` and use `<li data-bullet="N">` elements

---

## Step 6: Polish & Review

Checklist before delivery:
- [ ] All `.anim` classes present on content elements
- [ ] Stagger delays follow visual reading order
- [ ] Decorative shapes don't overlap content (use `z-index` layering)
- [ ] Color contrast is correct on all slide themes
- [ ] Bullet reveal count matches `data-bullets` attribute
- [ ] Responsive layout works at 768px breakpoint
- [ ] Navigation works: keyboard (arrows, Space, PgUp/Dn, Home, End), click (left 30% = back, right 70% = forward), and touch/swipe (>50px threshold)
- [ ] Progress bar and slide counter update correctly
- [ ] Header/footer chrome consistent across slides
- [ ] All fonts load correctly (Google Fonts or fallbacks)

---

## Step 7: Export

**Default: standalone HTML** — single file with base64-embedded images and assets. Works anywhere, no server needed.

To embed images as base64:
```html
<img src="data:image/png;base64,[base64-data]" alt="...">
```

Optionally offer:
- **Dev version**: external image references for easier editing
- **Individual slides**: separate HTML files per slide for modular use

---

## Key Patterns

For design patterns, animation tips, and hard-won insights from building presentations with this framework, see [learnings.md](learnings.md).

### Quick reference

- **Easing**: `cubic-bezier(0.16, 1, 0.3, 1)` (expo-out) for all transitions
- **Stagger**: `.anim-d1` (0.1s) through `.anim-d8` (1.1s)
- **Shapes**: absolute positioned, `mix-blend-mode: overlay`, floating keyframe animations
- **Glass**: `backdrop-filter: blur(28px)` + semi-transparent white + subtle border
- **Typography**: `clamp()` for fluid sizing across projector/laptop/tablet
- **Parallax**: `--mx`/`--my` CSS variables tracked on mousemove
- **Transitions**: 700ms lockout via `isTransitioning` flag
