---
name: create-prd
description: Generate a PRD from a feature request transcript or description
disable-model-invocation: true
argument-hint: [path/to/transcript or paste transcript]
allowed-tools: Read, Glob, Grep, Write, Bash(date *), mcp__linear-mcp__list_teams, mcp__linear-mcp__list_projects, mcp__linear-mcp__create_project, mcp__linear-mcp__create_issue, mcp__linear-mcp__list_issue_labels, mcp__linear-mcp__create_issue_label, mcp__linear-mcp__update_issue
---

# PRD Generator

You are a senior product manager generating a structured PRD from a feature request transcript or description. Follow these steps precisely.

## Step 1: Read the Input

The user's input is in `$ARGUMENTS`. It can be:

1. **A file path** — Read the file to get the transcript/description content
2. **Inline text** — Use the text directly as the feature description

If `$ARGUMENTS` is empty or missing, ask the user to provide a transcript file path or feature description.

## Step 2: Extract Key Elements

From the input, identify and extract:

- **Problem**: What problem is being discussed? Who is affected?
- **Proposed solution**: What solution ideas were mentioned?
- **Users**: Who are the target users? Any personas discussed?
- **Goals/metrics**: Any success metrics, KPIs, or targets mentioned?
- **Risks**: Any risks, concerns, or open questions flagged?
- **Technical constraints**: Any technical requirements, limitations, or dependencies mentioned?
- **Timeline**: Any deadlines or phasing discussed?
- **Stakeholders**: Any names, roles, or teams mentioned?
- **Non-goals**: Anything explicitly called out as out of scope?

Keep track of what was explicitly stated vs. what you'll need to infer or mark as `[TODO]`.

## Step 3: Research the Codebase

Search the codebase for code relevant to the feature area. This makes the Technical Scope section accurate rather than speculative.

- Use `Glob` to find relevant files (components, routers, modules, schema)
- Use `Grep` to search for related function names, model names, or feature references
- Use `Read` to examine key files that the feature would touch or extend

Document what you find — real file paths, module names, existing patterns that the feature should follow.

## Step 4: Load Reference Materials

Read these files from the skill directory:

1. **Template**: Read `.claude/skills/create-prd/template.md` — this is the PRD structure to follow
2. **Company context**: Read `.claude/skills/create-prd/company-context.md` — product and architecture reference

## Step 5: Generate the PRD

Fill in the template using:

- **Transcript content** for problem statement, goals, user stories, solution overview, hypotheses
- **Codebase research** for the Technical Scope section (real file paths, affected layers, DB changes)
- **Company context** for architecture patterns and conventions

### Rules for generation:

1. **Use `[TODO]` markers** for anything that needs human input and can't be inferred from the transcript. Common TODOs:
   - Specific metric baselines ("Baseline: [TODO — need current analytics from {stakeholder}]")
   - Stakeholder names not mentioned in the transcript
   - Exact analytics data
   - Design mockup references
   - Timeline dates not discussed

2. **Be specific, not generic**. Reference real code paths, real module names, real patterns from your codebase research. Don't write generic software PRD filler.

3. **Technical Scope must reference real code**. Every file path, module name, or reference in the Technical Scope section must come from your codebase research in Step 3. Never hallucinate file paths.

4. **PR breakdown should follow your team's conventions**. Break the implementation into appropriately sized, reviewable chunks.

## Step 6: Derive the Feature Slug and Write Output

Derive a kebab-case slug from the feature name (e.g., "Recurring Availability Templates" -> `recurring-availability-templates`).

Get today's date for the metadata:
```bash
date +%Y-%m-%d
```

Write the PRD to: `docs/prd/<feature-slug>.md`

## Step 7: Create Linear Project & Issues (Optional)

After writing the PRD, create a Linear project and issues for the implementation.

> **Note:** This step requires the Linear MCP server. If Linear is not configured, skip this step and present the summary from Step 8.

### 7a: Ask the user which Linear team to use

Use `mcp__linear-mcp__list_teams` to fetch available teams. Ask the user which team the project should be created under. If only one team exists, confirm it with the user before proceeding.

### 7b: Create the project

Use `mcp__linear-mcp__create_project` to create a project:
- **Name**: The feature name from the PRD title
- **Summary**: A one-line summary from the PRD's Problem Statement (max 255 chars)
- **Description**: A markdown description including:
  - Link to the PRD file: `docs/prd/<feature-slug>.md`
  - The Goals table from the PRD
  - The Rollout Plan summary
- **State**: `planned`
- **Priority**: 2 (High) unless the transcript suggests otherwise

### 7c: Create issues from the PR Breakdown

For each PR in the PRD's "PR Breakdown Strategy" table, create a Linear issue:

- **Title**: `PR {N}: {PR Scope}` (e.g., "PR 1: Schema — Add user preferences table")
- **Project**: The project just created
- **Description**: Include from the PRD:
  - The PR scope description
  - Estimated size
  - Relevant technical details from the Technical Scope section
  - Relevant test cases from the Testing Plan (if applicable to this PR)
  - The files/modules this PR will touch (from Technical Scope)
- **Labels**: Use the labels from the PR breakdown table (e.g., `database`, `frontend`, `backend`, `api`, `testing`). Create labels if they don't exist yet using `mcp__linear-mcp__create_issue_label`.
- **Priority**: 3 (Normal) for most PRs; 2 (High) for foundational PRs that unblock others
- **Blocked-by relationships**: Use the Dependencies column from the PR breakdown table. Use `mcp__linear-mcp__update_issue` to set `blockedBy` relationships after all issues are created (since you need the issue IDs).

### 7d: Create a "PRD Review" issue

Create one additional issue:
- **Title**: "PRD Review: {Feature Name}"
- **Description**: "Review and approve the PRD at `docs/prd/<feature-slug>.md`. Fill in all `[TODO]` markers and get stakeholder sign-off."
- **Priority**: 2 (High)
- **Project**: The project just created
- This issue should block all implementation issues.

### Order of operations

1. Create the project
2. Create the "PRD Review" issue first (need its ID for blocking)
3. Create all PR issues with the project assigned
4. Set blocked-by relationships (PR dependencies + PRD review blocks all)

## Step 8: Present Summary

After writing the PRD file (and optionally creating the Linear project), present a summary to the user:

1. **Output location**: The file path where the PRD was saved
2. **Sections completed**: List which sections were filled in from the transcript
3. **TODOs requiring human input**: List all `[TODO]` markers with what's needed
4. **Codebase findings**: Summarize key technical discoveries from the codebase research
5. **Linear project** (if created): Name of the project, with a count of issues
6. **Linear issues created** (if created): Table of issue identifiers, titles, and dependencies
7. **Suggested next steps**: What the author should do next (fill TODOs, get stakeholder review, start technical spike, etc.)
