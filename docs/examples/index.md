# Examples

Examples are the foundation for this documentation reset. A page is considered
release-worthy only when it uses public APIs, runs against local Helios bundles,
and demonstrates a real graph/data workflow.

## Visual Examples

Use these when building a browser visualization. They render actual graph
canvases, interaction state, UI panels, legends, filters, persistence, or
exported figure output with `mkdocs-sidecode`.

- [Basic rendering](helios-web/basic.md)
- [Attributes, mappers, and legends](helios-web/attributes-mappers.md)
- [Interaction and labels](helios-web/interaction-labels.md)
- [Layouts and filters](helios-web/layouts-filters.md)
- [Persistence and export](helios-web/persistence-export.md)
- [Touch and mobile controls](helios-web/mobile-custom.md)
- [Extension patterns](helios-web/advanced-apis.md)

Open the [visual examples guide](helios-web/index.md).

## Data/API Examples

Use these when working with graphs as data. They lead with the chainable
attribute writers and keep the direct buffer API as an explicit fast path.

- [Graphs and attributes](helios-network/graphs-attributes.md)
- [Selectors and serialization](helios-network/selectors-serialization.md)
- [Low-level buffer access](helios-network/buffer-access.md)
- [Language bindings](helios-network/language-bindings.md)

Open the [data/API examples guide](helios-network/index.md).

## Retired Scaffold

The original tiny behavior and persistence examples remain in the repository as
scaffold history, but they are not in the release navigation. New guides should
be written from the visual and API/data examples above.
