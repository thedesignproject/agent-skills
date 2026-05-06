---
name: agentic-design-systems
description: Use when designing, scaffolding, extending, or auditing a component library whose primary consumer is an AI agent — i.e. the design system needs machine-readable metadata (props, variants, relationships, tokens, anti-patterns) rather than only prose docs. Triggers include "agentic design system", "design system for AI/Claude", "make my design system AI-readable", "component metadata schema", "scaffold a UI library for an agent", or planning a new component library where the main consumer is an LLM. Don't use this skill for purely human-facing design system work — use figma:figma-generate-library for that.
---

# Agentic Design Systems

When this skill triggers, you're helping the user build, extend, or audit a component library whose primary consumer is an AI agent. The bar: given a prose request like *"Build a confirmation modal with a destructive action,"* an agent picks the right component, the right variant, and the right tokens — without inventing patterns.

This skill gives you the schema, the workflow, and the principles. Adapt it to where the user is.

---

## Diagnose first

Before producing anything, figure out which mode applies:

- **Greenfield** — user is starting a new system intended for agent consumption. Walk through the [build workflow](#build-workflow). Start with the schema and one worked component (Button is canonical); don't try to scaffold everything at once.
- **Retrofitting** — user has a component library and wants to make it agent-readable. Skip workspace setup. Add `meta.types.ts`, then write a `.meta.ts` per component, then build the index and validator. Anti-patterns first (see [Step 5](#step-5--anti-patterns-first)).
- **Auditing** — user has metadata already. Score each component against the [four pillars](#the-four-pillars) and the [validator checks](#step-9--metadata-validator). Flag missing relationships, prose anti-patterns, raw global tokens, and ungrounded variant axes.
- **Single component** — user wants to add or fix one component. Generate the full file set in [Step 3](#step-3--build-one-component-end-to-end). Metadata ships with the component or it doesn't ship.

If the prompt is ambiguous, ask one targeted question — don't guess.

---

## The four pillars

Treat every component as the intersection of four things. Most metadata schemas only model the first; that's why agents misuse the components.

| Pillar | What it answers | Failure mode if missing |
|---|---|---|
| **Props** | What you set | (always present) |
| **Variants** | Which combination to pick | Agent picks invalid combinations |
| **Relationships** | Where the component fits structurally and a11y-wise | Agent generates code that compiles but is structurally wrong |
| **Tokens** (component-scoped) | Which design values bind to this component | Agent invents colors and spacing |

Plus `aiHints` — the meta layer that tells an agent *when* to use the component, *which* variant fits *which* situation, and *what never to do*.

### Four design decisions baked into the schema

- **States are implicit in tokens, not a separate pillar.** Encode `button-primary-bg-hover`, `button-primary-bg-disabled`, etc. Theming becomes a token swap; one source of truth.
- **Variants are a matrix, not a flat enum.** Declare axes (`appearance × size × density`) and let the agent pick a cell. Use `invalidCombinations` for cells that shouldn't ship.
- **Accessibility folds into Relationships.** ARIA `role`, `keyboardSupport`, and `screenReader` describe how the component fits into the document and interaction model — that's relational. No separate a11y pillar.
- **Anti-patterns are first-class and structured.** Never prose. Always `{scenario, reason, alternative}` triples — they force precision.

---

## The schema (canonical contract)

Write this once at `meta.types.ts`. Every component's `.meta.ts` imports it and is type-checked. The schema *is* the contract.

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
    requires?: string[];           // contexts/providers above
    mustBeChildOf?: string[];
    mustBeParentOf?: string[];
    optionalSibling?: string[];
    commonPartners?: string[];
    triggers?: string[];           // events emitted
    blocksWhen?: { when: string; effect: string }[];
    exposesState?: string[];       // state descendants can read
    role: string;                  // a11y
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

When generating a component's `.meta.ts`, fill every field that applies. Empty arrays are fine; missing keys aren't — that's what the validator catches.

---

## Build workflow

### Step 1 — Workspace shape
Recommend a sibling package inside the consuming app's monorepo (`packages/ui-next/`). Switchover later is just an import rewrite. A separate repo only makes sense when independent versioning is required.

### Step 2 — Schema as TypeScript contract
Write `meta.types.ts` before any components. Everything else flows from it.

### Step 3 — Build one component end-to-end
Pick something small and high-traffic. Button is canonical. Ship the full set together:

```
Button/
  Button.tsx              ← implementation
  Button.meta.ts          ← four pillars + aiHints
  Button.tokens.css       ← component-scoped tokens
  Button.stories.tsx      ← visual test surface
  Button.test.tsx         ← behavior tests
  index.ts                ← single canonical export
```

Wire up Storybook early (`.storybook/main.ts` for story discovery, `.storybook/preview.ts` for theme imports). One story per variant matrix cell makes design-space regressions obvious at a glance.

Metadata ships with the component or the component doesn't ship. Don't defer it.

### Step 4 — Tokens at two levels
- `tokens/core.css` — raw brand palette and scales (`--color-brand-600`, `--space-4`).
- `tokens/themes/*.css` — map component-scoped tokens (`--button-primary-bg`) to core values.

Component CSS only ever references component-scoped tokens. Theme swaps stay mechanical.

### Step 5 — Anti-patterns first
For each component, write the `antiPatterns` array *before* writing the implementation. The structured-triple format (`scenario`, `reason`, `alternative`) forces precision — you can't write "don't overuse primary buttons"; you have to write *which scenario*, *why it's wrong*, *what to do instead*. The anti-patterns end up driving the API.

### Step 6 — Variant axes as a coordinate system
Variants aren't a flat list of strings. Declare axes (`appearance × size × density`) so the agent picks along independent dimensions. Use `invalidCombinations` to rule out cells that shouldn't ship (e.g. `appearance: "ghost" × size: "xs"` — too small to be tappable).

### Step 7 — Relationships as machine-checkable rules
- `requires` — providers that must exist above
- `mustBeChildOf` / `mustBeParentOf` — structural constraints
- `triggers` — events emitted
- `blocksWhen` — prop-state-dependent behavior
- `exposesState` — what descendants can read

This is the pillar that prevents agents from generating code that compiles but is structurally wrong.

### Step 8 — Hierarchical metadata index
Generate `metadata/index.json` — a flat list of `{name, category, path, keywords, priority}`. Agents scan this first to shortlist candidates, then read the full `.meta.ts` only for relevant components. Cheap discovery, expensive depth.

Build with a script (`scripts/build-index.ts`) that walks every `*.meta.ts`, dynamically imports each one, and writes the JSON. Run it on every metadata change so the index can never lie about what exists.

### Step 9 — Metadata validator
A short script (`scripts/validate-metadata.ts`) walks every `*.meta.ts` (via fast-glob), dynamically imports each one, shape-checks the export, and asserts:

- Every variant axis cell appears in `aiHints.selectionCriteria` or `variants.purpose`
- Every `tokens.*` key is component-scoped (kebab-case of the component name)
- `antiPatterns` is non-empty for `priority: "high"` components
- `relationships.role` / `keyboardSupport` / `screenReader` are non-empty (enforces the "a11y folds into Relationships" decision)
- `invalidCombinations` references only declared axis values

Run in CI. If the metadata is wrong, the build fails. The schema is enforced, not aspirational.

### Step 10 — Switchover (per-component, not big-bang)
Don't switch over at the end — switch per-component as parity is reached.

- **API parity tracker** — markdown checklist of old library exports → new equivalents.
- **Token bridge** — map old tokens to new component-scoped ones.
- **Codemod** — rewrite imports page-by-page.

---

## Principles

- **Lean over generated.** Hand-write metadata for the first ~10 components. Automate only after the patterns are obvious.
- **Direct imports, no barrels.** One canonical path per component. Two ways in means the agent picks wrong.
- **Co-locate everything.** Component, metadata, tokens, stories, tests — one folder.
- **Anti-patterns drive design.** Write them first. They reveal the contract.
- **Component-scoped tokens.** Never reference raw global tokens from a component's CSS.
- **States live in tokens.** No `states` block. No `behavior.states` array.
- **A11y is relational.** It belongs in Relationships, not its own pillar.
- **The schema is the contract.** Validator runs in CI; failing metadata fails the build.

---

## What success looks like

The user hands an agent a Figma screenshot or a prose request — *"Build a confirmation modal with a destructive action"* — and the agent:

1. Scans `metadata/index.json` and shortlists `Modal`, `Button`, `Heading`.
2. Reads each shortlisted component's `.meta.ts`.
3. Sees `Button.relationships.mustBeChildOf` includes `ModalFooter`; picks `appearance: "danger"` from `aiHints.selectionCriteria`.
4. Avoids two `appearance: "primary"` siblings because `antiPatterns` flags it.
5. References component-scoped tokens — never invents a color.
6. Generates code that follows the contract on the first try.

That's the bar. If the metadata can't get an agent to that outcome, fix the metadata.
