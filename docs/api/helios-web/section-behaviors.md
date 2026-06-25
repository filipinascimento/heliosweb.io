
# Behaviors

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

Composable behavior modules for interaction, labels, legends, mappers, filters, interface state, and export controls.

Behaviors are the user-facing modules that keep Helios composable. Each behavior
owns one workflow, such as labels, legends, filters, mappers, layout controls,
selection, hover inspection, interface controls, persistence, or export. The
behavior manager creates the default set, and applications can register custom
behavior classes when they need different UI or state synchronization.

Read the base `Behavior` contract first if you are adding a new behavior. Use
the implementation pages when you want to configure an existing workflow.

## Core

<p class="helios-api-group-description">Base behavior contracts, registry helpers, and runtime managers shared by every behavior.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../Behavior/">
<span>class</span>
<strong>Behavior</strong>
<em>Base class for reusable Helios application behaviors.</em>
</a>
<a class="helios-api-directory-item" href="../BehaviorManager/">
<span>class</span>
<strong>BehaviorManager</strong>
<em>Runtime owner for active behavior instances on a Helios visualization.</em>
</a>
<a class="helios-api-directory-item" href="../BehaviorRegistry/">
<span>class</span>
<strong>BehaviorRegistry</strong>
<em>Registry mapping behavior ids to behavior constructors or factories.</em>
</a>
</div>


## Behavior Implementations

<p class="helios-api-group-description">Built-in behavior classes that attach interaction, layout, mapper, filter, labels, legends, interface, and export workflows to a Helios instance.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../AppearanceBehavior/">
<span>class</span>
<strong>AppearanceBehavior</strong>
<em>Built-in behavior for global visual appearance and render quality.</em>
</a>
<a class="helios-api-directory-item" href="../ExporterBehavior/">
<span>class</span>
<strong>ExporterBehavior</strong>
<em>Built-in behavior for figure export settings and preview capture.</em>
</a>
<a class="helios-api-directory-item" href="../FilterBehavior/">
<span>class</span>
<strong>FilterBehavior</strong>
<em>Built-in behavior for graph filtering.</em>
</a>
<a class="helios-api-directory-item" href="../HoverBehavior/">
<span>class</span>
<strong>HoverBehavior</strong>
<em>Built-in behavior for hover picking and hover labels.</em>
</a>
<a class="helios-api-directory-item" href="../InterfaceBehavior/">
<span>class</span>
<strong>InterfaceBehavior</strong>
<em>Built-in behavior for responsive interface and touch-oriented app state.</em>
</a>
<a class="helios-api-directory-item" href="../LabelsBehavior/">
<span>class</span>
<strong>LabelsBehavior</strong>
<em>Built-in behavior for SVG label overlays.</em>
</a>
<a class="helios-api-directory-item" href="../LayoutBehavior/">
<span>class</span>
<strong>LayoutBehavior</strong>
<em>Built-in behavior for choosing and controlling the active layout.</em>
</a>
<a class="helios-api-directory-item" href="../LegendsBehavior/">
<span>class</span>
<strong>LegendsBehavior</strong>
<em>Built-in behavior for legend overlays.</em>
</a>
<a class="helios-api-directory-item" href="../MappersBehavior/">
<span>class</span>
<strong>MappersBehavior</strong>
<em>Built-in behavior for node and edge visual mappers.</em>
</a>
<a class="helios-api-directory-item" href="../SelectionBehavior/">
<span>class</span>
<strong>SelectionBehavior</strong>
<em>Built-in behavior for node and edge selection state.</em>
</a>
</div>


## Auxiliary

<p class="helios-api-group-description">Supporting exports used to configure or compose behavior integrations.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../BEHAVIOR_IDS/">
<span>symbol</span>
<strong>BEHAVIOR_IDS</strong>
<em>Ordered ids for the built-in behavior set.</em>
</a>
<a class="helios-api-directory-item" href="../createDefaultBehaviorRegistry/">
<span>function</span>
<strong>createDefaultBehaviorRegistry</strong>
<em>Create a registry containing all built-in Helios Web behaviors.</em>
</a>
</div>
