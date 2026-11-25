# Agent Skills

A collection of knowledge, tips, and resources for the builder community on AI, Claude Code, and other developer tools.

## What's inside

Practical guides, skills, and references for getting the most out of AI-powered development tools.

## Download Build My Designer Brain

[**Download the skill ZIP**](https://github.com/thedesignproject/agent-skills/raw/refs/heads/main/downloads/build-my-designer-brain.zip) · [Setup instructions](guides/build-my-designer-brain.md)

Build your personal critique methods, AI working preferences, optional references and taste, and reusable lessons through a guided interview. No terminal needed for Claude upload.

1. Download the ZIP above. Keep it zipped for Claude.
2. In Claude, open **Customize → Skills → + → Create skill → Upload a skill** and select the ZIP. Enable the skill; file creation must be enabled.
3. Say: **“Use Build My Designer Brain to help me build my personal designer brain.”**

For local coding agents, unzip the download and install the complete folder using the [tool-specific instructions](guides/build-my-designer-brain.md#install-the-shared-skill). ChatGPT installation differs by surface; the ZIP is not a published ChatGPT plugin.

## Quick start: NPX Installation (Recommended)

```bash
# Install all skills — pick from an interactive list of every skill in the repo
npx skills add thedesignproject/agent-skills

# Install one skill
npx skills add thedesignproject/agent-skills -s <skill-name>

# Install several at once
npx skills add thedesignproject/agent-skills -s figma-use -s frontend-design
```

Add `-g` to install globally instead of into the current project. See `npx skills add --help` for the full flag list.

## Skills

Each skill activates in one of two ways, shown in the **How to use** column:

- **Slash command**: invoke it explicitly, e.g. `/create-prd path/to/transcript.md`.
- **Auto**: the skill triggers on its own when your request matches what it does.

Skills are grouped by the kind of work they help with. Skills by Emil Kowalski and Paul Bakaus (Impeccable) are included under their open-source licenses; see [NOTICES.md](NOTICES.md).

### Brand

Identity, type, color and decks.

| Skill | What it does | How to use |
|-------|--------------|------------|
| [presentation](skills/presentation/) | Create polished single-file HTML/CSS/JS slide deck presentations with animations, keyboard/click/swipe navigation, and progressive bullet reveal. | `/presentation [topic]`, or ask Claude to build a slide deck / pitch deck. |
| [extract-design-system](skills/extract-design-system/) | Extracts design primitives (color, typography, spacing) from a public website and generates starter token files. | Auto — ask to extract design tokens or a design system from a website URL. |

### Product

Planning, prototyping, design engineering, motion, review and design systems.

| Skill | What it does | How to use |
|-------|--------------|------------|
| [impeccable](skills/impeccable/) | Paul Bakaus's design skill: shape, critique, audit, polish, typeset, colorize, layout, make bolder or quieter, harden, and more, each as a command. | `/impeccable <command> [target]`, e.g. `/impeccable critique the pricing page`. Auto for design work too. |
| [prototype](skills/prototype/) | Builds several genuinely different versions of a UI piece behind a live picker so you can flip between them and keep one. | `/prototype [what to explore]` |
| [emil-design-eng](skills/emil-design-eng/) | Emil Kowalski's design engineering rules for UI polish, component design, animation decisions and the details that make software feel right. | Auto when building or reviewing UI. |
| [break-ui](skills/break-ui/) | Feeds a piece of UI worst-case data (long names, empty states, huge numbers, non-Latin text) and fixes what breaks. | Auto, or ask to "break this UI". |
| [mobile-native](skills/mobile-native/) | The CSS and meta-tag fixes that make a web app feel native on a phone: tap states, 100vh, input zoom, safe areas. | Auto for mobile web work. |
| [pick-ui-library](skills/pick-ui-library/) | Picks a library for a frontend task from a curated list: primitives, toasts, drawers, command menus, charts, drag and drop. | `/pick-ui-library [task]` |
| [animate](skills/animate/) | Builds an animation from scratch, deciding in order: whether to animate, why, which tool, properties, curve and duration. | Auto when adding motion. |
| [choreograph](skills/choreograph/) | Coordinates several elements animating together so the group reads as one motion. | Auto for multi-element motion. |
| [gestures](skills/gestures/) | Drag, swipe and sheet interactions that track the finger 1:1 and stay interruptible. | Auto for gesture work. |
| [apple-design](skills/apple-design/) | Apple's approach to fluid, physical interface motion, translated for the web. | Auto for springs, sheets and gesture-driven UI. |
| [animation-vocabulary](skills/animation-vocabulary/) | Turns a vague description of a motion effect into its exact name. | Ask "what's it called when..." |
| [review-animations](skills/review-animations/) | Reviews animation code against a high craft bar. Approval is earned. | `/review-animations` |
| [improve-animations](skills/improve-animations/) | Audits a codebase's motion and writes prioritized plans for fixing it. Read-only. | Auto, or ask for a motion audit. |
| [find-animation-opportunities](skills/find-animation-opportunities/) | Finds places that should animate and rejects the ones that shouldn't. Proposes exact values, changes nothing. | Ask "where should this animate?" |
| [remove-animations](skills/remove-animations/) | Finds animations an interface doesn't need and removes them. | Ask to cut unnecessary motion. |
| [animation-performance](skills/animation-performance/) | Keeps web animations inside the frame budget and finds why one drops frames. | Auto when motion is janky. |
| [frontend-design](skills/frontend-design/) | Creates distinctive, production-grade frontend interfaces with high design quality. Avoids the generic "AI aesthetic" of identical sans-serif + flat color UI. | Auto — ask to build web components, pages, or applications. |
| [ux-audit](skills/ux-audit/) | UX and landing page audit: finds the top 3 issues, fixes them, and writes a Loom script to share the changes. | Auto, or ask to audit a page. |
| [accessibility](skills/accessibility/) | Audits and improves web accessibility following WCAG 2.2 — a11y reviews, screen reader support, keyboard navigation. | Auto — ask to "audit accessibility", "a11y audit", "WCAG compliance", or "make accessible". |
| [web-design-guidelines](skills/web-design-guidelines/) | Reviews UI code against Web Interface Guidelines — UX, accessibility, design conventions. | Auto — ask to "review my UI", "audit design", or "check my site against best practices". |
| [create-prd](skills/create-prd/) | Generate structured PRDs from feature request transcripts or descriptions. Researches your codebase for accurate technical scoping and optionally creates Linear projects and issues. | `/create-prd path/to/transcript.md` (or paste the request). Customize `company-context.md` first. |
| [business-kickoff-workshop](skills/business-kickoff-workshop/) | Prepares a customized 45-min Business Model Canvas workshop agenda from customer context before a call, or fills the BMC from a post-call transcript. | Auto — mention a kickoff call, BMC workshop, or business model canvas. |
| [product-context-builder](skills/product-context-builder/) | Creates a connected context system across AGENTS.md, CLAUDE.md, PRODUCT.md, DESIGN.md, and project skills, grounded in the real repository. | Auto — ask to set up or improve AI context files for a product or repository. |
| [agentic-design-systems](skills/agentic-design-systems/) | Designs, scaffolds, extends, or audits a component library whose primary consumer is an AI agent. Generates machine-readable metadata for components, variants, tokens, and anti-patterns. | Auto — ask to build or make a design system AI-readable, define a component metadata schema, or scaffold a UI library for an LLM. |
| [ai-component-metadata](skills/ai-component-metadata/) | Generates AI-ready metadata for design system components. Analyzes structure and produces structured metadata so an agent knows when and how to use each one. | Auto — ask to generate AI-ready metadata for your design-system components. |
| [setup-chromatic](skills/setup-chromatic/) | Sets up Chromatic for Storybook components, application screens, or both, including agent MCP login, CI, and visual-review verification. | Auto — ask to "set up Chromatic" or "add visual regression testing with Chromatic". |
| [figma-use](skills/figma-use/) | Mandatory prerequisite before any `use_figma` MCP call. Foundational context that prevents common write/read failures in Figma. | Auto — loads before any write or scripted read in a Figma file. |
| [figma-generate-design](skills/figma-generate-design/) | Translates an app page, view, or multi-section layout from code into Figma. Push existing pages into Figma without recreating by hand. | Auto — ask to build, write, or push a page/screen/modal to Figma. Pairs with `figma-use`. |
| [pr-branch-naming](skills/pr-branch-naming/) | Generate a conventionally-named branch and PR title from a feature description, with optional one-step branch checkout and draft PR creation. | `/pr-branch-naming [feature description]`, or ask "what should I call this branch / PR?" |

### Marketing

Persuasion, copy and growth.

| Skill | What it does | How to use |
|-------|--------------|------------|
| [marketing-psychology](skills/marketing-psychology/) | Applies psychology, mental models, and behavioral science to marketing — anchoring, social proof, scarcity, loss aversion, framing, nudge. | Auto — ask to apply psychology, persuasion, or behavioral science to marketing. |

### Shared

Making skills and teaching an agent how you work.

| Skill | What it does | How to use |
|-------|--------------|------------|
| [build-my-designer-brain](skills/build-my-designer-brain/) | Builds and evolves a personal designer brain with critique methods, AI working preferences, optional references and taste, and reusable lessons. | Auto — ask to build or update your personal designer brain. Includes a guided interview with write-ins and ranked priorities. |
| [learn-taste](skills/learn-taste/) | Turns a session's design corrections into rules, with their why, in DESIGN.md, a project skill or a lint check. | `/learn-taste` at the end of a session. |
| [create-skill](skills/create-skill/) | Authors new Cursor Agent Skills. Use when writing a new SKILL.md or asking how the skill format works. | Auto — ask to create a new skill or about `SKILL.md` structure. |
| [writing-skills](skills/writing-skills/) | Creates, edits, and verifies skills before deployment. Best practices, examples, graph conventions, subagent-based testing. | Auto — used when creating, editing, or testing skills. |
| [find-skills](skills/find-skills/) | Discovers and installs agent skills when you ask "is there a skill for X?" — surfaces things you didn't know existed. | Auto — ask "find a skill for X" or "how do I do X". |
| [prompt-engineer](skills/prompt-engineer/) | Writes, refactors, and evaluates LLM prompts — templates, structured output schemas, evaluation rubrics, test suites. | Auto — ask to write, refactor, or evaluate prompts (chain-of-thought, few-shot, system prompts). |
| [caveman](skills/caveman/) | Ultra-compressed communication mode. Cuts token usage ~75% by speaking like caveman while keeping technical accuracy. Levels: lite, full, ultra. | `/caveman`, or say "caveman mode" / "be brief" / "less tokens". |

### Team

Internal reviews.

| Skill | What it does | How to use |
|-------|--------------|------------|
| [performance-review-360-peer](skills/performance-review-360-peer/) | Helps someone give peer feedback using Non-Violent Communication. | Ask for help writing peer feedback. |
| [performance-review-manager](skills/performance-review-manager/) | Walks a manager through a quarterly review for a direct report. | Ask to prepare a performance review. |
| [performance-review-self-assessment](skills/performance-review-self-assessment/) | Helps an employee write their quarterly self-assessment. | Ask for help with your self-assessment. |

## Guides

| Guide | Description |
|-------|-------------|
| [build-my-designer-brain](guides/build-my-designer-brain.md) | Install the personal designer-brain skill, run the interview, and reuse the resulting knowledge in project work. |
| [pr-and-branch-naming](guides/github-for-designers/pr-and-branch-naming.md) | A simple convention for naming pull requests and branches when working on a client codebase, with an optional TDP prefix to make designer-authored work easy to spot. |

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Please note that this project follows a [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](LICENSE).
