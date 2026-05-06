---
name: agentic-design-systems
description: Methodology for building a component library that AI agents can design with accurately and consistently. Use when the user wants to design, structure, or extend a design system intended for AI consumption — encoding components as machine-readable metadata (props, relationships, tokens, anti-patterns) rather than prose docs. Triggers include: "agentic design system", "design system for Claude/AI", "component metadata schema", "make my design system AI-readable", or planning a new UI library where an agent will be the primary consumer.
---

# Building an Agentic Design System

A step-by-step methodology for creating a component library that an AI agent (like Claude) can design with — accurately, consistently, and without inventing patterns.

---

## The core idea

Most design systems are written for humans who can parse prose, infer context, and remember conventions. Agents can't. They need the same decisions encoded as **structured, queryable metadata** living alongside each component.

The goal isn't new documentation. It's the same documentation, translated to a machine-readable format so an agent can answer:

- *Should I use this component?*
- *Which variant?*
- *What goes inside it?*
- *What rules must I obey?*
- *What should I never do?*

---

## The mental model: three pillars per component

Every component is the intersection of three things:

| Pillar | What it answers | Example |
|---|---|---|
| **Props** | What the agent *sets* | `appearance: "primary" \| "secondary"` |
| **Relationships** | What the agent must *understand* before placing the component | `mustBeChildOf: ["Form"]`, `triggers: ["formSubmit"]` |
| **Tokens** | The design values bound to this component | `color-button-primary-bg`, `spacing-button-padding-x-md` |

Most metadata schemas miss **Relationships** and **component-scoped Tokens**. Those are exactly where agents make the most mistakes.

---

## Four design decisions that shape the schema

### 1. States are implicit in tokens
Don't define a separate `states` block. Encode interaction states as token suffixes:
```
button-primary-bg
button-primary-bg-hover
button-primary-bg-pressed
button-primary-bg-disabled
```
Theming becomes a token swap. There is one source of truth.

### 2. Variants are a matrix, not a flat enum
Declare the **axes** (e.g. `appearance × size × density`) and let the agent pick a cell. Add `invalidCombinations` for cells that shouldn't ship.

### 3. Accessibility folds into Relationships
ARIA `role`, `keyboardSupport`, and `screenReader` behavior are relational — they describe how the component fits into the document and the user's interaction model. Keeping them in `relationships` keeps the schema lean.

### 4. Anti-patterns are first-class
Every anti-pattern is a structured triple — never prose:
```ts
{
  scenario: "Two appearance='primary' buttons in the same section",
  reason: "Flattens hierarchy — user can't tell which action is canonical",
  alternative: "One primary, the rest secondary or ghost"
}
```

---

## The schema (four pillars + aiHints)

```ts
interface ComponentMeta {
  component: {
    name: string;
    category: "atoms" | "molecules" | "organisms";
    type: "interactive" | "display" | "container" | "input" | "navigation";
    description: string;
    path: string;
    figma?: { nodeId: string | null };
  };

  props: Record<string, PropDef>;

  variants: {
    axes: Record<string, readonly string[]>;
    purpose: Record<`${string}.${string}`, string>;
    invalidCombinations?: { axes: Record<string, string>; reason: string }[];
  };

  relationships: {
    requires?: string[];
    mustBeChildOf?: string[];
    mustBeParentOf?: string[];
    optionalSibling?: string[];
    commonPartners?: string[];
    triggers?: string[];
    blocksWhen?: { when: string; effect: string }[];
    exposesState?: string[];
    role: string;              // a11y, folded in
    keyboardSupport: string;
    screenReader: string;
  };

  tokens: {
    color?: Record<string, string>;
    spacing?: Record<string, string>;
    typography?: Record<string, string>;
    border?: Record<string, string>;
    motion?: Record<string, string>;
    elevation?: Record<string, string>;
  };

  aiHints: {
    priority: "high" | "medium" | "low";
    keywords: string[];
    selectionCriteria: Record<string, string>;
    usage: {
      useCases: string[];
      commonPatterns: { name: string; composition: string }[];
      antiPatterns: { scenario: string; reason: string; alternative: string }[];
    };
  };
}
```

---

## The 10 steps

### Step 1 — Pick a workspace shape
Recommended: a sibling package inside the consuming app's monorepo (`packages/ui-next/`). Switchover later is just an import rewrite. Avoid a separate repo unless you need independent versioning.

### Step 2 — Define the schema as a TypeScript contract
Write `meta.types.ts` once. Every component's metadata file imports it and is type-checked. The schema *is* the contract.

### Step 3 — Build one component end-to-end as the worked example
Pick something small and high-traffic (Button is canonical). Ship the full set of files together:
```
Button/
  Button.tsx              ← implementation
  Button.meta.ts          ← the four pillars + aiHints
  Button.tokens.css       ← component-scoped tokens
  Button.stories.tsx      ← visual test surface
  Button.test.tsx         ← behavior tests
  index.ts                ← single canonical export
```
Storybook is the harness — wire it up early. Add `.storybook/main.ts` (story discovery) and `.storybook/preview.ts` (theme CSS imports) so stories render. One story per variant matrix cell makes design-space regressions obvious at a glance.

The metadata is not optional and not deferred. It ships with the component or the component doesn't ship.

### Step 4 — Encode tokens at two levels
- `tokens/core.css` — the raw, brand-level palette and scales (`--color-brand-600`, `--space-4`).
- `tokens/themes/*.css` — map component-scoped tokens (`--button-primary-bg`) to the core values.

The component CSS only ever references component-scoped tokens. Theme swaps become mechanical.

### Step 5 — Anti-patterns first
For each component, write the `antiPatterns` block *before* the implementation. It forces precision: you can't write "don't overuse primary buttons" — you have to write the scenario, the reason, and the alternative. This document drives the implementation.

### Step 6 — Use Variant axes to model design language
Variants aren't a flat list of strings. They're a coordinate system. `appearance × size × density` tells the agent how to pick along independent axes — and `invalidCombinations` keeps it from picking a cell that shouldn't exist.

### Step 7 — Encode Relationships as machine-checkable rules
- `requires` — the contexts/providers that must exist above
- `mustBeChildOf` / `mustBeParentOf` — structural constraints
- `triggers` — events emitted
- `blocksWhen` — prop-state-dependent behavior
- `exposesState` — what descendants can read

This is where agents stop building things that compile but are structurally wrong.

### Step 8 — Build a hierarchical metadata index
Add `metadata/index.json`: a flat list of `{name, category, path, keywords, priority}`. The agent scans this first to find candidates, then reads the full `.meta.ts` only for relevant components. Cheap discovery, expensive depth.

Generate it from a script (`scripts/build-index.ts`) that walks every `*.meta.ts`, dynamically imports each one, and writes the JSON. Run it on every metadata change so the index can never lie about what exists.

### Step 9 — Write a metadata validator
A short script (`scripts/validate-metadata.ts`) walks every `*.meta.ts` (via fast-glob), dynamically imports each one, shape-checks the export, and asserts:
- Every variant axis cell appears in `aiHints.selectionCriteria` or `variants.purpose`
- Every `tokens.*` key is component-scoped (kebab-case of the component name)
- `antiPatterns` is non-empty for `priority: "high"` components
- `relationships.role` / `keyboardSupport` / `screenReader` are non-empty (a11y is folded into Relationships, so this enforces the schema decision)
- `invalidCombinations` references only declared axis values

Run it in CI. If the metadata is wrong, the build fails.

### Step 10 — Switchover plan
You don't switch over at the end. You switch over per-component as parity is reached.
- Keep an **API parity tracker** (a markdown checklist of the old library's exports → new equivalents).
- Write a **token bridge** mapping the old library's tokens to the new component-scoped ones.
- Migrate page-by-page with a codemod that rewrites imports.

---

## The principles, restated

- **Lean over generated.** Hand-write metadata for the first ~10 components. Automate only after the patterns are obvious.
- **Direct imports, no barrels.** One canonical path per component. Two ways in means the agent picks wrong.
- **Co-locate everything.** The component, its metadata, its tokens, its stories, its tests — one folder.
- **Anti-patterns drive design.** Write them first. They reveal the contract.
- **Component-scoped tokens.** Never reference raw global tokens from a component's CSS.
- **States live in tokens.** No `states` block. No `behavior.states` array.
- **A11y is relational.** It belongs in Relationships, not its own pillar.
- **The schema is the contract.** If the metadata is wrong, the build fails.

---

## What success looks like

You hand Claude a Figma screenshot or a prose request — *"Build a confirmation modal with a destructive action"* — and it:

1. Scans `metadata/index.json` and shortlists `Modal`, `Button`, `Heading`.
2. Reads each component's `.meta.ts`.
3. Sees `Button.relationships.mustBeChildOf` includes `ModalFooter`, picks `appearance: "danger"` from `aiHints.selectionCriteria`.
4. Avoids two `appearance: "primary"` siblings because of `antiPatterns`.
5. References component-scoped tokens — never invents a color.
6. Generates code that follows the contract on the first try.

That's the bar.
