# CI, approval gates, and evidence

Read the existing CI and use its package manager/runtime/runner. Add the selected lanes without replacing unrelated jobs. Keep each lane's token/config/archive/report distinct. Reuse a working runner provider; changing providers or buying capacity is a separate choice unless already authorized. Record setup, local tests, upload, and cloud capture times separately before suggesting performance changes.

## PR execution and one useful result

- Run automatically on relevant PR creation and new commits, including drafts when the user expects preview review. Use the PR head SHA and branch identity; fetch the Git history the CLI needs.
- Check path filters/selectors using the entire proposed PR diff against its exact base, including root configs, scripts, dependencies, and untracked files before commit. In a dependent PR, use the immediately lower branch. Never promise an unrelated audit will skip based only on a unit test for one ignored path. Do not blanket-ignore lockfiles or weaken other quality gates.
- Use least-privilege capture jobs. Don't expose upload secrets to untrusted fork code, and don't use `pull_request_target` to run it with elevated credentials. If uploads are skipped, explain the path for a maintainer to run a trusted branch and how required statuses behave.
- Prefer the native Chromatic comment if the integration provides the desired result. Otherwise update one bot-owned comment per PR, with project/build URL, tested SHA, executed count, errors/skips, pending reviews, and logs. In both mode, show both lanes and their own states. Skip stale heads. Keep permission to post separate from executing PR code where the provider permits it. Don't trust arbitrary report URLs or counts as success.
- A custom comment is a workflow-run snapshot unless an explicitly implemented webhook updates it after review. The native status is the authoritative live approval state.

## Yellow approval without a waiting runner

Leave auto-accept disabled unless the user explicitly requests a different policy. Prefer a linked repository and enabled native visual tests so Chromatic reports its own approval status. CLI `--exit-zero-on-changes` can let the runner finish on reviewable visual changes while preserving failures for real errors; it does not itself block merging.

When using this arrangement, do not exit immediately after upload if CI needs completed cloud results. Validate that capture/render/upload/report failures remain failures. A successful shell exit alone is not proof that every expected snapshot was captured.

A native pending check blocks merges only when the Git provider requires it. After the exact project checks have appeared, add the authorized required contexts while preserving existing protection settings, bypasses, and unrelated checks. Require local capture/upload/result jobs as appropriate too. Verify the actual required-check list and merge status, not just a comment saying "needs review."

For multiple projects, discover each actual check context; don't assume a shared generic name. Don't require a context disabled in Chromatic or skipped for that PR scenario. Roll requirements out only where the workflow can report them. Do not block parent stack branches or automatic stack maintenance by adding checks they cannot emit. Report pending rollout explicitly if changing rules is not authorized or not yet safe.

## Same-commit rebuilds and missing reports

A manual build can pass a SHA before CI runs it. The CLI may skip that passed same-commit rebuild and write no fresh JUnit report. If CI depends on a fresh report/native status, use the supported `--force-rebuild` option for that lane and explain its same-commit snapshot cost. Alternatively, explicitly verify a reused completed build for the exact project, SHA, config, and inventory through the authenticated MCP before reporting reuse. Never invent counts or treat a missing report as proof of success. During platform-parity verification, capture on the actual CI runner rather than reusing a differently sourced manual build.

Keep a missing, malformed, partial, skipped, or rendering-error report from being mislabeled "passed" or "awaiting approval." With a valid complete report, visual changes awaiting review are a separate state from infrastructure/test failure.

## Verify once, then a small controlled proof

1. Run relevant repository checks. For screen fixtures, reconcile inventory, source captures, archive replays, and cloud snapshots. Check semantic content so a missing element is not "verified" by two matching broken images.
2. Upload and inspect build results through the MCP/UI for the exact SHA and each selected project. An API project connection is not evidence that the CLI uploaded or tested anything.
3. Inspect first baselines. If they await approval, leave that human action pending; if the service automatically seeded them, report that. Do not accept unexplained changes. After a baseline has been accepted, run an unchanged control and expect no new differences.
4. Exercise a same-commit rerun and confirm the report and native statuses still exist. Reuse the control run for this proof where possible; don't duplicate builds unnecessarily. Stop and diagnose recurring failures before consuming more snapshots with identical retries.
5. If publication was requested, verify the actual PR job, comment, and native status in CI. If a visual demonstration was authorized, make a small intended change on a separate draft branch, verify only the expected snapshots differ, and verify required native checks stay pending while CI finishes. Do not merge or approve it automatically.

A setup can be locally valid while cloud/login/publication remains incomplete. Report the tested scope and remaining step precisely; don't turn a partial integration into an "all set" claim.

Official references:
- [GitHub Actions integration](https://www.chromatic.com/docs/github-actions/)
- [Mandatory PR checks](https://www.chromatic.com/docs/mandatory-pr-checks/)
- [Configuration reference](https://www.chromatic.com/docs/configure/)
- [MCP capabilities and limitations](https://www.chromatic.com/docs/mcp/)
