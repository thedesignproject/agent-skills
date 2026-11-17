---
name: chromatic-design-review
description: Set up or audit Storybook and Chromatic checks and review component changes against approved designs. Use when configuring Chromatic, requiring its UI Review before merging, troubleshooting visual PR checks, or reviewing AI-assisted UI changes with Storybook and Chromatic.
---

# Chromatic Design Review

Keep new front-end work aligned with the team's existing component decisions by making visual changes visible and reviewable before merging.

Chromatic detects visual differences in the stories it captures. People decide whether those differences are appropriate. Snapshot coverage does not establish product-wide consistency, functional correctness, or accessibility.

## Choose the task

- **Audit or explain:** inspect the current setup and give an evidence-based plan. Keep the repository and external settings unchanged.
- **Set up or fix:** inspect first, then make the local integration changes within the requested scope. Use [setup.md](references/setup.md) for CI, baselines, and merge requirements. Reuse existing integration choices where they work.
- **Review a change:** compare the changed implementation and snapshots with documented component decisions, following the review guidance below.
- **Share with the team:** provide or copy the [checklist and starter prompt](assets/design-review-checklist.md). Keep its unverified items unchecked.

## Establish the starting point

Read project instructions and find the relevant package, package manager, Storybook configuration, build command, stories, Chromatic configuration, and CI workflows. In a monorepo, identify which app and Chromatic project are in scope.

Look for component usage rules, design tokens, and the intended base branch. Record what is verified locally and what requires Chromatic or Git-provider access. If Storybook is missing, explain the prerequisite and propose a small first-component setup; do not silently build a whole library or substitute another tool.

Check current official documentation before editing version-dependent integration code. Use repository-compatible runtime and action versions. The setup reference links to the relevant primary sources.

## Preserve the review requirement

Distinguish three signals: the CI job that builds/uploads Storybook, Chromatic's **UI Tests** status, and its **UI Review** status. A successful upload job alone does not establish human approval.

For a required design-review workflow, verify that UI Review is enabled, the responsible reviewers are configured, and the appropriate required status check actually applies to the target branch. Discover the status names and source from a real PR rather than guessing them. Check enforcement and applicable bypasses before claiming a merge is blocked.

Setup work may require project creation, snapshot uploads, reviewer assignment, or repository-rule changes. Perform those external actions only within the user's authorization. Carry forward authorization already given. If access is missing, complete the local work and identify the exact owner action that remains; do not claim it is configured.

Do not introduce automatic baseline acceptance, skipped checks, broad snapshot exclusions, or weakened merge rules merely to get a green result. Preserve deliberate existing exceptions and explain how they affect coverage.

## Review a change

1. Match the PR/head commit, Storybook build, intended base, and comparison snapshots. A stale build cannot verify the current change.
2. Inspect before/after views and the diff alongside the changed component, token, story, and usage rules. Identify intentional changes, apparent regressions, and decisions that need context.
3. Give concrete feedback: the affected story/state, what changed, the relevant documented decision, and the requested fix or question. Separate documented violations from personal preferences.
4. Leave approval, baseline acceptance, discussion resolution, and merging to the authorized reviewer unless the user specifically asks you to perform that action. If visual evidence is inaccessible, label the review as code-only or incomplete.

## Verify and hand off

For setup, follow the verification exercise in [setup.md](references/setup.md). Report the scoped app, coverage, check names, evidence links, and whether merge enforcement was verified. Keep local validation separate from live-service verification.

End with what is ready, what remains unverified, and who can complete it. Never describe an agent's recommendation as human sign-off.
