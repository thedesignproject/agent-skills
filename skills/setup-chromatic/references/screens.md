# Application screens without a maintained component Storybook

Use [Chromatic's Playwright integration](https://www.chromatic.com/docs/playwright/) with existing browser tests when suitable. A generated archive may use Storybook internally; that does not require maintaining component stories or mean the repository has a product Storybook.

## Inventory first

Read routes/page entrypoints and product flows. Map each distinct screen/template to explicit states and readiness assertions. Include important dialogs, panels, authentication, permission, empty/error/success states and responsive layouts where applicable. For widgets/extensions, distinguish the real rendered UI from installation, browser permissions, background tasks, or backend behavior that fixtures do not validate.

Start with one browser, primary theme, and viewport. Add responsive/theme cases when they expose distinct layouts. Deduplicate shared content templates. Show the inventory count and estimate the multiplier before adding another axis. Count snapshots, not just test files or routes. Reconcile executed captures and cloud results to that inventory.

## Smallest supported implementation

Install compatible development dependencies `chromatic`, `@chromatic-com/playwright`, and Playwright if absent. Use the adapter's `test`/`expect` in selected visual tests; use targeted snapshots for intermediate states instead of capturing every step. Confirm the installed adapter's APIs and supported browser configuration in current docs/types.

Run the app with test fixture APIs, or a small production-source harness when real backend/auth prerequisites would otherwise make setup impractical. Reuse production views; do not recreate them as visual stand-ins. Keep this harness out of production routes/builds. Ensure generated archives, images, traces, and reports are ignored by Git and are not staged for commit. Isolate capture output and set `CHROMATIC_ARCHIVE_LOCATION` consistently if the output directory changes. Run tests before `chromatic --playwright`; use an explicit config per project in both mode.

Default to the official archive pipeline. Don't start by copying private adapter internals or a custom Storybook renderer. If an actual reproducible archive defect needs an extension, keep it narrow, record the reason/version constraint, and verify its fidelity before relying on cloud diffs.

## Deterministic content and faithful capture

- Use fixture accounts/data, fixed clocks/time zones/locales, stable IDs, and mocked error states. Keep uploads free of live customer data and credentials. Make unexpected external/API requests fail visibly rather than returning empty generic successes.
- Wait for meaningful state assertions, images, layout, and fonts. Prefer supported reduced-motion/animation settings. Assert essential visible content after stabilization, such as every expected item in a repeated list; a source image and replay can both omit the same element.
- If animation state is serialized incorrectly, use supported motion controls first. Any narrowly verified workaround must settle the intended final state consistently in source and archive rather than copying an intermediate frame. Assert visibility of overlays and repeated items after stabilization.
- Bundle the fonts used by the UI. Synthetic canvas screenshots must use a fixed raster fixture or a verified bundled-font path; system-font drawing differs across machines. Keep masks/ignored regions narrow and justified.
- Prefer static poster fixtures to nondeterministic video playback where motion is not the test subject. Don't load secrets into the fixture build; provide the project token only to the upload process.
- For a fixture harness or archive workaround, compare stable source screenshots with replayed archives before uploading. Inspect representative images, not just exit codes. Do not relax thresholds to conceal missing text, cards, overlays, focus, or scroll restoration.

Diagnose artifact size and upload time independently of test time. Avoid unnecessary assets or repeated scroll captures. Reuse the CLI's incremental uploads; don't force an entire repository archive or disable hashing without evidence. An expired upload authorization needs a fresh invocation, not repeated use of an old upload request.

Official references:
- [Playwright setup](https://www.chromatic.com/docs/playwright/)
- [Playwright configuration](https://www.chromatic.com/docs/playwright/configure/)
- [Targeted snapshots](https://www.chromatic.com/docs/playwright/targeted-snapshots/)
