# Slide Type Templates

HTML templates for each slide type. Load this file when building slides (Step 5).

Adapt class names, colors, content, and shapes to match each presentation's design brief. The patterns here are structural — the visual identity comes from the CSS tokens defined in the framework.

---

## 1. Title Slide (`.slide-title`)

Opening slide with large heading, decorative shapes, and glass panel.

```html
<section class="slide slide--primary slide-title active" data-theme="dark">
  <!-- Decorative shapes — bleed off edges, luminosity blend -->
  <div class="shape shape-pill shape-enter-left" style="top:15%; left:-5%; width:200px;"></div>
  <div class="shape shape-sphere shape-enter-right" style="top:-10%; right:-3%; width:180px; height:180px;"></div>
  <div class="shape shape-star shape-enter-bottom" style="bottom:-8%; left:20%;"></div>

  <!-- Optional glass panel -->
  <div class="glass-panel"></div>

  <!-- Header chrome -->
  <div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.18); z-index:10; pointer-events:none;">
    <span style="font-size:clamp(10px,1vw,14px); font-weight:600; letter-spacing:0.12em; text-transform:uppercase; opacity:0.5;">Tagline</span>
    <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em;">Logo</span>
  </div>

  <div class="slide-content" style="z-index:4; position:relative;">
    <div class="title-main anim anim-d1">First Line</div>
    <div class="title-main anim anim-d2">Second <span class="italic-accent">Line</span></div>
  </div>

  <div class="slide-footer" style="z-index:4;">
    <span class="anim anim-d3">Presenter Name @ Role</span>
  </div>
</section>
```

**CSS (slide-specific):**
```css
.slide-title {
  justify-content: center !important;
  align-items: flex-start !important;
  padding-left: 8vw !important;
  padding-right: 8vw !important;
}
.slide-title .slide-content {
  text-align: left; z-index: 3; position: relative;
  display: flex; flex-direction: column; align-items: flex-start; gap: 0;
}
.slide-title .title-main {
  font-family: var(--font-heading); font-weight: 800;
  font-size: clamp(56px, 7.5vw, 112px); line-height: 0.92; letter-spacing: -0.03em;
}
```

---

## 2. Speaker/Bio Slide (`.slide-speaker`)

Introduce the presenter with avatar, name, role, and glass card backdrop.

```html
<section class="slide slide--primary slide-speaker" data-theme="dark">
  <!-- Shapes -->
  <div class="shape shape-sphere shape-enter-left" style="top:-18%; left:-10%; width:200px; height:200px;"></div>
  <div class="shape shape-pill shape-enter-right" style="bottom:-10%; right:-6%;"></div>

  <!-- Glass card -->
  <div class="glass-panel"></div>

  <div class="speaker-layout">
    <div class="avatar-ring anim anim-d1 anim-scale">
      <img src="avatar.jpg" alt="Name">
    </div>
    <div class="speaker-subtitle anim anim-d2">Tagline or motto</div>
    <div class="speaker-name anim anim-d3">Full Name</div>
    <div class="speaker-title-text anim anim-d4">title &amp; company</div>
  </div>

  <div class="slide-footer" style="z-index:3;">
    <span>Presentation Title</span>
    <span class="italic-accent">subtitle</span>
  </div>
</section>
```

**CSS (slide-specific):**
```css
.slide-speaker .speaker-layout {
  display: flex; flex-direction: column; align-items: center;
  gap: 28px; z-index: 3; position: relative;
}
.avatar-ring {
  width: clamp(160px, 18vw, 240px); height: clamp(160px, 18vw, 240px);
  border-radius: 50%; border: 3px solid rgba(255,255,255,0.3);
  overflow: hidden;
  background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
  display: flex; align-items: center; justify-content: center;
}
.avatar-ring img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
.speaker-name {
  font-family: var(--font-heading); font-weight: 700;
  font-size: clamp(20px, 2.5vw, 32px); text-align: center;
}
.speaker-title-text {
  font-size: clamp(13px, 1.2vw, 16px); opacity: 0.6;
  font-weight: 500; letter-spacing: 0.1em; text-transform: lowercase;
}
.speaker-subtitle {
  font-family: var(--font-serif); font-style: italic;
  font-size: clamp(18px, 2.2vw, 30px); opacity: 0.7;
}
```

---

## 3. Question Slide (`.slide-familiar`)

Large centered question for audience engagement.

```html
<section class="slide slide--primary slide-familiar" data-theme="dark" style="justify-content:center; align-items:flex-start; padding:0 8vw;">
  <!-- Header -->
  <div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.18); z-index:10; pointer-events:none;">
    <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em;">Logo</span>
  </div>

  <!-- Shapes -->
  <div class="shape shape-sphere shape-enter-left" style="top:-2%; right:22%; width:18vw; max-width:240px;"></div>

  <div class="slide-content" style="flex-direction:column; align-items:flex-start; text-align:left; gap:0;">
    <div class="heading-xl anim anim-d1">Does This</div>
    <div class="heading-xl anim anim-d2"><span class="italic-accent">Sound Familiar?</span></div>
  </div>

  <div class="slide-footer">
    <span>Presentation Title</span>
    <span>Subtitle</span>
  </div>
</section>
```

---

## 4. Bullet Reveal Slide (`.slide-learn`)

Progressive disclosure — bullets appear one by one on click/keypress.

```html
<section class="slide slide--secondary slide-learn" data-theme="dark" data-bullets="4" style="justify-content:center !important; align-items:flex-start !important; padding:0 8vw !important;">
  <!-- Header -->
  <div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.2); z-index:10; pointer-events:none;">
    <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em;">Logo</span>
  </div>

  <!-- Large decorative shape -->
  <div class="shape shape-star shape-enter-right" style="position:absolute; top:50%; right:-18%; transform:translateY(-50%); width:500px; height:500px; opacity:0.75; z-index:1;"></div>

  <div class="slide-content" style="flex-direction:column; align-items:flex-start; justify-content:center; gap:5vh; z-index:3;">
    <div>
      <div class="heading-lg anim anim-d1">What You&rsquo;ll</div>
      <div class="heading-lg anim anim-d2"><span class="italic-accent">Learn Today</span></div>
    </div>
    <ul class="bullet-list">
      <li data-bullet="1">First point to reveal</li>
      <li data-bullet="2">Second point to reveal</li>
      <li data-bullet="3">Third point to reveal</li>
      <li data-bullet="4">Fourth point to reveal</li>
    </ul>
    <div class="bullet-hint">Press &rarr; to reveal next point</div>
  </div>

  <div class="slide-footer">
    <span>Presentation Title</span>
    <span>Subtitle</span>
  </div>
</section>
```

**Key:** `data-bullets="4"` on the section tells the JS engine how many bullets to reveal before advancing. Each `<li>` starts hidden and gets `.visible` class on click.

**CSS (slide-specific):**
```css
.slide-learn { align-items: flex-start !important; padding-left: 12% !important; }
.slide-learn .slide-content {
  z-index: 1; display: flex; flex-direction: column; gap: 12px; max-width: 750px;
}
.bullet-list {
  list-style: none; display: flex; flex-direction: column; gap: 18px; margin-top: 24px;
}
.bullet-list li {
  font-family: var(--font-body); font-size: clamp(18px, 2vw, 26px); font-weight: 500;
  line-height: 1.4; padding-left: 28px; position: relative;
  opacity: 0; transform: translateY(16px);
  transition: opacity 0.5s var(--ease-out-expo), transform 0.5s var(--ease-out-expo);
}
.bullet-list li.visible { opacity: 1; transform: translateY(0); }
.bullet-list li::before {
  content: ''; position: absolute; left: 0; top: 8px;
  width: 10px; height: 10px; border-radius: 50%; background: rgba(255,255,255,0.6);
}
.bullet-hint {
  font-size: 14px; opacity: 0.4; font-weight: 500; margin-top: 20px; transition: opacity 0.3s;
}
.bullet-hint.hidden { opacity: 0; }
```

---

## 5. Tool/Badge Grid Slide (`.slide-setup`)

Grid of tool badges with icons.

```html
<section class="slide slide--light slide-setup" data-theme="light" style="justify-content:center; align-items:flex-start; padding:0 8vw;">
  <!-- Header -->
  <div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(28,28,28,0.1); z-index:10; pointer-events:none;">
    <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em; color:var(--dark);">Logo</span>
  </div>

  <div class="slide-content" style="flex-direction:column; align-items:flex-start; gap:5vh; padding-top:4vh;">
    <div>
      <div class="heading-lg anim anim-d1" style="color:var(--dark);">Setting Up</div>
      <div class="heading-lg anim anim-d2" style="color:var(--dark);">Your <span class="italic-accent">Environment</span></div>
    </div>

    <div class="tool-grid" style="justify-content:flex-start;">
      <div class="tool-badge anim-scale anim-d3">
        <div class="badge-icon" style="background:#24292e;">G</div>
        Tool Name
      </div>
      <div class="tool-badge anim-scale anim-d4">
        <div class="badge-icon" style="background:#000;">C</div>
        Another Tool
      </div>
      <!-- Add more badges as needed -->
    </div>
  </div>

  <div class="slide-footer">
    <span>Presentation Title</span>
    <span>Subtitle</span>
  </div>
</section>
```

**CSS (slide-specific):**
```css
.tool-grid { display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; margin-top: 16px; }
.tool-badge {
  display: flex; align-items: center; gap: 10px; padding: 14px 28px;
  border-radius: 50px; font-family: var(--font-heading); font-weight: 700;
  font-size: clamp(14px, 1.4vw, 18px); letter-spacing: 0.04em; text-transform: uppercase;
  background: var(--white); color: var(--dark); box-shadow: 0 4px 20px rgba(0,0,0,0.06);
}
.tool-badge .badge-icon {
  width: 28px; height: 28px; border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; font-weight: 800; color: white;
}
```

---

## 6. Workflow/Flow Slide (`.slide-flow`)

Connected process steps with arrows.

```html
<section class="slide slide--primary slide-flow" data-theme="dark">
  <!-- Shapes -->
  <div class="shape shape-sphere shape-enter-left" style="bottom:-8%; left:-4%; width:200px; height:200px; opacity:0.45;"></div>

  <div class="slide-content">
    <div class="heading-lg anim anim-d1" style="text-align:center;">How They Work <span class="italic-accent">Together</span></div>

    <div class="flow-diagram">
      <div class="flow-step anim anim-d2">
        <div class="flow-box">Step 1</div>
        <div class="flow-label">description</div>
      </div>
      <div class="flow-arrow anim anim-d3">&rarr;</div>
      <div class="flow-step anim anim-d3">
        <div class="flow-box">Step 2</div>
        <div class="flow-label">description</div>
      </div>
      <div class="flow-arrow anim anim-d4">&rarr;</div>
      <div class="flow-step anim anim-d4">
        <div class="flow-box">Step 3</div>
        <div class="flow-label">description</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span>Presentation Title</span>
    <span class="italic-accent">subtitle</span>
  </div>
</section>
```

**CSS (slide-specific):**
```css
.slide-flow .slide-content {
  z-index: 1; width: 100%; max-width: 1000px;
  display: flex; flex-direction: column; align-items: center; gap: 40px;
}
.flow-diagram { display: flex; align-items: center; gap: 0; width: 100%; justify-content: center; }
.flow-step { display: flex; flex-direction: column; align-items: center; gap: 10px; min-width: 120px; }
.flow-box {
  padding: 16px 24px; border-radius: 14px;
  background: rgba(255,255,255,0.15); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.2);
  font-family: var(--font-heading); font-weight: 700; font-size: clamp(13px, 1.4vw, 18px);
  text-align: center; white-space: nowrap;
}
.flow-label { font-size: clamp(11px, 1vw, 14px); opacity: 0.5; font-weight: 500; text-transform: lowercase; }
.flow-arrow { font-size: 24px; opacity: 0.4; margin: 0 8px; flex-shrink: 0; }
```

---

## 7. Two-Column Slide (`.slide-llm`)

Text on left, image/screenshot on right.

```html
<section class="slide slide--light slide-llm" data-theme="light">
  <!-- Header -->
  <div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(28,28,28,0.1); z-index:10; pointer-events:none;">
    <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em; color:var(--dark);">Logo</span>
  </div>

  <div class="slide-content">
    <div class="llm-text">
      <div class="heading-lg anim anim-d1" style="color:var(--dark);">First Line</div>
      <div class="heading-lg anim anim-d2" style="color:var(--dark);"><span class="italic-accent">Second Line</span></div>
      <div style="display:flex; flex-direction:column; gap:10px; margin-top:20px;">
        <div class="open-source-badge anim-scale anim-d3">Badge Text</div>
      </div>
    </div>
    <div class="llm-screenshot anim anim-d3">
      <img src="screenshot.png" alt="Description">
    </div>
  </div>

  <div class="slide-footer">
    <span>Presentation Title</span>
    <span>Subtitle</span>
  </div>
</section>
```

**CSS (slide-specific):**
```css
.slide-llm .slide-content {
  z-index: 1; display: flex; align-items: center; gap: 60px; width: 100%; max-width: 1100px;
}
.llm-text { flex: 1; display: flex; flex-direction: column; gap: 16px; }
.llm-screenshot {
  flex: 1; max-width: 480px; border-radius: 16px; overflow: hidden;
  box-shadow: 0 16px 60px rgba(0,0,0,0.12); background: var(--white);
  border: 1px solid rgba(0,0,0,0.06);
}
.llm-screenshot img { width: 100%; display: block; }
.open-source-badge {
  display: inline-block; padding: 6px 18px; border-radius: 20px;
  background: var(--secondary); color: var(--white);
  font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;
  width: fit-content;
}
```

---

## 8. Team/Grid Slide (`.slide-speakers`)

Photo grid with names and roles for multiple people.

```html
<section class="slide slide--primary slide-speakers" data-theme="dark">
  <!-- Header chrome -->
  <div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.18); z-index:10; pointer-events:none;">
    <span style="font-size:clamp(10px,1vw,14px); font-weight:600; letter-spacing:0.12em; text-transform:uppercase; opacity:0.5;">Tagline</span>
    <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em;">Logo</span>
  </div>

  <!-- Glass backdrop -->
  <div class="speakers-glass"></div>

  <div class="speakers-layout">
    <div class="speakers-intro anim anim-d1">Meet the team</div>
    <div class="speakers-row">
      <div class="speaker-card anim anim-d2">
        <div class="avatar-ring"><img src="person1.jpg" alt="Name"></div>
        <div class="speaker-name">Full Name</div>
        <div class="speaker-handle">@handle · role</div>
      </div>
      <div class="speaker-card anim anim-d3">
        <div class="avatar-ring"><img src="person2.jpg" alt="Name"></div>
        <div class="speaker-name">Full Name</div>
        <div class="speaker-handle">@handle · role</div>
      </div>
      <div class="speaker-card anim anim-d4">
        <div class="avatar-ring"><img src="person3.jpg" alt="Name"></div>
        <div class="speaker-name">Full Name</div>
        <div class="speaker-handle">@handle · role</div>
      </div>
    </div>
  </div>

  <div class="slide-footer" style="z-index:3;">
    <span>Presentation Title</span>
    <span class="italic-accent">subtitle</span>
  </div>
</section>
```

**CSS (slide-specific):**
```css
.slide-speakers { justify-content: center !important; align-items: center !important; }
.speakers-glass {
  position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
  width: 88%; height: 80%;
  background: rgba(255,255,255,0.06); backdrop-filter: blur(28px); -webkit-backdrop-filter: blur(28px);
  border-radius: 40px; border: 1px solid rgba(255,255,255,0.15); z-index: 2; pointer-events: none;
}
.speakers-layout {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  gap: 0; z-index: 3; position: relative;
}
.speakers-row {
  display: flex; align-items: center; justify-content: center;
  gap: clamp(40px, 6vw, 96px);
}
.speaker-card {
  display: flex; flex-direction: column; align-items: center;
  gap: clamp(10px, 1.4vh, 18px); text-align: center;
}
.speaker-card .avatar-ring { width: clamp(110px, 12vw, 170px); height: clamp(110px, 12vw, 170px); }
.speaker-card .speaker-name { font-size: clamp(14px, 1.5vw, 22px); }
.speaker-handle {
  font-family: var(--font-body); font-size: clamp(10px, 0.9vw, 13px);
  font-weight: 500; letter-spacing: 0.08em; opacity: 0.45;
}
.speakers-intro {
  font-family: var(--font-serif); font-style: italic;
  font-size: clamp(16px, 2vw, 28px); opacity: 0.65;
  margin-bottom: clamp(20px, 3.5vh, 44px); text-align: center;
}
```

---

## 9. Glossary/Definition Slide (`.slide-gloss`)

Large term with definition — one concept per slide.

```html
<section class="slide slide--light slide-gloss" data-theme="light">
  <!-- Header chrome -->
  <div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(28,28,28,0.1); z-index:10; pointer-events:none;">
    <span style="font-size:clamp(10px,1vw,14px); font-weight:600; letter-spacing:0.12em; text-transform:uppercase; opacity:0.5; color:var(--dark);">Tagline</span>
    <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em; color:var(--dark);">Logo</span>
  </div>

  <div class="slide-content" style="flex-direction:column; align-items:flex-start; gap:0; z-index:3;">
    <p class="gloss-eyebrow anim anim-d1">Glossary</p>
    <h2 class="gloss-term anim anim-d2">Term<br><em>Name</em></h2>
    <div class="gloss-rule anim anim-d3"></div>
    <p class="gloss-def anim anim-d4"><span class="gloss-arrow">&rarr;</span>Definition text goes here explaining the concept clearly.</p>
  </div>

  <div class="slide-footer" style="z-index:4;">
    <span class="anim anim-d3">Presenter Name @ Role</span>
  </div>
</section>
```

**CSS (slide-specific):**
```css
.slide-gloss {
  align-items: flex-start !important; justify-content: center !important; padding: 0 8vw !important;
}
.slide-gloss .slide-content {
  z-index: 3; display: flex; flex-direction: column; align-items: flex-start; gap: 0; max-width: 900px;
}
.gloss-eyebrow {
  font-family: var(--font-body); font-size: clamp(11px, 1vw, 14px); font-weight: 700;
  letter-spacing: 0.22em; text-transform: uppercase; opacity: 0.4; margin-bottom: 2.5vh;
}
.gloss-term {
  font-family: var(--font-heading); font-weight: 800;
  font-size: clamp(60px, 8.5vw, 130px); line-height: 0.88; letter-spacing: -0.04em; margin-bottom: 4vh;
}
.gloss-term em {
  font-family: var(--font-serif); font-style: italic; font-weight: 400; letter-spacing: -0.02em;
}
.gloss-rule {
  width: clamp(200px, 35vw, 560px); height: 1px;
  background: currentColor; opacity: 0.18; margin-bottom: 4vh;
}
.gloss-def {
  font-family: var(--font-body); font-size: clamp(17px, 1.9vw, 27px); font-weight: 500;
  line-height: 1.6; max-width: 680px; opacity: 0.85;
}
.gloss-arrow { display: inline-block; margin-right: 6px; opacity: 0.5; }
```

**Note:** Glossary slides work well alternating between theme variants (`.slide--primary`, `.slide--secondary`, `.slide--light`) for visual variety.

---

## 10. Closing/CTA Slide (`.slide-closing`)

Final slide with large text and call to action.

```html
<section class="slide slide--primary slide-closing" data-theme="dark">
  <!-- Shapes — dense layering for dramatic finish -->
  <div class="shape shape-pill shape-enter-left" style="top:-16%; left:-8%; width:300px; opacity:0.3;"></div>
  <div class="shape shape-star shape-enter-right" style="top:-10%; right:-7%; width:250px; height:250px; opacity:0.55; z-index:3;"></div>
  <div class="shape shape-sphere shape-enter-bottom" style="bottom:-12%; left:-5%; width:280px; height:280px; opacity:0.3;"></div>

  <!-- Glass card -->
  <div class="glass-panel"></div>

  <!-- Header chrome -->
  <div style="position:absolute; top:0; left:0; right:0; padding:2vh 4vw; display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.18); z-index:10; pointer-events:none;">
    <span style="font-size:clamp(10px,1vw,14px); font-weight:600; letter-spacing:0.12em; text-transform:uppercase; opacity:0.5;">Tagline</span>
    <span style="font-size:clamp(14px,1.3vw,20px); font-weight:800; letter-spacing:-0.02em;">Logo</span>
  </div>

  <div class="slide-content" style="flex-direction:column; align-items:center; text-align:center; gap:0; z-index:4; position:relative;">
    <div class="title-main anim anim-d1">Thank</div>
    <div class="title-main anim anim-d2"><span class="italic-accent">You!</span></div>
  </div>

  <div class="slide-footer" style="z-index:4;">
    <span class="anim anim-d3">Presenter Name @ Role</span>
  </div>
</section>
```

**CSS (slide-specific):**
```css
.slide-closing .slide-content {
  text-align: center; z-index: 4; position: relative;
  display: flex; flex-direction: column; align-items: center; gap: 0;
}
.slide-closing .title-main {
  font-family: var(--font-heading); font-weight: 800;
  font-size: clamp(60px, 8vw, 120px); line-height: 0.9; letter-spacing: -0.03em;
}
```
