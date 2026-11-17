# Set up Storybook and Chromatic review

Read this for implementation or troubleshooting. Adapt to the repository; the goal is a working visual-review path with evidence that the intended merge requirement applies.

## Local integration

Confirm the existing Storybook build works using the repository's package manager and workspace conventions. Reuse its build script, framework configuration, tokens, and stories. Include the states affected by the proposed change; an undocumented state cannot be reviewed through an absent snapshot.

Inspect the installed Chromatic package and config before adding anything. Store `CHROMATIC_PROJECT_TOKEN` through the CI secret mechanism. Reference the variable in configuration; do not put its value in source, reports, or prompts. Creating the external project and uploading Storybook require authorized access.

## CI

Follow the [Chromatic CI guide](https://www.chromatic.com/docs/ci/) and the integration for the actual provider. For [GitHub Actions](https://www.chromatic.com/docs/github-actions/):

- Use the existing package manager, lockfile, runtime, workspace path, and compatible action versions. Fetch the Git history required for baseline detection.
- Cover the default branch and the team's feature-branch workflow. Chromatic recommends push events; when preserving a pull-request trigger, verify head-commit and branch identification. Add merge-queue coverage if that repository uses a queue.
- Read the actual exit behavior. The GitHub Action may finish successfully while visual changes await review; verify the separate Chromatic statuses.
- Review automatic-acceptance settings and path/branch filters. Do not use them to hide the demonstration change.

Choose minimal workflow permissions using [GitHub's secure-use guidance](https://docs.github.com/en/actions/reference/security/secure-use). Preserve the repository's trust boundary for forked code; do not expose the project token or run untrusted PR code in a privileged workflow to make a test pass. If fork coverage needs a separate policy, document that remaining decision.

## Project and merge settings

Use the [Storybook quickstart](https://www.chromatic.com/docs/quickstart/) to establish an initial build, and have the team inspect the starting snapshots before relying on them. Confirm builds exist for the intended comparison base and head.

Follow [UI Review](https://www.chromatic.com/docs/review/) to enable the workflow and configure the team's reviewers. Confirm access and feature availability. If unavailable, describe the limitation and a manual review handoff without calling that enforced Chromatic approval.

Follow [mandatory PR checks](https://www.chromatic.com/docs/mandatory-pr-checks/) to require the observed UI Review status on the intended target branch. UI Tests may also be required according to team policy. Inspect existing [GitHub protection rules or rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), enforcement, and bypass permissions. Reuse them without replacing unrelated requirements. A local workflow file cannot prove these external settings are active.

## Verification exercise

After the user authorizes live builds and a demonstration PR:

1. Start from a reviewed baseline. On a temporary branch, change one component shown by a story, such as an orange button to blue. Keep unrelated work out of the exercise.
2. Build/upload and inspect the resulting PR. Match the build to the current commit and confirm the visual change appears in the expected story/state.
3. Verify that the relevant UI Review status is pending and that merge eligibility is blocked by the required review for an actor subject to the rule. Do not attempt a merge as a test.
4. Have the designated reviewer request a fix or approve an intentional change. An unapproved baseline must not be accepted just to finish setup.
5. For a rejected example, revert the visual change and rerun. For an approved change, confirm the review requirements and discussions are complete. Check the latest statuses; approval of an older build is insufficient.
6. Leave or close the demonstration PR according to the user's request. Keep the intentional bad change off the default branch.

If live access is unavailable, run the local checks you can and hand off this exercise. Report setup as locally prepared, with external verification outstanding.
