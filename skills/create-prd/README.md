# PRD Generator Skill for Claude Code

A Claude Code skill that generates structured PRDs from feature request transcripts or descriptions, researches your codebase for accurate technical scoping, and optionally creates Linear projects and issues.

## Installation

1. Copy this folder into your repo's `.claude/skills/` directory:

```bash
cp -r create-prd-skill/ your-repo/.claude/skills/create-prd/
```

2. Customize `company-context.md` with your product, architecture, and conventions (see the `[YOUR ...]` placeholders inside).

3. Optionally update `template.md` to match your team's PRD format.

4. Use it:

```
/create-prd path/to/transcript.md
```

or

```
/create-prd We need a feature that lets users do X when Y happens...
```

## What's inside

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition — the instructions Claude follows |
| `template.md` | PRD template with section-by-section guidance |
| `company-context.md` | Your product & architecture reference — **customize this** |

## Customization checklist

- [ ] Fill in `company-context.md` with your product concepts, architecture, tech stack, and conventions
- [ ] Update the example PRD path in `SKILL.md` Step 5 rule 3 (or remove that rule)
- [ ] Adjust the PR size limits in `template.md` Section 12 if your team uses different thresholds
- [ ] If you don't use Linear, remove Step 7 from `SKILL.md` and the Linear tools from `allowed-tools`
- [ ] If you don't use feature flags, simplify the Feature Flag sections in `template.md` and `company-context.md`

## Linear integration (optional)

Step 7 of the skill creates a Linear project and issues from the PRD's implementation plan. This requires the [Linear MCP server](https://github.com/ibraheem4/linear-mcp) to be configured in your Claude Code setup.

To remove Linear integration, delete Step 7 from `SKILL.md` and remove the `mcp__linear-mcp__*` entries from the `allowed-tools` line in the frontmatter.
