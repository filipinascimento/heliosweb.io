
# Helios Web API

<img class="helios-api-logo" src="../../assets/helios-logo.svg" alt="Helios Web logo">

<p class="helios-api-version">Version 0.10.0</p>

Helios Web is the browser visualization layer: renderer selection, camera and interaction state, behaviors, mappers, filters, layouts, persistence, and export. The reference below is grouped by the way users usually extend or configure a visualization.

## Core

<p class="helios-api-group-description">The main visualization controller and primary user-facing entry points.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="Helios/">
<span>class</span>
<strong>Helios</strong>
<em>Main Helios Web visualization controller for one `helios-network` graph.</em>
</a>
</div>


## Constants

<p class="helios-api-group-description">Named event ids, figure presets, and other exported constant surfaces.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="EVENTS/">
<span>symbol</span>
<strong>EVENTS</strong>
<em>Stable event names emitted by `Helios` instances.</em>
</a>
<a class="helios-api-directory-item" href="FIGURE_EXPORT_PRESETS/">
<span>symbol</span>
<strong>FIGURE_EXPORT_PRESETS</strong>
<em>Built-in figure size presets for Helios exports.</em>
</a>
</div>


## Behaviors

<p class="helios-api-group-description">Composable behavior modules for interaction, labels, legends, mappers, filters, interface state, and export controls.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="AppearanceBehavior/">
<span>class</span>
<strong>AppearanceBehavior</strong>
<em>Built-in behavior for global visual appearance and render quality.</em>
</a>
<a class="helios-api-directory-item" href="Behavior/">
<span>class</span>
<strong>Behavior</strong>
<em>Base class for reusable Helios application behaviors.</em>
</a>
<a class="helios-api-directory-item" href="BEHAVIOR_IDS/">
<span>symbol</span>
<strong>BEHAVIOR_IDS</strong>
<em>Ordered ids for the built-in behavior set.</em>
</a>
<a class="helios-api-directory-item" href="BehaviorManager/">
<span>class</span>
<strong>BehaviorManager</strong>
<em>Runtime owner for active behavior instances on a Helios visualization.</em>
</a>
<a class="helios-api-directory-item" href="BehaviorRegistry/">
<span>class</span>
<strong>BehaviorRegistry</strong>
<em>Registry mapping behavior ids to behavior constructors or factories.</em>
</a>
<a class="helios-api-directory-item" href="createDefaultBehaviorRegistry/">
<span>function</span>
<strong>createDefaultBehaviorRegistry</strong>
<em>Create a registry containing all built-in Helios Web behaviors.</em>
</a>
<a class="helios-api-directory-item" href="ExporterBehavior/">
<span>class</span>
<strong>ExporterBehavior</strong>
<em>Built-in behavior for figure export settings and preview capture.</em>
</a>
<a class="helios-api-directory-item" href="FilterBehavior/">
<span>class</span>
<strong>FilterBehavior</strong>
<em>Built-in behavior for graph filtering.</em>
</a>
<a class="helios-api-directory-item" href="HoverBehavior/">
<span>class</span>
<strong>HoverBehavior</strong>
<em>Built-in behavior for hover picking and hover labels.</em>
</a>
<a class="helios-api-directory-item" href="InterfaceBehavior/">
<span>class</span>
<strong>InterfaceBehavior</strong>
<em>Built-in behavior for responsive interface and touch-oriented app state.</em>
</a>
<a class="helios-api-directory-item" href="LabelsBehavior/">
<span>class</span>
<strong>LabelsBehavior</strong>
<em>Built-in behavior for SVG label overlays.</em>
</a>
<a class="helios-api-directory-item" href="LayoutBehavior/">
<span>class</span>
<strong>LayoutBehavior</strong>
<em>Built-in behavior for choosing and controlling the active layout.</em>
</a>
<a class="helios-api-directory-item" href="LegendsBehavior/">
<span>class</span>
<strong>LegendsBehavior</strong>
<em>Built-in behavior for legend overlays.</em>
</a>
<a class="helios-api-directory-item" href="MappersBehavior/">
<span>class</span>
<strong>MappersBehavior</strong>
<em>Built-in behavior for node and edge visual mappers.</em>
</a>
<a class="helios-api-directory-item" href="SelectionBehavior/">
<span>class</span>
<strong>SelectionBehavior</strong>
<em>Built-in behavior for node and edge selection state.</em>
</a>
</div>


## Layouts

<p class="helios-api-group-description">Layout controllers and position delegates for static, worker, D3 force, and GPU force layouts.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="D3Force3DLayout/">
<span>class</span>
<strong>D3Force3DLayout</strong>
<em>Worker-backed layout adapter for the D3 Force 3D engine.</em>
</a>
<a class="helios-api-directory-item" href="DEFAULT_LAYOUT_TUNING_MODEL/">
<span>symbol</span>
<strong>DEFAULT_LAYOUT_TUNING_MODEL</strong>
<em>Default model used to tune GPU force layout options from graph statistics.</em>
</a>
<a class="helios-api-directory-item" href="extractLayoutTuningFeatures/">
<span>function</span>
<strong>extractLayoutTuningFeatures</strong>
<em>Extract graph features used by the layout tuning model.</em>
</a>
<a class="helios-api-directory-item" href="GpuForceLayout/">
<span>class</span>
<strong>GpuForceLayout</strong>
<em>GPU-backed force layout that can run through WebGPU or WebGL2 delegates.</em>
</a>
<a class="helios-api-directory-item" href="GpuForcePositionDelegate/">
<span>class</span>
<strong>GpuForcePositionDelegate</strong>
<em>Position delegate used by GPU force layouts.</em>
</a>
<a class="helios-api-directory-item" href="Layout/">
<span>class</span>
<strong>Layout</strong>
<em>Base class for layout algorithms.</em>
</a>
<a class="helios-api-directory-item" href="PositionDelegate/">
<span>class</span>
<strong>PositionDelegate</strong>
<em>Abstract source for layout positions owned outside the network buffers.</em>
</a>
<a class="helios-api-directory-item" href="predictLayoutTuningOptions/">
<span>function</span>
<strong>predictLayoutTuningOptions</strong>
<em>Predict layout option overrides for a network using the layout tuning model.</em>
</a>
<a class="helios-api-directory-item" href="StaticLayout/">
<span>class</span>
<strong>StaticLayout</strong>
<em>Layout that keeps existing node positions fixed.</em>
</a>
<a class="helios-api-directory-item" href="WorkerLayout/">
<span>class</span>
<strong>WorkerLayout</strong>
<em>Worker-backed force or jitter layout.</em>
</a>
</div>


## Mappers

<p class="helios-api-group-description">Visual attribute mapping primitives used to bind graph data to colors, sizes, opacity, and related channels.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="Mapper/">
<span>class</span>
<strong>Mapper</strong>
<em>Low-level mapper for one node or edge visual mode.</em>
</a>
<a class="helios-api-directory-item" href="MapperCollection/">
<span>class</span>
<strong>MapperCollection</strong>
<em>Collection of named mappers for either node or edge visuals.</em>
</a>
<a class="helios-api-directory-item" href="VISUAL_ATTRIBUTES/">
<span>symbol</span>
<strong>VISUAL_ATTRIBUTES</strong>
<em>Map of public mapper channel names to internal Helios visual attribute names.</em>
</a>
<a class="helios-api-directory-item" href="VisualAttributes/">
<span>class</span>
<strong>VisualAttributes</strong>
<em>Ensures required visual attributes exist on the Helios network, seeds defaults, and provides helpers to apply mappers into sparse buffers.</em>
</a>
</div>


## Filters

<p class="helios-api-group-description">Filter builders and behavior APIs for render-only or render-and-layout graph filtering.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="HeliosFilter/">
<span>class</span>
<strong>HeliosFilter</strong>
<em>Builder for reusable graph filter rule sets.</em>
</a>
</div>


## Export

<p class="helios-api-group-description">Figure export presets, capability checks, PNG/SVG capture, and preview helpers.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="buildFigureExportPresetList/">
<span>function</span>
<strong>buildFigureExportPresetList</strong>
<em>Build export preset metadata for a viewport and renderer capability.</em>
</a>
<a class="helios-api-directory-item" href="getFigureExportCapability/">
<span>function</span>
<strong>getFigureExportCapability</strong>
<em>Resolve renderer limits that constrain figure export dimensions.</em>
</a>
<a class="helios-api-directory-item" href="resolveFigureExportOptions/">
<span>function</span>
<strong>resolveFigureExportOptions</strong>
<em>Normalize figure export options into concrete dimensions and capture flags.</em>
</a>
</div>


## Persistence

<p class="helios-api-group-description">State manager, storage manager, session, preference, and envelope APIs for saving and restoring visualization state.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="applyOverridesToVisualizationState/">
<span>function</span>
<strong>applyOverridesToVisualizationState</strong>
<em>Apply sparse dotted-path overrides to a visualization state object.</em>
</a>
<a class="helios-api-directory-item" href="BrowserStorageManager/">
<span>class</span>
<strong>BrowserStorageManager</strong>
<em>Browser storage manager backed by IndexedDB and Web Storage fallbacks.</em>
</a>
<a class="helios-api-directory-item" href="createDefaultNetworkSource/">
<span>function</span>
<strong>createDefaultNetworkSource</strong>
<em>Normalize source-network metadata stored with visualization state.</em>
</a>
<a class="helios-api-directory-item" href="createDefaultPreferencesState/">
<span>function</span>
<strong>createDefaultPreferencesState</strong>
<em>Normalize a preferences payload into the current public preference shape.</em>
</a>
<a class="helios-api-directory-item" href="createDefaultUIState/">
<span>function</span>
<strong>createDefaultUIState</strong>
<em>Normalize a UI payload into the current serializable UI state shape.</em>
</a>
<a class="helios-api-directory-item" href="createHeliosStorageManager/">
<span>function</span>
<strong>createHeliosStorageManager</strong>
<em>Create the storage manager selected by a Helios `storage` constructor option.</em>
</a>
<a class="helios-api-directory-item" href="createMemoryIndexedDBFactory/">
<span>function</span>
<strong>createMemoryIndexedDBFactory</strong>
<em>Create an in-memory IndexedDB-like factory for persistence tests.</em>
</a>
<a class="helios-api-directory-item" href="createMemoryStorage/">
<span>function</span>
<strong>createMemoryStorage</strong>
<em>Create an in-memory Storage-compatible object.</em>
</a>
<a class="helios-api-directory-item" href="createPersistenceEnvelope/">
<span>function</span>
<strong>createPersistenceEnvelope</strong>
<em>Create a versioned persistence envelope.</em>
</a>
<a class="helios-api-directory-item" href="diffOverrideMaps/">
<span>function</span>
<strong>diffOverrideMaps</strong>
<em>Compute sparse override differences between two flattened override maps.</em>
</a>
<a class="helios-api-directory-item" href="DummyStorageManager/">
<span>class</span>
<strong>DummyStorageManager</strong>
<em>In-memory storage facade used when durable persistence is disabled.</em>
</a>
<a class="helios-api-directory-item" href="flattenVisualizationOverrides/">
<span>function</span>
<strong>flattenVisualizationOverrides</strong>
<em>Flatten visualization state into sparse dotted override paths.</em>
</a>
<a class="helios-api-directory-item" href="HeliosStateManager/">
<span>class</span>
<strong>HeliosStateManager</strong>
<em>Central live state graph for Helios defaults, bindings, overrides, and reset status.</em>
</a>
<a class="helios-api-directory-item" href="HeliosStorageManager/">
<span>class</span>
<strong>HeliosStorageManager</strong>
<em>Base storage facade for Helios state snapshots, sessions, and portable network state.</em>
</a>
<a class="helios-api-directory-item" href="IndexedDBSessionStore/">
<span>class</span>
<strong>IndexedDBSessionStore</strong>
<em>Session store backed by IndexedDB.</em>
</a>
<a class="helios-api-directory-item" href="LocalStoragePreferenceStore/">
<span>class</span>
<strong>LocalStoragePreferenceStore</strong>
<em>Preference store backed by the browser `localStorage` API.</em>
</a>
<a class="helios-api-directory-item" href="migratePersistenceEnvelope/">
<span>function</span>
<strong>migratePersistenceEnvelope</strong>
<em>Normalize a partial persistence object into the current envelope.</em>
</a>
<a class="helios-api-directory-item" href="parsePersistenceEnvelope/">
<span>function</span>
<strong>parsePersistenceEnvelope</strong>
<em>Parse and migrate persistence input.</em>
</a>
<a class="helios-api-directory-item" href="PERSISTENCE_KINDS/">
<span>symbol</span>
<strong>PERSISTENCE_KINDS</strong>
<em>Supported persistence envelope kinds.</em>
</a>
<a class="helios-api-directory-item" href="PERSISTENCE_SCHEMA_VERSION/">
<span>symbol</span>
<strong>PERSISTENCE_SCHEMA_VERSION</strong>
<em>Current schema version for Helios Web persistence envelopes.</em>
</a>
<a class="helios-api-directory-item" href="RemoteStorageManager/">
<span>class</span>
<strong>RemoteStorageManager</strong>
<em>Storage manager that delegates session records to a host-provided client.</em>
</a>
<a class="helios-api-directory-item" href="serializePersistenceEnvelope/">
<span>function</span>
<strong>serializePersistenceEnvelope</strong>
<em>Serialize a persistence envelope to JSON.</em>
</a>
<a class="helios-api-directory-item" href="SessionStore/">
<span>class</span>
<strong>SessionStore</strong>
<em>Low-level session record store used by Helios storage managers.</em>
</a>
<a class="helios-api-directory-item" href="StateBindingController/">
<span>class</span>
<strong>StateBindingController</strong>
<em>Binding controller that keeps registered state entries synchronized with runtime owners.</em>
</a>
<a class="helios-api-directory-item" href="StateTransaction/">
<span>class</span>
<strong>StateTransaction</strong>
<em>Helper passed to `HeliosStateManager.transaction()` for grouped state writes.</em>
</a>
<a class="helios-api-directory-item" href="UIAttribute/">
<span>class</span>
<strong>UIAttribute</strong>
<em>Observable UI attribute descriptor used to bind controls to Helios state.</em>
</a>
</div>


## Internal

<p class="helios-api-group-description">Advanced exported utilities that are usually consumed by Helios Web itself or custom integrations.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="applyCameraPose/">
<span>function</span>
<strong>applyCameraPose</strong>
<em>Apply a captured or merged pose to a renderer camera.</em>
</a>
<a class="helios-api-directory-item" href="base64ToUint8Array/">
<span>function</span>
<strong>base64ToUint8Array</strong>
<em>Decode base64-encoded binary colormap data.</em>
</a>
<a class="helios-api-directory-item" href="CameraTransitionController/">
<span>class</span>
<strong>CameraTransitionController</strong>
<em>Time-based camera transition controller used by Helios camera animations.</em>
</a>
<a class="helios-api-directory-item" href="captureCameraPose/">
<span>function</span>
<strong>captureCameraPose</strong>
<em>Capture a renderer camera into a serializable pose object.</em>
</a>
<a class="helios-api-directory-item" href="colormaps/">
<span>symbol</span>
<strong>colormaps</strong>
<em>Built-in color map registry grouped by source collection.</em>
</a>
<a class="helios-api-directory-item" href="colormapToInterpolator/">
<span>function</span>
<strong>colormapToInterpolator</strong>
<em>Resolve a colormap to an interpolation function.</em>
</a>
<a class="helios-api-directory-item" href="colormapToScheme/">
<span>function</span>
<strong>colormapToScheme</strong>
<em>Resolve a colormap to a discrete color scheme.</em>
</a>
<a class="helios-api-directory-item" href="createCategoricalColormap/">
<span>function</span>
<strong>createCategoricalColormap</strong>
<em>Create a categorical palette from a colormap.</em>
</a>
<a class="helios-api-directory-item" href="createColormapScale/">
<span>function</span>
<strong>createColormapScale</strong>
<em>Create a numeric colormap scale.</em>
</a>
<a class="helios-api-directory-item" href="createDefaultMappers/">
<span>function</span>
<strong>createDefaultMappers</strong>
<em>Create the default node and edge mapper collections for a network.</em>
</a>
<a class="helios-api-directory-item" href="createPanelSchemaIndicator/">
<span>function</span>
<strong>createPanelSchemaIndicator</strong>
<em>Create a DOM indicator that reflects dirty status for a panel schema.</em>
</a>
<a class="helios-api-directory-item" href="createYawPitchQuaternion/">
<span>function</span>
<strong>createYawPitchQuaternion</strong>
<em>Build a normalized camera rotation quaternion from yaw and pitch angles.</em>
</a>
<a class="helios-api-directory-item" href="decodeColormapData/">
<span>function</span>
<strong>decodeColormapData</strong>
<em>Decode packed RGB colormap bytes into color tuples.</em>
</a>
<a class="helios-api-directory-item" href="DEFAULT_NODE_COLORMAP/">
<span>symbol</span>
<strong>DEFAULT_NODE_COLORMAP</strong>
<em>Default node colormap used by Helios when no explicit node color mapper is set.</em>
</a>
<a class="helios-api-directory-item" href="defineHeliosWebComponents/">
<span>function</span>
<strong>defineHeliosWebComponents</strong>
<em>Register Helios Web custom elements in a document or window.</em>
</a>
<a class="helios-api-directory-item" href="ensureDefaultStyles/">
<span>function</span>
<strong>ensureDefaultStyles</strong>
<em>Ensure the default Helios UI stylesheet is present in a document.</em>
</a>
<a class="helios-api-directory-item" href="FILTERS_PANEL_SCHEMA/">
<span>symbol</span>
<strong>FILTERS_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Filters panel.</em>
</a>
<a class="helios-api-directory-item" href="HeliosUI/">
<span>class</span>
<strong>HeliosUI</strong>
<em>Optional built-in control surface for a Helios visualization.</em>
</a>
<a class="helios-api-directory-item" href="humanizeControlLabel/">
<span>function</span>
<strong>humanizeControlLabel</strong>
<em>Convert a state key or control identifier into a display label.</em>
</a>
<a class="helios-api-directory-item" href="LABELS_PANEL_SCHEMA/">
<span>symbol</span>
<strong>LABELS_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Labels panel.</em>
</a>
<a class="helios-api-directory-item" href="LAYOUT_PANEL_SCHEMA/">
<span>symbol</span>
<strong>LAYOUT_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Layout panel.</em>
</a>
<a class="helios-api-directory-item" href="LEGENDS_PANEL_SCHEMA/">
<span>symbol</span>
<strong>LEGENDS_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Legends panel.</em>
</a>
<a class="helios-api-directory-item" href="MAPPERS_PANEL_SCHEMA/">
<span>symbol</span>
<strong>MAPPERS_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Mappers panel.</em>
</a>
<a class="helios-api-directory-item" href="mergeCameraPose/">
<span>function</span>
<strong>mergeCameraPose</strong>
<em>Merge a partial camera pose into an existing pose.</em>
</a>
<a class="helios-api-directory-item" href="normalizePanelSchema/">
<span>function</span>
<strong>normalizePanelSchema</strong>
<em>Normalize a panel schema into the canonical shape used by Helios UI panels.</em>
</a>
<a class="helios-api-directory-item" href="panelSchemaKeys/">
<span>function</span>
<strong>panelSchemaKeys</strong>
<em>Return all state keys referenced by a panel schema.</em>
</a>
<a class="helios-api-directory-item" href="panelSchemaSectionKeys/">
<span>function</span>
<strong>panelSchemaSectionKeys</strong>
<em>Return all state keys referenced by one panel schema section.</em>
</a>
<a class="helios-api-directory-item" href="panelSchemaSectionStatus/">
<span>function</span>
<strong>panelSchemaSectionStatus</strong>
<em>Compute the dirty status for one panel schema section.</em>
</a>
<a class="helios-api-directory-item" href="panelSchemaStatus/">
<span>function</span>
<strong>panelSchemaStatus</strong>
<em>Compute the dirty status for a full panel schema.</em>
</a>
<a class="helios-api-directory-item" href="PanelStack/">
<span>class</span>
<strong>PanelStack</strong>
<em>Collapsible stack of UI subpanels used by the optional Helios UI.</em>
</a>
<a class="helios-api-directory-item" href="resolvePanelItemLabel/">
<span>function</span>
<strong>resolvePanelItemLabel</strong>
<em>Resolve the display label for a panel schema item.</em>
</a>
<a class="helios-api-directory-item" href="SCENE_PANEL_SCHEMA/">
<span>symbol</span>
<strong>SCENE_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Scene panel.</em>
</a>
<a class="helios-api-directory-item" href="SELECTION_PANEL_SCHEMA/">
<span>symbol</span>
<strong>SELECTION_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Selection panel.</em>
</a>
<a class="helios-api-directory-item" href="TabbedPanel/">
<span>class</span>
<strong>TabbedPanel</strong>
<em>Small tabbed panel primitive used by the optional Helios UI.</em>
</a>
</div>



## Typed Reference

The docs build emits a structured typed reference at [`../reference.json`](../reference.json) from source exports and code annotations. TypeScript declaration files are downstream artifacts and are not used as an API documentation source.

## Annotation Coverage Notes

Top-level public exports without source summaries:

- No unannotated public exports detected.

Primary public class members currently using generated fallback descriptions:

- No generated member-summary fallbacks detected.
