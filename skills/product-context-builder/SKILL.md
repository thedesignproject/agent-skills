---
name: product-context-builder
description: Create or improve a repo's AGENTS.md, CLAUDE.md, PRODUCT.md, DESIGN.md, and project skills so AI agents can use the product and design system accurately.
---

# Product Context Builder

Build a compact, connected context system grounded in the user's real product and repository. The finished files should help an AI agent understand the codebase, the product judgment behind it, the visual system it must reuse, and the task-specific workflows it can load when relevant.

## Start by discovering what exists

Inspect the repository before interviewing the user. Locate:

- existing `AGENTS.md`, `CLAUDE.md`, `PRODUCT.md`, `DESIGN.md`, and skill folders
- package scripts, build and test commands, source directories, and contribution rules
- UI components, Storybook stories, theme files, CSS variables, Tailwind configuration, and token packages
- product documentation, PRDs, research, brand guidance, and accessibility requirements

Report what you found, what can be inferred safely, and what needs a human answer. Never invent commands, component names, product positioning, tokens, or constraints.

## Choose the files that earn their place

Do not generate every file automatically.

- Create or update `AGENTS.md` when multiple coding agents need stable repository instructions.
- Create or update `CLAUDE.md` when Claude Code needs tool-specific guidance that is meaningfully different. Keep shared rules aligned with `AGENTS.md`.
- Create `PRODUCT.md` when agents need durable product judgment: audience, purpose, personality, principles, references, and anti-references.
- Create `DESIGN.md` when a real visual system or component library can be documented from evidence.
- Create a project skill only for a repeatable task with a recognizable trigger and a stable workflow.

Read the matching guide before drafting a file:

- [Always-loaded files](references/always-loaded-files.md)
- [PRODUCT.md](references/product.md)
- [DESIGN.md](references/design.md)
- [Project skills](references/project-skills.md)
- [Validation](references/validation.md)

Use the templates in `assets/templates/` as prompts for evidence, not forms that must be filled mechanically. Remove empty and irrelevant sections.

## Work in reviewable passes

Draft one file at a time and explain:

1. which repository evidence shaped it
2. which statements came from the user
3. which questions or conflicts remain

Ask the user to review strategic judgment before treating it as durable context. Product personality, anti-references, exceptions, and hard constraints need explicit confirmation.

## Keep the layers connected

The always-loaded file should contain the smallest useful routing rule. For example:

```md
Before writing or changing UI, read PRODUCT.md and DESIGN.md. Reuse documented components and tokens. If the system does not cover a design need, ask before creating a new pattern.
```

Do not copy the full contents of `PRODUCT.md` or `DESIGN.md` into `AGENTS.md` or `CLAUDE.md`. Do not hide universal repository rules inside a task skill.

## Finish with a context audit

Read [validation](references/validation.md), check every generated file against the repository, and summarize:

- files created or updated
- evidence used
- contradictions resolved
- assumptions still awaiting confirmation
- the next real task the user should test with the new context system

