# Using Build My Designer Brain

The [skill](../skills/build-my-designer-brain/SKILL.md) contains a guided interview and an update workflow. Your answers become a separate folder of Markdown files. It does not require a company project, screenshots, or a reference integration.

## Start

Install this skill with the repository’s existing installer:

```bash
npx skills add thedesignproject/agent-skills -s build-my-designer-brain
```

Add `-g` for a personal installation across projects.

In Codex, invoke:

```text
Use $build-my-designer-brain to help me build my personal designer brain.
```

In another host, invoke the installed skill by its name using that host's supported interface. For an agent that can read files directly, you can also point it to `build-my-designer-brain/SKILL.md` and ask it to follow the linked interview.

The interview covers critique methods, working with AI, optional references and taste, then lessons and update preferences. It asks two questions per round, accepts write-ins, and supports ordered text ranking with custom priorities and ties. You can skip or resume.

## Install the shared skill

Keep the complete `build-my-designer-brain/` folder together, including references and metadata.

| Host | Installation route |
| --- | --- |
| Codex | Copy the folder into `~/.codex/skills/` or another supported skill location. Start a new session if needed. |
| Claude Code | Copy the folder into `~/.claude/skills/` for personal use. |
| Claude chat | ZIP the skill folder and upload it through Customize → Skills, where available. Enable the required file-creation capabilities. |
| Cursor | Copy the folder into `~/.agents/skills/` or `.cursor/skills/` for a project. |
| Gemini CLI | Follow its documented Agent Skills installation flow with the same folder. |
| ChatGPT | Use the available skill-creation/import workflow in the desktop app. Native distribution across web/mobile uses plugin packaging; this release is the core skill folder and ZIP, not a published plugin. |

Official instructions: [OpenAI](https://learn.chatgpt.com/docs/build-skills), [Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude), [Claude Code](https://code.claude.com/docs/en/skills), [Cursor](https://cursor.com/docs/skills), [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/). Features and organization controls vary. These are documented installation routes, not a claim of testing in every application.

For an assistant without native skill loading, provide the skill and its referenced files as readable context and ask it to follow the interview. This is a manual fallback, not a native install. Without file access, it can return Markdown or downloadable files; you must save or reattach those files for later work.

## Bring the finished brain to work

Give the active agent access to your brain folder alongside the product workspace, then say:

```text
Read my personal brain's README, working-with-me, and critique-methods files.
Use the relevant guidance for this feature alongside the current company rules.
Follow my selected evolution policy and tell me if you cannot read or save a file.
```

Access alone does not automatically load the files. A skill is not a background watcher or a repository-sync service. Company decisions stay in company context, feature exceptions stay local, and optional personal taste does not silently override product requirements.

## Validation scope

The core package is checked with the skill validator and exercised using agent-based interview and file-writing scenarios. Native installation and UI behavior in Claude, ChatGPT, Cursor, and Gemini require host-specific verification before advertising them as tested. No marketplace publication or external account configuration is included.
