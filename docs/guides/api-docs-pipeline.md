# API Documentation Pipeline

The extraction pipeline is implemented in `scripts/generate_api_reference.py`.

It generates Markdown reference pages before MkDocs builds:

- Helios Web from the `filipinascimento/helios-web` source checkout.
- Helios Network JS/WASM from `src/helios-network.js` and JSDoc in `src/js/HeliosNetwork.js`.
- Helios Network Python from `helios_network.__all__` and docstrings.
- Helios Network native C from `CX_EXTERN` declarations and Doxygen-style comments in public headers.

Helios Web and Helios Network API extraction should use source checkouts from
GitHub. The docs runtime, examples, landing preview, and `/app/` route still use
the npm-installed packages staged into `docs/assets/vendor/helios/`. Set
`HELIOS_WEB_SOURCE` or `HELIOS_NETWORK_SOURCE` when the source checkouts are not
adjacent to this repository.

`index.d.ts` files are not documentation sources. They should be generated from
the same source annotations that feed the API pages. Do not hand-edit generated
declaration files to close documentation gaps; until declaration generation is
wired, existing declaration files are treated as legacy compatibility surfaces
and documented as a release gap.

## Current Limitations

This is the first integration point, not the final extraction stack. The likely
next improvements are TypeScript declaration generation from JSDoc for Helios
Web, JSDoc-to-Markdown or declaration generation for Helios Network JS/WASM,
mkdocstrings for Python, and Doxygen XML ingestion for native C.

The important release invariant is already in place: generated API pages are
part of the docs build path and should be regenerated from the exact package or
source checkout being documented.
