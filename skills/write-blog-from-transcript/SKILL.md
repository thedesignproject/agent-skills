---
name: writing-blog-posts-from-transcripts
description: Transforms YouTube video transcripts into structured, publish-ready blog posts for The Design Project (TDP), a design engineering agency serving B2B SaaS startups. Use when asked to write a blog post from a YouTube transcript, convert a video into a blog article, repurpose video content into written content, or turn a transcript into a TDP blog post. Also use when editing or refining a previously generated blog post from a transcript.
---

# Writing Blog Posts from Transcripts

## Workflow

### 1. Analyze the transcript

Before writing, extract from the transcript:

- **Core topic** — the single main concept
- **Key points** — 3-7 distinct ideas or steps
- **Stories and examples** — client anecdotes, case studies with specific details
- **Metrics** — numbers, percentages, timeframes, results
- **Quotable moments** — strong opinions, memorable phrasing

If the transcript is rambling or covers multiple topics, pick the strongest single thread. Flag anything omitted.

### 2. Determine search intent

Before structuring, identify what someone searching for the target keyword actually wants:

- **Informational** ("what is X", "how to X") → go deep on explanation, examples, and step-by-step. Longer form.
- **Transactional** ("best X tool", "X service") → lead with comparisons, pros/cons, and clear recommendations. Medium length.
- **Navigational** ("X platform login", "X documentation") → rarely our target. If the keyword is navigational, pivot to an informational angle.

Google the primary keyword. Look at the top 3 results — what format are they? What depth? Match or exceed that depth. Note any "People Also Ask" questions to address in the post.

### 3. Choose structure

Map content onto the blog template in [references/blog-template.md](references/blog-template.md). Read that file before writing.

The template follows: **Hook → Table of Contents → What → Why → Examples → How → Tools/Resources → CTA → Related Reading**.

Adapt based on video type:

- **Tutorial** → emphasize What + How, minimize Why. Use numbered steps for featured snippet potential.
- **Case study** → emphasize Examples, brief What. Lead with results for transactional intent.
- **Thought leadership** → emphasize Why + What, light Examples. Good for informational intent.
- **Comparison** → use "vs." subsections as backbone. Use tables for featured snippet potential.

Not every section is required. Skip sections that would feel forced.

### 4. Write the post

**Voice rules:**

- Conversational, confident, never corporate
- First-person experience: "We've been testing..." not "Here's how you should..."
- Parenthetical asides and light humor
- No emojis in body text. Minimal exclamation marks.

**Formatting:**

- Sentence case headers
- Bold only for key terms on first use or benefit headlines
- Paragraphs: 3-4 sentences max
- Bullets only for 3+ genuinely parallel items — default to prose
- No section over 300 words without a visual break
- Use `[IMAGE: description]` placeholders where visuals help

**Transcript transformation:**

- Never transcribe verbatim — restructure completely for reading
- Cut filler ("you know," "so basically," "right?")
- Collapse repetitive explanations into single clear statements
- Expand strong throwaway mentions into full paragraphs
- Replace "as you can see here" with written descriptions
- Convert spoken examples into mini case study format: problem → solution → results

**SEO:**

- Title: `[Primary Keyword]: [Compelling promise]`
- Slug: 3-5 keyword-rich words only (e.g., `design-system-mistakes` not `5-design-system-mistakes-startups-make-and-how-to-fix-them`)
- Primary keyword in title, first H2, first 100 words
- Secondary/semantic keywords: identify 3-5 related terms from "People Also Ask" and competitor posts. Place naturally in H2s and body — never force them.
- Table of contents with anchor links
- Featured snippet optimization:
  - Key definitions: write as standalone 40-60 word paragraphs immediately after the H2
  - Processes: use numbered lists (Google pulls these as featured snippets)
  - Comparisons: use markdown tables with clear column headers
- E-E-A-T signals: weave in first-person experience ("We built this for a client who..."), specific examples with names/metrics, concrete timelines, and link to authoritative external sources (2-3 per post)
- Use `[INTERNAL LINK: topic]` and `[EXTERNAL LINK: topic]` placeholders

**TDP context** (weave in only when naturally relevant):

- TDP converts Figma designs into production-ready code
- Clients: funded B2B SaaS startups, 6-18 months post-funding
- Value prop: eliminate design-to-dev handoffs, ship faster
- Verticals: healthcare, B2B SaaS, EdTech

### 5. Self-review

Verify before outputting:

- Hook is specific and opinionated, not generic
- Logical flow: What → Why → Examples → How
- Examples include concrete metrics
- How section is immediately actionable
- Answers "so what?" within first 3 paragraphs
- Sounds like a person, not a brand
- No references to "the video" or "this episode"
- Title contains keyword + compelling promise
- Slug is 3-5 words, keyword-rich, no filler words
- Table of contents present with anchors
- 3-5 secondary keywords placed naturally in H2s and body
- At least one featured-snippet-ready element (definition paragraph, numbered list, or comparison table)
- E-E-A-T: at least 2 first-person experience references, 1 specific client/project example, 2-3 external authority links

### 6. Output

Save as markdown using the optimized slug as filename (e.g., `design-system-mistakes.md` — match the slug field, not the full title).

Append a content brief after the post:

```
## Content Brief
- **Title:** [final title]
- **Slug:** [3-5 keyword-rich words]
- **Primary Keyword:** [keyword]
- **Secondary Keywords:** [3-5 related terms]
- **Search Intent:** [informational / transactional / navigational]
- **Meta Description:** [under 160 chars]
- **Suggested Categories:** [1-2]
- **Internal Link Opportunities:** [topics]
- **Social Pull Quotes:** [2-3 sentences for social repurposing]
- **Word Count:** [X words]
```

### 7. Generate cover image

Run the hero image generator to create a branded cover image for the post:

```bash
python3 scripts/generate-hero.py "Blog Post Title Here" --output /path/to/output/
```

The script creates a 1200x630 TDP-branded image with the title rendered on a colored background. It rotates through brand colors (charcoal, purple, orange, lime green) and adds decorative elements for visual interest.

The image saves as `[slug].png` alongside the markdown file. When the post is published to Ghost using the publish script, the image is automatically uploaded and set as the feature image.
