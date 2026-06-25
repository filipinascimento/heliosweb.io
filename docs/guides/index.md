# Guides

Guides explain how the runtime pieces fit together. They are longer-form than
examples: an example should show one small thing; a guide should explain when to
use it, what it changes internally, and what tradeoffs matter in an application.

## Application Setup

- [Installation and bundling](installation.md) covers package installation,
  `package.json`, Vite, ESM imports, CDN-style imports, local checkout bundles,
  and common asset/runtime mistakes.
- [Development and contributing](development.md) covers local builds, docs-site
  generation, generated API pages, versioning notes, and how to keep package
  artifacts synchronized.

## Helios Web Concepts

- [Behaviors](behaviors.md) covers reusable application logic for selection,
  hover, labels, legends, mappers, filters, layout, export, and interface state.
- [Persistence](persistence.md) covers `helios.states`, `helios.storage`,
  sessions, portable network state, and host storage integration.

## Graph Data

- [Data formats](data-formats/index.md) explains BXNet, ZXNet, XNet, GML, graph-tool
  GT/GT.ZST, node-link JSON, and load/save examples across JS/WASM, Helios Web,
  Python, native C, and CLI.

## Documentation And API Surface

- [API documentation pipeline](api-docs-pipeline.md) defines the source-first
  contract for generated reference pages and future declaration generation.
- [Apps and integrations](../apps/index.md) covers Helios CLI, Widget, and
  Desktop host surfaces.

The next guide topics should be renderer capability strategy, production
deployment, mobile input design, app-shell integration, and remote storage
backends. New guides should include code and link back to the generated API
reference instead of describing unverified behavior from memory.
