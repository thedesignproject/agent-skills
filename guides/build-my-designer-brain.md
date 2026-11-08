# Using Build My Designer Brain

The [skill](../skills/build-my-designer-brain/SKILL.md) contains a guided interview and an update workflow. Your answers become a separate folder of Markdown files. It does not require a company project, screenshots, or a reference integration.

## Download and upload No terminal needed

[**Download Build My Designer Brain ZIP**](https://github.com/thedesignproject/agent-skills/raw/refs/heads/main/downloads/build-my-designer-brain.zip)

This download contains just this skill, including its interview and supporting references. You do not need to download the entire repository or assemble the files yourself.

For Claude:

1. Download the ZIP and keep it zipped. If your browser unzips it automatically, use the original downloaded ZIP or compress the `build-my-designer-brain` folder again.
2. Enable **Code execution and file creation** (called **Create and edit files** in some layouts) in Settings → Capabilities. Team settings may be managed by your organization.
3. Open **Customize → Skills**, select **+ → Create skill → Upload a skill**, and upload the ZIP.
4. Enable the skill and start a conversation with:

   > Use Build My Designer Brain to help me build my personal designer brain.

These steps follow [Claude’s custom skill instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude). For coding agents, unzip the download and use the installation table below. For ChatGPT, follow its supported skill workflow; this download is not a published ChatGPT plugin.

## Start with the installer Optional

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
| Claude chat | Download the ready-made ZIP above, keep it zipped, and upload it through Customize → Skills. Enable the required file-creation capabilities. |
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

## Updating your installed skill

When a new version is available, download the ZIP again and use your app’s supported update or replacement workflow. For local coding agents, replace the installed skill folder with the new folder. Your generated personal brain is stored separately; keep those personal files when updating the skill.

If you installed with the repository’s NPX installer, use its update command instead:

```bash
npx skills update
```

## Maintaining the downloadable package

After editing the skill, rebuild and verify its ZIP before committing:

```bash
python3 scripts/package-skill.py build-my-designer-brain
python3 scripts/package-skill.py build-my-designer-brain --check
```

Commit the source changes and `downloads/build-my-designer-brain.zip` together. The package includes one top-level skill folder with `SKILL.md`, its metadata, and all reference files.
