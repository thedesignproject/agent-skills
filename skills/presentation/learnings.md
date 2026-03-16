# Learnings & Design Patterns

Hard-won insights from building presentations with this framework. Reference when making design decisions.

---

## Architecture

1. **Single file is king** — Standalone HTML with embedded CSS, JS, and base64 assets. No build tools, no server, no dependencies. Drop the file anywhere and it works.

2. **Absolute positioning for slides** — Stack all `section.slide` elements with `position: absolute; inset: 0` and toggle `.active`. Simpler and more reliable than carousel transforms or scroll-based approaches.

3. **CSS variables for everything** — Colors, fonts, easing curves, spacing — all in `:root`. Changing a presentation's entire theme takes 30 seconds of editing custom properties.

4. **Transition lockout prevents jank** — 700ms `isTransitioning` flag in JS prevents double-navigation when users click rapidly. Without this, slides stack on top of each other mid-transition.

---

## Animation & Polish

5. **Easing > duration** — `cubic-bezier(0.16, 1, 0.3, 1)` (expo-out) feels premium on every transition. The curve matters more than the milliseconds. Use `ease-out-back` sparingly for playful scale-ins.

6. **Stagger delays create hierarchy** — `.anim-d1` through `.anim-d8` make content appear to "build" rather than pop. Assign delays in visual reading order: headline first, then subtext, then supporting elements. The eye follows the stagger.

7. **Shape decorations sell polish** — Floating, blurred, `mix-blend-mode: overlay` background shapes make slides look designed even with simple content. Use `luminosity` blend mode for subtlety, `overlay` for vibrancy.

8. **Parallax is cheap polish** — 5 lines of JS tracking mouse position to `--mx`/`--my` CSS variables, applied to shapes via `calc()`. Subtle movement that makes slides feel alive.

9. **Glassmorphism adds depth** — `backdrop-filter: blur(28px)` + semi-transparent white (`rgba(255,255,255,0.07)`) + subtle border. Creates visual layers without heavy shadows. Always include `-webkit-backdrop-filter` for Safari.

---

## Navigation

10. **Click zones > buttons** — Left 30% of screen = back, right 70% = forward. Invisible but intuitive — no UI buttons cluttering slides. Works naturally with presenter remotes too.

11. **Bullet reveal is essential** — `data-bullets` attribute + progressive `.visible` toggling. Dense content slides need progressive disclosure or the audience reads ahead. The JS engine intercepts `nextSlide()` to reveal bullets before advancing.

12. **Touch/swipe needs a threshold** — >50px horizontal swipe to trigger, and only if horizontal movement exceeds vertical. Prevents accidental navigation from scrolling gestures.

---

## Typography & Layout

13. **`clamp()` for typography** — `clamp(56px, 7.5vw, 112px)` works on projectors (1920px), laptops (1440px), and tablets (768px) without media queries. Every text size should use clamp.

14. **Tight line-height on display type** — `line-height: 0.92` on headings makes multi-line titles feel editorial. Body text gets `1.6` for readability.

15. **Serif italic as accent** — Pairing a bold sans-serif heading font with an italic serif creates instant visual interest. Use `font-family: var(--font-serif); font-style: italic;` via `.italic-accent` class.

---

## Content

16. **Content first, design second** — Build the slide outline collaboratively before touching any code. The best animations can't save a confusing narrative arc.

17. **One concept per slide** — Especially for glossary/definition slides. Large term + concise definition + decorative elements. Resist cramming multiple ideas.

18. **Alternate themes for variety** — Cycling between `.slide--primary`, `.slide--secondary`, and `.slide--light` prevents monotony. Plan the theme map during the outline step.

---

## Export & Delivery

19. **Standalone by default** — Base64-embed all images (`data:image/png;base64,...`). The resulting file is large but completely portable. Offer a dev version with external assets for editing.

20. **Header/footer chrome** — Consistent top bar (tagline + logo) and bottom bar (section name + subtitle) on every slide frames the content professionally. Use `position: absolute` with `pointer-events: none`.
