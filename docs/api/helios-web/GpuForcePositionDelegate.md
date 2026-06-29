# GpuForcePositionDelegate

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/delegates/GpuForcePositionDelegate.js:5279</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Position delegate used by GPU force layouts.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class GpuForcePositionDelegate extends PositionDelegate {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">GPU force layout delegate options and resource handles.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Delegate that synchronizes graph topology to GPU buffers and exposes position snapshots to Helios renderers.</p><span class="helios-api-return-type"><strong>Type</strong> <code>GpuForcePositionDelegate</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
This is a low-level extension point. Most applications configure it
indirectly through `GpuForceLayout` or `LayoutBehavior`.
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-resetdynamicstatefromnetwork" class="helios-api-member-anchor"></a>

### `resetDynamicStateFromNetwork(context = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5464</code></p>
<p>Updates the dynamic state from network state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>resetDynamicStateFromNetwork</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-capturenetworkversionsnapshot" class="helios-api-member-anchor"></a>

### `captureNetworkVersionSnapshot(network)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5523</code></p>
<p>Configures or reads capture network version snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Network instance to read from or mutate.</td></tr>
</tbody>
</table>
</div>

<a id="method-synchronizenodepositionstonetwork" class="helios-api-member-anchor"></a>

### `synchronizeNodePositionsToNetwork(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:6257</code></p>
<p>Configures or reads synchronize node positions to network.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>synchronizeNodePositionsToNetwork</code>.</td></tr>
</tbody>
</table>
</div>

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-getnodepositionview" class="helios-api-member-anchor"></a>

### `getNodePositionView(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5941</code></p>
<p>Returns the current node position view value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getNodePositionView</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-getwebgpupositionbuffer" class="helios-api-member-anchor"></a>

### `getWebGPUPositionBuffer(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5954</code></p>
<p>Returns the current web gpuposition buffer value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getWebGPUPositionBuffer</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-getwebglpositiontexture" class="helios-api-member-anchor"></a>

### `getWebGLPositionTexture(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5966</code></p>
<p>Returns the current web glposition texture value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getWebGLPositionTexture</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-getgpupositionresource" class="helios-api-member-anchor"></a>

### `getGpuPositionResource(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5979</code></p>
<p>Returns the current gpu position resource value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getGpuPositionResource</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-snapshotnodepositions" class="helios-api-member-anchor"></a>

### `snapshotNodePositions(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5992</code></p>
<p>Configures or reads snapshot node positions.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>snapshotNodePositions</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-snapshotnodepositionsbyid" class="helios-api-member-anchor"></a>

### `snapshotNodePositionsById(context = {}, nodeIds = [], options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:6079</code></p>
<p>Configures or reads snapshot node positions by id.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>snapshotNodePositionsById</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>nodeIds</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>[]</code></td><td class="helios-api-param-description">Node or edge identifiers/indices used by the operation.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-writepositionsnapshot" class="helios-api-member-anchor"></a>

### `writePositionSnapshot(snapshot, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:6241</code></p>
<p>Configures or reads write position snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writePositionSnapshot</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

## Appearance { #api-appearance .helios-api-section-title }

<p class="helios-api-section-description">Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.</p>

<a id="method-flattennodedepthtoplane" class="helios-api-member-anchor"></a>

### `flattenNodeDepthToPlane(context = {}, zValue = 0)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:6282</code></p>
<p>Configures or reads flatten node depth to plane.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>flattenNodeDepthToPlane</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>zValue</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>0</code></td><td class="helios-api-param-description">Value passed to <code>flattenNodeDepthToPlane</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-injectplanardepthjitter" class="helios-api-member-anchor"></a>

### `injectPlanarDepthJitter(context = {}, amplitude = 0)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:6323</code></p>
<p>Configures or reads inject planar depth jitter.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>injectPlanarDepthJitter</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>amplitude</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>0</code></td><td class="helios-api-param-description">Value passed to <code>injectPlanarDepthJitter</code>.</td></tr>
</tbody>
</table>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-resetannealing" class="helios-api-member-anchor"></a>

### `resetAnnealing()` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5473</code></p>
<p>Updates the annealing state on the current instance.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-getcompletedepochs" class="helios-api-member-anchor"></a>

### `getCompletedEpochs()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5484</code></p>
<p>Returns the current completed epochs value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getCompletedEpochs();
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-marktopologydirty" class="helios-api-member-anchor"></a>

### `markTopologyDirty(reason = 'manual')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5343</code></p>
<p>Configures or reads mark topology dirty.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;manual&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-diddetach" class="helios-api-member-anchor"></a>

### `didDetach()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5354</code></p>
<p>Configures or reads did detach.</p>
</div>

<a id="method-updateoptions" class="helios-api-member-anchor"></a>

### `updateOptions(next = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5358</code></p>
<p>Configures or reads update options.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>next</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>updateOptions</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-dispose" class="helios-api-member-anchor"></a>

### `dispose()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5427</code></p>
<p>Configures or reads dispose.</p>
</div>

<a id="method-synchronizetopology" class="helios-api-member-anchor"></a>

### `synchronizeTopology(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5587</code></p>
<p>Configures or reads synchronize topology.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>synchronizeTopology</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-step" class="helios-api-member-anchor"></a>

### `step(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:5730</code></p>
<p>Configures or reads step.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>step</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-snapshotnodecentroidbyid" class="helios-api-member-anchor"></a>

### `snapshotNodeCentroidById(context = {}, nodeIds = [], options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/GpuForcePositionDelegate.js:6153</code></p>
<p>Configures or reads snapshot node centroid by id.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>snapshotNodeCentroidById</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>nodeIds</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>[]</code></td><td class="helios-api-param-description">Node or edge identifiers/indices used by the operation.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>
