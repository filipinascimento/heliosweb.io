# Visual Examples

Helios Web examples are organized by the way people usually learn the library:
start with a small rendered graph, add data attributes and mappers, add
interaction, then move into layout, filtering, persistence, export, mobile
behavior, and custom behavior.

The snippets use package-style imports. In the docs runtime those imports are
mapped to the local bundles staged under `assets/vendor/helios/`, so the code
looks like package code while still running against this checkout.

Built-in behaviors attach by default. Most examples create `new Helios(...)`
with only `container` and `mode`, then use `helios.behavior.*` for public
behavior APIs. Constructor `behaviors` options appear only when the example is
changing behavior parameters.

## Categories

- [Basic rendering](basic.md) creates the smallest useful visual graph.
- [Attributes, mappers, and legends](attributes-mappers.md) maps data fields to
  node and edge visual channels using the new chainable attribute writers.
- [Interaction and labels](interaction-labels.md) covers selection, hover, and
  label behavior.
- [Layouts and filters](layouts-filters.md) controls layout execution and
  narrows the rendered view with attribute filters.
- [Persistence and export](persistence-export.md) saves/restores visualization
  state and creates a figure preview.
- [Touch and mobile controls](mobile-custom.md) configures compact/touch state
  and mobile-friendly behavior options.
- [Extension patterns](advanced-apis.md) shows focused uses of
  `HeliosFilter`, categorical colormap helpers, web component registration, and
  custom UI controller patterns.

The low-level buffer API is intentionally not the first thing shown in Helios
Web examples. It remains documented as the fast path in
[Helios Network low-level buffer access](../helios-network/buffer-access.md).
