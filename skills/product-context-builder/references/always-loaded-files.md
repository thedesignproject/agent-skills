# Always-loaded files

Use `AGENTS.md` and `CLAUDE.md` for stable instructions that are useful at the beginning of many sessions.

## Include

- one-sentence project definition
- verified architecture and important paths
- package manager and exact build, test, lint, and type-check commands
- conventions that are easy to violate
- hard constraints and actions that require approval
- short routing instructions for `PRODUCT.md`, `DESIGN.md`, and project skills

## Exclude

- task-specific checklists
- long explanations already documented elsewhere
- aspirational rules the repository does not follow
- generic engineering advice
- duplicated product and design-system documentation

Prefer one shared source for common guidance. If both files exist, keep tool-specific instructions local and review shared rules for drift.

