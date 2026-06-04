# Agent Skills

A collection of knowledge, tips, and resources for the builder community on AI, Claude Code, and other developer tools.

## What's inside

Practical guides, skills, and references for getting the most out of AI-powered development tools.

## Install

Skills install via the [vercel-labs/skills](https://github.com/vercel-labs/skills) CLI — works with Claude Code, Codex, Cursor, and 60+ other agents.

```bash
# Install one skill
npx skills add thedesignproject/agent-skills -s <skill-name>

# Install several at once
npx skills add thedesignproject/agent-skills -s figma-use -s frontend-design

# Pick from an interactive list of every skill in the repo
npx skills add thedesignproject/agent-skills
```

Add `-g` to install globally instead of into the current project. See `npx skills add --help` for the full flag list.

## Skills

| Skill | Description |
|-------|-------------|
| [accessibility](skills/accessibility/) | Audits and improves web accessibility following WCAG 2.2 — a11y reviews, screen reader support, keyboard navigation. |
| [agentic-design-systems](skills/agentic-design-systems/) | Designs, scaffolds, extends, or audits a component library whose primary consumer is an AI agent. Generates machine-readable metadata for components, variants, tokens, and anti-patterns. |
| [ai-component-metadata](skills/ai-component-metadata/) | Generates AI-ready metadata for design system components. Analyzes structure and produces structured metadata so an agent knows when and how to use each one. |
| [business-kickoff-workshop](skills/business-kickoff-workshop/) | Prepares a customized 45-min Business Model Canvas workshop agenda from customer context before a call, or fills the BMC from a post-call transcript. |
| [caveman](skills/caveman/) | Ultra-compressed communication mode. Cuts token usage ~75% by speaking like caveman while keeping technical accuracy. Levels: lite, full, ultra. |
| [create-prd](skills/create-prd/) | Generate structured PRDs from feature request transcripts or descriptions. Researches your codebase for accurate technical scoping and optionally creates Linear projects and issues. |
| [create-skill](skills/create-skill/) | Authors new Cursor Agent Skills. Use when writing a new SKILL.md or asking how the skill format works. |
| [extract-design-system](skills/extract-design-system/) | Extracts design primitives (color, typography, spacing) from a public website and generates starter token files. |
| [figma-generate-design](skills/figma-generate-design/) | Translates an app page, view, or multi-section layout from code into Figma. Push existing pages into Figma without recreating by hand. |
| [figma-use](skills/figma-use/) | Mandatory prerequisite before any `use_figma` MCP call. Foundational context that prevents common write/read failures in Figma. |
| [find-skills](skills/find-skills/) | Discovers and installs agent skills when you ask "is there a skill for X?" — surfaces things you didn't know existed. |
| [frontend-design](skills/frontend-design/) | Creates distinctive, production-grade frontend interfaces with high design quality. Avoids the generic "AI aesthetic" of identical sans-serif + flat color UI. |
| [marketing-psychology](skills/marketing-psychology/) | Applies psychology, mental models, and behavioral science to marketing — anchoring, social proof, scarcity, loss aversion, framing, nudge. |
| [pr-branch-naming](skills/pr-branch-naming/) | Generate a conventionally-named branch and PR title from a feature description, with optional one-step branch checkout and draft PR creation. |
| [presentation](skills/presentation/) | Create polished single-file HTML/CSS/JS slide deck presentations with animations, keyboard/click/swipe navigation, and progressive bullet reveal. |
| [prompt-engineer](skills/prompt-engineer/) | Writes, refactors, and evaluates LLM prompts — templates, structured output schemas, evaluation rubrics, test suites. |
| [web-design-guidelines](skills/web-design-guidelines/) | Reviews UI code against Web Interface Guidelines — UX, accessibility, design conventions. |
| [writing-skills](skills/writing-skills/) | Creates, edits, and verifies skills before deployment. Best practices, examples, graph conventions, subagent-based testing. |

## Guides

| Guide | Description |
|-------|-------------|
| [pr-and-branch-naming](guides/github-for-designers/pr-and-branch-naming.md) | A simple convention for naming pull requests and branches when working on a client codebase, with an optional TDP prefix to make designer-authored work easy to spot. |

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Please note that this project follows a [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](LICENSE).
