# Behaviors

Helios Web behaviors are reusable units of application logic that sit above the renderer and below UI panels. They are the public path for selection, hover, labels, legends, layout, mappers, filters, appearance, export, interface state, and persistence-aware workflows.

The API reference is generated from the public `helios-web/src/index.js` export surface. Authored behavior guides should use only symbols exported there.

Common public entry points include `Behavior`, `BehaviorRegistry`, `BehaviorManager`, `SelectionBehavior`, `HoverBehavior`, `LabelsBehavior`, `LegendsBehavior`, `LayoutBehavior`, `AppearanceBehavior`, and `createDefaultBehaviorRegistry`.
