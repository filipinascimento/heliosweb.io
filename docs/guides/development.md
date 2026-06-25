# Development And Contributing

This guide replaces the old top-level Reference pages. It collects the practical
development workflow for people editing this checkout, rebuilding generated
artifacts, and keeping the docs-site in sync with source annotations.

## Repository Shape

The Helios checkout contains related packages rather than one single package:

- `helios-network-v2` is the C/WASM graph store plus JavaScript, Python, and
  native C surfaces.
- `helios-web` is the renderer, interaction, behavior, UI, layout,
  persistence, and export package.
- `docs-site` is the MkDocs site. It stages local bundles from the package
  `dist/` folders before building.

Several package folders have their own build and test commands. Do not assume a
top-level build updates everything.

## Local Build Order

When native/network code changes:

```bash
cd helios-network-v2
npm install
npm run build:wasm
npm run build
npm test
```

When web renderer, UI, examples, or docs runtime code changes:

```bash
cd helios-web
npm install
npm run build
npm test
```

When docs-site pages or generated API references change:

```bash
cd docs-site
python3 scripts/build_docs.py
```

`scripts/build_docs.py` stages local Helios bundles into
`docs/assets/vendor/helios/`, regenerates API reference Markdown, and runs
MkDocs in strict mode.

## Local Preview And Sharing

For a local-only preview:

```bash
cd docs-site
python3 scripts/build_docs.py
python3 -m http.server 8111 --directory site
```

Open `http://localhost:8111/`. This serves the already-built static site, so it
matches the generated artifacts exactly.

For live editing, use MkDocs directly after dependencies are installed:

```bash
cd docs-site
mkdocs serve --dev-addr 127.0.0.1:8111
```

Use a host-network tunnel or LAN binding only when the machine should be
reachable from another device:

```bash
cd docs-site
python3 -m http.server 8111 --bind 0.0.0.0 --directory site
```

The docs examples load staged local bundles from `docs/assets/vendor/helios/`.
If a visual example is stale, rebuild the packages first, then rebuild the docs
site so those bundles are copied again.

## API Documentation Contract

API reference pages are generated from source:

- Helios Web: public exports in `src/index.js` plus JSDoc in implementation
  files.
- Helios Network JS/WASM: public JS exports and JSDoc in
  `src/js/HeliosNetwork.js`.
- Python: `helios_network.__all__` and docstrings.
- Native C: `CX_EXTERN` declarations and Doxygen comments in public headers.

Do not hand-edit generated API Markdown as the source of truth. Fix the source
annotation or the generator, then rebuild the docs-site.

`helios-web/src/index.d.ts` is a downstream declaration surface. It should
be generated from source annotations; until that workflow is wired into the
package scripts, do not patch the declaration file by hand to close docs gaps.

When adding public API, update the owning source annotation first:

1. Add a summary that explains what the symbol is for.
2. Add parameter and return descriptions for public methods.
3. Add `@remarks` when there is lifecycle, memory, renderer, or persistence
   behavior that is not obvious from the signature.
4. Add a short `@example` when the API is commonly called directly.
5. Rebuild the docs-site and confirm the symbol appears in the expected API
   group.

For Helios Network buffer APIs, document memory lifetime explicitly. WASM typed
array views can become invalid after allocation or memory growth, so docs should
explain whether an API returns a view, copies data, allocates, or must be called
inside `withBufferAccess(...)`.

## Docs-Site Link Checks

MkDocs strict mode catches missing files in navigation, but not every generated
runtime path. After API generator changes, check representative section links:

```bash
cd docs-site
python3 scripts/build_docs.py
python3 -m http.server 8111 --directory site
```

Then verify paths like:

```text
http://localhost:8111/api/helios-web/section-mappers/
http://localhost:8111/api/helios-web/Mapper/
```

Section cards should link to sibling symbol pages, not nested URLs such as
`section-mappers/Mapper/`.

## Public URLs And Release Builds

This repo owns the public website, app, and docs URLs:

- The live application URL is configured under `extra.helios.public_urls.app`
  in `mkdocs.yml`.
- The docs URL is configured under `extra.helios.public_urls.docs`.
- Package examples use the public names `helios-network` and `helios-web`.
- Runnable docs examples use the staged 0.10.0 bundles from
  `docs/assets/vendor/helios`.

When release artifacts change, update these places together:

1. Installation and Getting Started guides.
2. Data-format load/save examples where package imports are shown.
3. `mkdocs.yml` public URLs and sidecode import map if examples should load
   from published bundles.
4. App integration pages that reference CLI, Widget, or Desktop package names.
5. Generated API package version labels by rebuilding from the released package
   metadata.

## Visual Example QA

The docs include rendered examples. After changing examples, renderer behavior,
or staged bundles, run:

```bash
cd docs-site
node scripts/validate_visual_examples.mjs
```

The validator loads the built site in Playwright, waits for each selected
sidecode canvas, screenshots it, and fails if the canvas is blank or if the page
reports browser console errors.

## Versioning Notes

Docs versions follow package releases. Keep examples written with package-style
imports and tag this repository with the matching release tag, such as
`v0.10.0`.

Record documentation-impacting changes in the package changelog when a public
API, supported file format, import path, persistence envelope, or generated
declaration surface changes. If the change only expands prose or examples, a
changelog entry is usually unnecessary unless it corrects a published mistake.
