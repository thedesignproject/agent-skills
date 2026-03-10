---
name: review-thumbnail
description: Analyzes a YouTube thumbnail image and suggests improvements based on MrBeast's proven thumbnail strategies. Use when asked to review a thumbnail, improve a thumbnail, analyze a thumbnail, give feedback on a YouTube thumbnail, or when the user shares a thumbnail image.
argument-hint: [thumbnail-path]
allowed-tools: Read
---

# Review YouTube Thumbnail

Analyze a YouTube thumbnail and provide actionable improvement suggestions based on MrBeast's team principles.

## Inputs

- `$0` — path to the thumbnail image file (.png, .jpg, .webp)

If the argument is not provided, ask the user for the thumbnail path.

## Workflow

### 1. Load the thumbnail

Use the Read tool to view the image file. If the file doesn't exist, tell the user and ask for a corrected path.

### 2. Load the evaluation criteria

Read [mrbeast-principles.md](mrbeast-principles.md) for the full set of criteria and evaluation questions.

### 3. Analyze the thumbnail

Evaluate the thumbnail against each of the 7 criteria (A through G) from the principles file. For each criterion, assign a score:

- **Strong** — meets the principle well
- **Needs Work** — partially meets it, with clear room for improvement
- **Missing** — does not address the principle at all

### 4. Present the review

**Overall Impression:** One sentence summary of the thumbnail's effectiveness.

| Criteria | Score | Notes |
|----------|-------|-------|
| Simplicity & Story | ... | ... |
| Facial Expression | ... | ... |
| High-Contrast Colors | ... | ... |
| Text (Minimal & Bold) | ... | ... |
| Curiosity & Intrigue | ... | ... |
| Branding & Consistency | ... | ... |
| Trust & Deliverability | ... | ... |

### 5. Top 3 improvements

List the **top 3 most impactful changes** ordered by expected impact on click-through rate. Be specific and actionable — say exactly what to change, not vague advice like "make it more colorful."

### 6. A/B test suggestion

Suggest one concrete A/B test variation following MrBeast's practice of testing multiple thumbnail versions. Describe the alternate version in enough detail that a designer could produce it.
