# Context system validation

- Every command runs or is clearly marked unverified.
- Every path and named component exists.
- `AGENTS.md` and `CLAUDE.md` agree on shared constraints.
- Product claims came from an owner or existing source.
- Design tokens reflect the repository and link to their source of truth.
- The always-loaded files route to deeper context instead of duplicating it.
- Skill descriptions are specific enough to trigger for the intended work.
- No file contains secrets, temporary task details, or instructions copied from untrusted content.
- Empty template sections have been removed.

Test with one real task. Review whether the agent opened the right files, reused an existing component, followed product principles, and asked before inventing an uncovered pattern.

