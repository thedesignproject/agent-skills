# Your Storybook Is Set Up. Now What?

A Storybook + Chromatic design review checklist from The Design Project.

Use this with your designer and engineer to make UI changes visible before they merge. Chromatic highlights visual differences in captured stories; your team decides whether a change follows the product's design decisions.

## Work through setup with engineering

- [ ] Identify the app, Storybook, Chromatic project, and branch receiving changes.
- [ ] Confirm Storybook builds and includes the component states your team wants to review.
- [ ] Run an initial Chromatic build and review the starting snapshots together.
- [ ] Connect the project to your Git provider and run builds through CI for the relevant branches.
- [ ] Keep the project token in the CI secret mechanism.
- [ ] Enable UI Review and agree who reviews changes, including reviewer access.
- [ ] Observe the UI Tests and UI Review statuses on a real pull request. A green upload job alone is insufficient.
- [ ] Make the appropriate UI Review status required on the target branch, and check that the rule is active for the people contributing.
- [ ] Try a small intentional visual change and confirm it appears for review and cannot merge through the normal workflow while required approval is outstanding.

Record any missing access or settings as unfinished work. The checklist is complete when you have verified the behavior, rather than only added a workflow file.

## Review a visual change

- [ ] Am I looking at the current PR commit and the intended comparison version?
- [ ] Which components, states, and layouts changed?
- [ ] Was this intentional, and which documented component or token decision applies?
- [ ] Does the change need a fix, or should the team update the agreed standard?
- [ ] Have I left specific feedback on the affected snapshot and checked the latest result after a fix?

Inspect color, spacing, typography, and layout where relevant. Functional behavior and accessibility still need their own appropriate checks. Parts of the product outside the captured stories remain outside this visual comparison.

## Try the orange-to-blue example

Your approved button is orange. Someone makes it blue in Paper and asks an agent to implement the change. The new build highlights the difference in Chromatic.

The reviewer checks the component rules and comments: “The record button should use our existing orange token. Please restore it and rerun the checks.” With UI Review required and enforcement verified, the normal merge path waits for the review requirements to pass.

An intentional redesign can be approved after discussion. Updating the baseline is a design decision; a passing code check alone does not make that decision.

## Copy this prompt into your coding agent

```text
Use the chromatic-design-review skill to inspect this repository's Storybook,
Chromatic configuration, and PR workflow. Start with a read-only audit.
Tell me what is already configured, what is missing, and what needs engineering
or account access. Separate the upload job, UI Tests, and UI Review statuses.
Propose the smallest setup that lets our designated reviewer inspect visual
changes before merging. Include a test using one intentional component change.
Keep unverified items clearly marked, and show me the plan before changing files
or external settings. Never include token values in your response.
```

Without an installed skill, give the agent the complete skill folder first. If it cannot inspect the repository or settings, use its response as a plan for the team to verify.

## Official setup references

[Chromatic for Storybook](https://www.chromatic.com/docs/quickstart/) · [CI integration](https://www.chromatic.com/docs/ci/) · [UI Review](https://www.chromatic.com/docs/review/) · [Required PR checks](https://www.chromatic.com/docs/mandatory-pr-checks/)
