# Storybook + Chromatic: Design Review Before Merge

Already building from your Storybook component library? This resource helps your team inspect visual changes and configure a review checkpoint before merging.

- [Read the checklist and copy the starter prompt](../skills/chromatic-design-review/assets/design-review-checklist.md).
- [Download the complete skill ZIP](https://github.com/thedesignproject/agent-skills/raw/refs/heads/main/downloads/chromatic-design-review.zip).
- [Read the agent instructions](../skills/chromatic-design-review/SKILL.md).

## Install in your coding agent

```bash
npx skills add thedesignproject/agent-skills -s chromatic-design-review
```

Then ask your agent:

```text
Use the chromatic-design-review skill to audit our Storybook and Chromatic
setup. Show us what is needed to require design review before merging.
```

You can also download and extract the ZIP, then give your coding agent the complete `chromatic-design-review` folder. Keep its references, checklist, and metadata together. A chat app without repository or account access can help prepare a plan; an agent with the appropriate access is needed to implement and verify it.

## What it covers

The skill supports a read-only audit, scoped integration changes, and review of a component change. It distinguishes a successful upload from UI Tests and human UI Review, and gives the team a way to verify the required approval on a real PR.

The checklist includes setup questions for engineering, review questions for designers, and the orange-to-blue button example from the video. The resource and skill are free to download; access to external services follows your team's accounts and configuration.

## Maintain the download

After changing the packaged skill:

```bash
python3 scripts/package-skill.py chromatic-design-review
python3 scripts/package-skill.py chromatic-design-review --check
```
