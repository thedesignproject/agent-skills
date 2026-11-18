# Existing Storybook components

Use the repository's real Storybook build and framework integration. Inspect its stories, decorators, providers, themes, loaders, mocks, assets, fonts, and existing visual-test exclusions. Report a broken or example-only Storybook instead of claiming the product library is already covered.

1. Inventory authored components/stories and useful states. Preserve intentionally excluded stories and ask about consequential gaps. Add missing representative stories in the existing format when they belong to the agreed coverage; do not auto-generate a story for every internal file.
2. Build the current Storybook locally before introducing Chromatic, so pre-existing failures are separated from integration failures.
3. Add a compatible `chromatic` development dependency with the current package manager, public project ID config, and explicit local/CI command. Preserve the existing build script and Storybook configuration. Use `--config-file` in a multi-project repository.
4. Use deterministic data and local or explicitly archived assets. Let Storybook `play` functions and assertions reach interactive states. Avoid driving stories through Playwright to simulate component coverage; the standard Storybook integration handles them directly.
5. Upload the selected stories through the CLI with the secret in the upload step's environment. Confirm the actual count, errors, skipped tests, review state, branch, and SHA from the resulting build.

Check imported global CSS, custom fonts, portals, and responsive parameters before interpreting diffs. Changes to UI, typography, or layout are reviewable differences; missing assets, failed stories, or random fixtures are setup defects.

Use targeted/TurboSnap options only when supported and tracing/external assets are configured correctly. First establish complete coverage and an unchanged control build; do not enable skips that conceal missing tests. Do not apply Storybook-only optimizations blindly to the screen lane.

Official references:
- [Chromatic CLI and configuration](https://www.chromatic.com/docs/cli/)
- [Combine component and E2E visual testing](https://www.chromatic.com/docs/combine-stories-e2e/) — separate projects for both lanes.
