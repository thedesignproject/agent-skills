---
name: setup-chromatic
description: Set up Chromatic visual testing for existing Storybook components, application screens, or both, including the agent's MCP connection, authenticated project setup, CI, and verification. Use when adding or completing a project's Chromatic integration, or resuming it after login/restart with requests such as continue Chromatic.
---

# Set up Chromatic

Turn the user's project into a working visual-review workflow. Inspect their code, ask what to cover, connect their agent, implement the selected integration, and verify actual cloud results. Explain choices in plain language; run the commands for the user when the environment supports them.

This skill works with Claude Code, Codex, Cursor, and other coding agents. It needs repository access and a way to install dependencies and run tests. A chat-only client can connect the MCP and inspect builds, but cannot complete repository setup without a connected coding environment. Explain that limitation instead of claiming success.

## Put the user's next action first

Apply this to **every user-facing message during the skill**, including coverage choices, progress updates, login/restart handoffs, credential blockers, review requests, and the final report. Write for someone unfamiliar with MCP, CLI tools, and CI.

- If user input/action is needed, begin with a visually distinct **Your next step** block (bold label plus a blockquote or short numbered list). State the immediate action in plain language and exactly where to do it. Put the question/choice there when one is needed, using the host's input tool when appropriate. Never bury the request below a status report.
- Give only the steps the user must perform now, usually one to three. Explain unfamiliar terms briefly where needed. Do not mix future agent work such as project creation, secret provisioning, or uploads into the user's checklist.
- If no user action is needed, lead with **No action needed — I'm continuing** and the useful progress fact; at completion, lead with the actual result and say whether any action remains. Do not manufacture a confirmation request to fit this format.
- After a blank line, separate a short **Status** summary from the action block. Include only the evidence/limitations needed now. Put extensive coverage, changed-file lists, implementation details, and unrelated findings afterward or in a linked local report. A handoff should not open with a long implementation recap.

For an unavoidable restart, lead with the applicable client instructions and the resume phrase, for example:

> **Your next step**
> 1. Restart this agent session, then open `/mcp`, choose **Chromatic**, and sign in through your browser.
> 2. Open this same project and say **continue Chromatic**. A new chat is fine; your progress is saved locally.

**Status:** Local tests pass; cloud verification is waiting for login. Progress is saved in [the handoff file](references/restart-handoff.md). I'll verify login and continue the authorized setup afterward.

This example shows message structure, not a fixed command sequence: use restart only when required, match the actual client, replace the illustrative reference with the real saved handoff's absolute path, and report only results actually verified.

## Resume an interrupted setup

For requests such as **continue Chromatic** (including obvious typos), check the current repository root for `CHROMATIC-HANDOFF.md` before starting discovery again. Read [Restart handoff](references/restart-handoff.md), load the saved progress, recheck the next prerequisite, and continue within the recorded authorization. Do not require the user to paste the previous chat or repeat settled choices.

## 1. Discover the project and choose coverage

Read the repository's instructions, package manager/lockfile, runtime versions, build scripts, app/router structure, existing tests, Git remote/default branch, and CI. Reuse working setup; do not restart or replace it merely to match a template.

Look for authored Storybook configuration, matching stories, and a build script. A dependency, addon package, or generated Playwright archive alone does not establish an existing Storybook. Source-controlled Storybook configuration with only starter examples still counts as an existing workbench, but report that product-component coverage is missing. If configuration exists but is broken, report it as broken rather than absent. Limit repairs to compatible toolchain packages and configuration within the chosen scope. Missing product source, major upgrades, or framework migration need a specific user decision; do not invent a component just to make its story build. In monorepos, identify the relevant apps and Storybooks before choosing coverage.

Restoring dependencies from an existing lockfile for discovery is allowed when running repository tooling is authorized. Wait for the coverage choice before adding/upgrading packages, creating a lockfile, or creating Chromatic projects. If no lockfile exists, use an explicit `packageManager` declaration or ask which manager to use; do not create a competing lockfile.

**Ask the user to choose:**

- When a Storybook workbench exists: **Storybook components only**, **application screens only**, or **both**.
- Otherwise: explain that no Storybook workbench was found and ask **set up screens**, or **stop**. Do not silently scaffold a component Storybook to unlock another option. An explicit request to create one is additional scope.

Say what was found and which apps the choices cover. Respect an explicit choice already made in the conversation. Explain that cloud verification uploads fixture UI and consumes snapshots. Before the first upload, show the bounded inventory and planned verification runs and confirm once, unless the user already authorized that verification. Reuse this authorization for the agreed checks rather than prompting for every routine rerun; ask again only when scope or cost materially grows.

## 2. Connect the user's actual agent

Read [MCP and login](references/mcp-and-login.md). Detect the active client from evidence; ask which one only when unclear. Reuse a healthy existing Chromatic connection. Otherwise install the official plugin when supported, or the account MCP server when it is not. Do not install duplicate connections or change unrelated agent settings.

Try the client-supported current-session plugin reload or MCP reconnect first; do not prescribe a restart merely because configuration changed. Have the user complete their own browser OAuth login, then verify a real authenticated read-only call. Only request a restart when tools remain unavailable and the installed client cannot load them in-session. Continue independent local work while waiting. Do not pretend configuration, loaded tools, and authenticated access are the same thing.

Before stopping for an MCP restart or login handoff, **write `CHROMATIC-HANDOFF.md` in the target repository root**, following [Restart handoff](references/restart-handoff.md). A chat-only note is insufficient for a new conversation. Verify the file exists and is excluded from Git, then tell the user the required client action and: **Afterward, open this same project and say ‘continue Chromatic’.** Do not promise execution while the session is closed. If the file cannot be written, explain that concrete limitation and provide the non-secret handoff text for the user to save.

Use current official docs and the exposed tools, not guessed MCP methods. The **Chromatic account MCP** manages project/build information; a **Storybook MCP** serves component docs and is optional, not a prerequisite for visual testing.

## 3. Match projects and credentials

Use the authenticated MCP and Git remote to find the right existing project/account. Reuse it after checking the linked repository, build type, and recent builds. If several match, ask the user to select; do not unlink or delete existing projects to simplify setup.

For **both**, use separate Chromatic projects: one Storybook project and one Playwright/screen project linked to the same repository. Keep separate config files, project IDs, artifact locations, and CI secrets; pass the right `--config-file` for each command. Supply the selected project ID explicitly to MCP tools when multiple configs would be ambiguous. Verify both lanes independently.

Create missing projects only within the user's authorized setup scope; confirm account/repository when ambiguous. Account creation, paid plans, expanded app permissions, and other host-required approvals remain user actions. Use browser/connector fallback only for operations the MCP cannot perform; explain that specific limitation.

A public project ID belongs in config; OAuth credentials and project tokens do not. MCP OAuth does not provide the CLI upload token. The MCP cannot read an existing project's token, while project creation can return one once. Treat that tool result as sensitive; never repeat its token in chat or logs.

Handle credentials yourself when the user's authorized setup and available access allow it. Follow [credential provisioning](references/mcp-and-login.md#provision-upload-credentials): inspect existing secret sources without displaying values, check CI access, and configure the correctly scoped secret through a structured secret field or stdin. For GitHub, use authenticated `gh` rather than defaulting to instructions for the user. GitHub secret names/metadata can be listed; their saved values cannot be read back. Do not overwrite an existing secret merely because its value is unreadable.

For local uploads, inject an available approved token into the process environment. Use an ignored, access-restricted local env file only when authorized and verified ignored before writing. Never place tokens in command arguments, tracked files, ordinary chat, or resume notes; do not assume a fixed env filename. If access, a retrievable token, or a secure input channel is missing, report that specific blocker and ask for the smallest necessary user action. Continue all independent setup work.

## 4. Implement only the chosen lanes

- **Components:** read [Storybook coverage](references/storybook.md).
- **Screens:** read [Screen coverage](references/screens.md).
- **Both:** read both, keeping their projects and commands separate.

Derive a compact coverage inventory from real routes/components and visible states. Include relevant auth, empty, loading, error, success, overlay, widget, or extension states where they exist. State what remains outside visual coverage. Share the planned count, browsers, viewports, and themes; avoid a Cartesian product of every combination. Add variants when they exercise a distinct layout or the user requests them.

Keep visual fixtures separate from production behavior. Use the repository's package manager, runtime, design system, and relevant checks. Prefer official adapters and supported options before custom archive renderers. Do not copy fixed dependency versions or project-specific internals from another integration.

## 5. Wire CI and review

Read [CI and verification](references/ci-and-verification.md). Add automatic PR/push checks using the existing CI provider and runner conventions. Preserve existing workflows and secrets. Keep review manual by default and finish the runner while the native approval check remains pending; do not poll for a human approval inside CI.

Reuse the user's existing authorization, including across login or restart. An explicitly authorized end-to-end setup with CI secrets and a draft PR should proceed through those steps without repeated permission requests. Available credentials alone are not authorization: honor local-only, no-push, or other explicit limits. If pushing/opening a PR, setting CI secrets, or changing branch rules falls outside the authorized scope, first finish and validate the independent local implementation, then present the concrete remaining action for authorization. Before any authorized push, state what will be pushed and which CI workflows its **complete diff** will trigger. Do not merge setup or demonstration changes as part of installing Chromatic.

## 6. Prove the workflow

Verify repository checks, the selected snapshot inventory, cloud capture, native statuses, and PR reporting for the exact tested SHA. Check unchanged repeat behavior and the same-commit rerun/report path. For screens, verify source-to-archive fidelity and important semantic content; a source image and replay can both be equally wrong.

Do not accept baselines just to make setup green. Initial snapshots may need review, or the service may seed a first baseline automatically; report what actually happened and have the user inspect it. With an accepted baseline, unchanged UI should introduce no new differences. Investigate unexplained differences rather than increasing thresholds or hiding elements.

When authorized, use a tiny, reversible visual change on a separate draft branch to demonstrate the gate. Select an isolated surface, check the complete diff against CI path filters/selectors, and confirm the native review check remains pending while runner jobs finish. Do not approve or merge the demonstration without the user's instruction.

Finish with: scope and coverage count; project/config mapping; local and cloud evidence with build/SHA links; actual CI/comment behavior; exact required-check status; runtime/snapshot cost observations; and any remaining user action. Distinguish **configured locally**, **uploaded and tested**, and **live PR gate verified**. Never call the whole setup complete while a login, missing token, unpublished workflow, or unverified gate is still required for the agreed scope.
