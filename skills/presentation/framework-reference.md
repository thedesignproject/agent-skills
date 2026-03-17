# Framework Reference

Detailed CSS architecture and JS navigation engine templates for the presentation framework. Load this file when building the framework (Step 4).

---

## CSS Architecture

### Reset & Base

```css
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 100%; height: 100%; overflow: hidden; }
body {
  font-family: '[heading-font]', system-ui, -apple-system, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

### Design Tokens (CSS Custom Properties)

Adapt the color names and values to the presentation's design brief. The structure should always include:

```css
:root {
  /* Colors — adapt names and values per project */
  --primary: #5B5BF0;
  --primary-dark: #4A4AD0;
  --primary-light: #7B7BFF;
  --secondary: #FF6B47;
  --secondary-light: #FF8A6A;
  --light: #FAF5F0;
  --light-dark: #F0E8E0;
  --white: #FFFFFF;
  --dark: #2D2D2D;
  --dark-muted: #555555;

  /* Fonts — adapt per project */
  --font-heading: 'Plus Jakarta Sans', system-ui, sans-serif;
  --font-serif: 'Playfair Display', Georgia, serif;
  --font-body: 'Plus Jakarta Sans', system-ui, sans-serif;

  /* Easing — these are battle-tested, rarely need changing */
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-out-back: cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);

  /* Parallax mouse tracking */
  --mx: 0;
  --my: 0;
}
```

### Slide Container System

```css
.presentation {
  width: 100vw;
  height: 100vh;
  position: relative;
  background: var(--dark);
}

.slide {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 60px 80px;
  opacity: 0;
  visibility: hidden;
  transform: scale(0.96);
  transition: opacity 0.7s var(--ease-out-expo),
              transform 0.7s var(--ease-out-expo),
              visibility 0s 0.7s;
  overflow: hidden;
}

.slide.active {
  opacity: 1;
  visibility: visible;
  transform: scale(1);
  transition: opacity 0.7s var(--ease-out-expo),
              transform 0.7s var(--ease-out-expo),
              visibility 0s 0s;
}
```

### Background Theme Variants

Create theme classes for each brand color. Use radial gradients for depth.

```css
.slide--primary {
  background: var(--primary);
  background-image:
    radial-gradient(ellipse 65% 55% at 25% 35%, rgba(130,140,255,0.5) 0%, transparent 65%),
    radial-gradient(ellipse 40% 35% at 80% 70%, rgba(70,50,190,0.45) 0%, transparent 55%);
  color: var(--white);
}
.slide--secondary {
  background: var(--secondary);
  background-image:
    radial-gradient(ellipse 45% 40% at 15% 65%, rgba(255,140,60,0.35) 0%, transparent 60%);
  color: var(--white);
}
.slide--light { background: var(--light); color: var(--dark); }
```

Each slide uses `data-theme="dark"` or `data-theme="light"` so the JS can adapt nav UI colors.

### Slide Footer

```css
.slide-footer {
  position: absolute;
  bottom: 2vh;
  left: 4vw;
  right: 4vw;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: clamp(10px, 1vw, 14px);
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  opacity: 0.5;
}

.slide--primary .slide-footer,
.slide--secondary .slide-footer { color: var(--white); }
.slide--light .slide-footer { color: var(--dark-muted); }
```

### Header Chrome

Optional top bar for branding. Applied per-slide as inline styles:

```html
<div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.18); z-index:10; pointer-events:none;">
  <span style="font-size:clamp(10px,1vw,14px); font-weight:600; letter-spacing:0.12em; text-transform:uppercase; opacity:0.5;">Left label</span>
  <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em;">Logo</span>
</div>
```

For light-themed slides, use `rgba(28,28,28,0.1)` for the border and `color:var(--dark)` on text.

---

## Decorative Shapes

### Glass Shapes (CSS-only, for dark backgrounds)

```css
.shape {
  position: absolute;
  pointer-events: none;
  z-index: 0;
  --parallax: 5;
  transition: margin 0.4s ease-out;
}
.slide.active .shape {
  margin-left: calc(var(--mx) * var(--parallax) * 1px);
  margin-top: calc(var(--my) * var(--parallax) * 1px);
}

/* Glass pill */
.shape-pill {
  width: 180px; height: 80px;
  border-radius: 40px;
  background: linear-gradient(135deg, rgba(255,255,255,0.25) 0%, rgba(255,255,255,0.08) 100%);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.2);
  box-shadow: 0 8px 32px rgba(0,0,0,0.1), inset 0 1px 0 rgba(255,255,255,0.3);
  animation: float1 8s ease-in-out infinite;
}

/* Glass sphere */
.shape-sphere {
  width: 140px; height: 140px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, rgba(255,255,255,0.35) 0%, rgba(255,255,255,0.05) 70%);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255,255,255,0.15);
  box-shadow: 0 12px 40px rgba(0,0,0,0.08), inset 0 -4px 12px rgba(255,255,255,0.1);
  animation: float3 9s ease-in-out infinite;
}

/* Glass star */
.shape-star {
  width: 120px; height: 120px;
  background: linear-gradient(135deg, rgba(255,255,255,0.3) 0%, rgba(255,255,255,0.1) 100%);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
  filter: drop-shadow(0 4px 16px rgba(0,0,0,0.1));
  animation: float2 10s ease-in-out infinite;
}
```

### Image-based Shapes

For using image assets as decorative shapes:

```css
.shape-img {
  mix-blend-mode: overlay;
  object-fit: contain;
  height: auto;
}
```

Usage: position with inline styles, vary `opacity`, `width`, `animation-delay`, and `mix-blend-mode: luminosity` for subtlety.

### Iridescent Variant (for light backgrounds)

```css
.shape--iridescent {
  background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 30%, #fdfcfb 50%, #a8edea 70%, #fed6e3 100%) !important;
  opacity: 0.7;
  border: none !important;
  box-shadow: 0 8px 32px rgba(255, 107, 71, 0.15), 0 2px 8px rgba(91, 91, 240, 0.1);
}
```

### Floating Keyframes

```css
@keyframes float1 {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  33% { transform: translateY(-18px) rotate(5deg); }
  66% { transform: translateY(8px) rotate(-3deg); }
}
@keyframes float2 {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-25px) rotate(-8deg); }
}
@keyframes float3 {
  0%, 100% { transform: translateY(0) rotate(0deg) scale(1); }
  50% { transform: translateY(-15px) rotate(12deg) scale(1.03); }
}
@keyframes spin-slow {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
@keyframes pulse-glow {
  0%, 100% { opacity: 0.7; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.05); }
}
```

### Glassmorphism Panel

For glass card backgrounds behind content:

```css
.glass-panel {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 91%; height: 88%;
  background: rgba(255, 255, 255, 0.07);
  backdrop-filter: blur(28px);
  -webkit-backdrop-filter: blur(28px);
  border-radius: 40px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  z-index: 2;
  pointer-events: none;
}
```

---

## Animation System

### Entrance Animations

```css
.slide .anim {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s var(--ease-out-expo), transform 0.6s var(--ease-out-expo);
}
.slide.active .anim {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger delays */
.slide.active .anim-d1 { transition-delay: 0.1s; }
.slide.active .anim-d2 { transition-delay: 0.2s; }
.slide.active .anim-d3 { transition-delay: 0.35s; }
.slide.active .anim-d4 { transition-delay: 0.5s; }
.slide.active .anim-d5 { transition-delay: 0.65s; }
.slide.active .anim-d6 { transition-delay: 0.8s; }
.slide.active .anim-d7 { transition-delay: 0.95s; }
.slide.active .anim-d8 { transition-delay: 1.1s; }
```

### Shape Entrances

```css
.slide .shape {
  opacity: 0;
  transition: opacity 1s var(--ease-out-expo), transform 1s var(--ease-out-expo), margin 0.4s ease-out;
}
.slide.active .shape { opacity: 1; }

.slide .shape-enter-left { transform: translateX(-100px) scale(0.7); }
.slide .shape-enter-right { transform: translateX(100px) scale(0.7); }
.slide .shape-enter-top { transform: translateY(-80px) scale(0.7); }
.slide .shape-enter-bottom { transform: translateY(80px) scale(0.7); }

.slide.active .shape-enter-left,
.slide.active .shape-enter-right,
.slide.active .shape-enter-top,
.slide.active .shape-enter-bottom {
  transform: translateX(0) translateY(0) scale(1);
}
```

### Scale-in (for badges, icons)

```css
.slide .anim-scale {
  opacity: 0;
  transform: scale(0.5);
  transition: opacity 0.5s var(--ease-out-expo), transform 0.5s var(--ease-out-back);
}
.slide.active .anim-scale { opacity: 1; transform: scale(1); }
```

---

## Typography

Use `clamp()` for fluid sizing that works on projectors, laptops, and tablets.

```css
.heading-xl {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: clamp(56px, 7.5vw, 112px);
  line-height: 0.92;
  letter-spacing: -0.03em;
}
.heading-lg {
  font-family: var(--font-heading);
  font-weight: 800;
  font-size: clamp(56px, 7.5vw, 112px);
  line-height: 0.92;
  letter-spacing: -0.03em;
}
.heading-md {
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: clamp(24px, 3vw, 42px);
  line-height: 1.2;
}
.italic-accent {
  font-family: var(--font-serif);
  font-style: italic;
  font-weight: 400;
}
.subtitle {
  font-family: var(--font-body);
  font-size: clamp(14px, 1.5vw, 20px);
  font-weight: 500;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  opacity: 0.7;
}
.body-text {
  font-family: var(--font-body);
  font-size: clamp(16px, 1.8vw, 22px);
  line-height: 1.6;
  font-weight: 400;
}
```

---

## UI Chrome

### Progress Bar

```css
.progress-bar {
  position: fixed;
  bottom: 0; left: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--primary), var(--secondary));
  transition: width 0.5s var(--ease-out-expo);
  z-index: 100;
}
```

### Slide Counter

```css
.slide-counter {
  position: fixed;
  bottom: 14px; right: 30px;
  font-family: var(--font-body);
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,0.5);
  z-index: 100;
  transition: color 0.5s;
  letter-spacing: 0.05em;
}
.slide-counter.on-light { color: rgba(45,45,45,0.4); }
```

### Nav Hint

```css
.nav-hint {
  position: fixed;
  bottom: 14px; left: 50%;
  transform: translateX(-50%);
  font-family: var(--font-body);
  font-size: 12px;
  font-weight: 500;
  color: rgba(255,255,255,0.3);
  z-index: 100;
  transition: opacity 1.5s, color 0.5s;
  letter-spacing: 0.05em;
}
.nav-hint.on-light { color: rgba(45,45,45,0.25); }
.nav-hint.hidden { opacity: 0; }
```

### Responsive Breakpoint

```css
@media (max-width: 768px) {
  .slide { padding: 40px 32px; }
  .slide-footer { left: 32px; right: 32px; bottom: 20px; }
  .flow-diagram { flex-direction: column; gap: 12px; }
  .flow-arrow { transform: rotate(90deg); }
  .slide-llm .slide-content { flex-direction: column; gap: 30px; }
  .llm-screenshot { max-width: 100%; }
  .glossary-grid--two { grid-template-columns: 1fr; }
  .slide-learn { padding-left: 40px !important; }
}
```

---

## JavaScript Navigation Engine

Complete template for the IIFE-based slide engine. Adapt `bulletSlides` array to match which slides have `data-bullets`.

```javascript
(function() {
  'use strict';

  // ===== SLIDE ENGINE =====
  const slides = Array.from(document.querySelectorAll('.slide'));
  const totalSlides = slides.length;
  let currentSlide = 0;
  let isTransitioning = false;
  let transitionTimeout = null;

  // Bullet reveal state — track per-slide
  // Find all slides with data-bullets attribute
  const bulletSlides = {};
  slides.forEach((slide, i) => {
    if (slide.dataset.bullets) {
      bulletSlides[i] = { index: 0, total: parseInt(slide.dataset.bullets) };
    }
  });

  const progressBar = document.getElementById('progressBar');
  const slideCounter = document.getElementById('slideCounter');
  const navHint = document.getElementById('navHint');

  function updateUI() {
    const progress = ((currentSlide) / (totalSlides - 1)) * 100;
    progressBar.style.width = progress + '%';
    slideCounter.textContent = (currentSlide + 1) + ' / ' + totalSlides;

    const theme = slides[currentSlide].dataset.theme;
    slideCounter.classList.toggle('on-light', theme === 'light');
    navHint.classList.toggle('on-light', theme === 'light');
  }

  function goToSlide(index) {
    if (index < 0 || index >= totalSlides || index === currentSlide || isTransitioning) return;

    isTransitioning = true;
    clearTimeout(transitionTimeout);

    slides[currentSlide].classList.remove('active');
    currentSlide = index;
    slides[currentSlide].classList.add('active');

    // Reset bullet state when entering a bullet slide
    if (bulletSlides[currentSlide]) {
      resetBullets(currentSlide);
    }

    updateUI();

    transitionTimeout = setTimeout(() => {
      isTransitioning = false;
    }, 700);
  }

  function nextSlide() {
    // Check if current slide has bullets to reveal
    if (bulletSlides[currentSlide]) {
      const state = bulletSlides[currentSlide];
      const bullets = slides[currentSlide].querySelectorAll('.bullet-list li');
      if (state.index < bullets.length) {
        bullets[state.index].classList.add('visible');
        state.index++;
        if (state.index >= bullets.length) {
          const hint = slides[currentSlide].querySelector('.bullet-hint');
          if (hint) hint.classList.add('hidden');
        }
        return;
      }
    }
    goToSlide(currentSlide + 1);
  }

  function prevSlide() {
    if (bulletSlides[currentSlide] && bulletSlides[currentSlide].index > 0) {
      const state = bulletSlides[currentSlide];
      state.index--;
      const bullets = slides[currentSlide].querySelectorAll('.bullet-list li');
      bullets[state.index].classList.remove('visible');
      const hint = slides[currentSlide].querySelector('.bullet-hint');
      if (hint) hint.classList.remove('hidden');
      return;
    }
    goToSlide(currentSlide - 1);
  }

  function resetBullets(slideIndex) {
    bulletSlides[slideIndex].index = 0;
    const bullets = slides[slideIndex].querySelectorAll('.bullet-list li');
    bullets.forEach(b => b.classList.remove('visible'));
    const hint = slides[slideIndex].querySelector('.bullet-hint');
    if (hint) hint.classList.remove('hidden');
  }

  // ===== KEYBOARD NAV =====
  document.addEventListener('keydown', function(e) {
    navHint.classList.add('hidden');
    switch (e.key) {
      case 'ArrowRight': case 'ArrowDown': case ' ': case 'PageDown':
        e.preventDefault(); nextSlide(); break;
      case 'ArrowLeft': case 'ArrowUp': case 'PageUp':
        e.preventDefault(); prevSlide(); break;
      case 'Home':
        e.preventDefault(); goToSlide(0); break;
      case 'End':
        e.preventDefault(); goToSlide(totalSlides - 1); break;
    }
  });

  // ===== CLICK NAV =====
  document.addEventListener('click', function(e) {
    navHint.classList.add('hidden');
    if (e.clientX > window.innerWidth * 0.3) nextSlide();
    else prevSlide();
  });

  // ===== TOUCH/SWIPE NAV =====
  let touchStartX = 0, touchStartY = 0;

  document.addEventListener('touchstart', function(e) {
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
  }, { passive: true });

  document.addEventListener('touchend', function(e) {
    navHint.classList.add('hidden');
    const dx = e.changedTouches[0].clientX - touchStartX;
    const dy = e.changedTouches[0].clientY - touchStartY;
    if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 50) {
      if (dx < 0) nextSlide();
      else prevSlide();
    }
  }, { passive: true });

  // ===== MOUSE PARALLAX =====
  document.addEventListener('mousemove', function(e) {
    const x = (e.clientX / window.innerWidth - 0.5) * 2;
    const y = (e.clientY / window.innerHeight - 0.5) * 2;
    document.documentElement.style.setProperty('--mx', x);
    document.documentElement.style.setProperty('--my', y);
  });

  // ===== INIT =====
  updateUI();
  setTimeout(function() { navHint.classList.add('hidden'); }, 5000);

})();
```

### HTML for UI Chrome (place after `.presentation` div)

```html
<div class="progress-bar" id="progressBar"></div>
<div class="slide-counter" id="slideCounter">1 / N</div>
<div class="nav-hint" id="navHint">Use arrow keys or click to navigate</div>
```
