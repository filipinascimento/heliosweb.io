# PositionDelegate

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/delegates/PositionDelegate.js:34</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Abstract source for layout positions owned outside the network buffers.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class PositionDelegate {
```

</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Subclasses provide synchronized topology and position snapshots for renderers.</p><span class="helios-api-return-type"><strong>Type</strong> <code>PositionDelegate</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Use position delegates when layout state lives in GPU buffers or
another external system. Subclasses must implement synchronization hooks and
bump `version` whenever positions change.
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-capturenetworkversionsnapshot" class="helios-api-member-anchor"></a>

### `captureNetworkVersionSnapshot(network)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:183</code></p>
<p>Configures or reads capture network version snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Network instance to read from or mutate.</td></tr>
</tbody>
</table>
</div>

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-getnodepositionview" class="helios-api-member-anchor"></a>

### `getNodePositionView(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:107</code></p>
<p>Returns the current node position view value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getNodePositionView</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-getpositionview" class="helios-api-member-anchor"></a>

### `getPositionView(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:112</code></p>
<p>Returns the current position view value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getPositionView</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-getwebgpupositionbuffer" class="helios-api-member-anchor"></a>

### `getWebGPUPositionBuffer(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:116</code></p>
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

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:121</code></p>
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

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:126</code></p>
<p>Returns the current gpu position resource value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getGpuPositionResource</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-getpositionresource" class="helios-api-member-anchor"></a>

### `getPositionResource(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:131</code></p>
<p>Returns the current position resource value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getPositionResource</code>.</td></tr>
</tbody>
</table>
</div>

## Appearance { #api-appearance .helios-api-section-title }

<p class="helios-api-section-description">Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.</p>

<a id="method-flattennodedepthtoplane" class="helios-api-member-anchor"></a>

### `flattenNodeDepthToPlane(context = {}, zValue = 0)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:135</code></p>
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

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-getversion" class="helios-api-member-anchor"></a>

### `getVersion(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:102</code></p>
<p>Returns the current version value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>getVersion</code>.</td></tr>
</tbody>
</table>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-onattach" class="helios-api-member-anchor"></a>

### `onAttach(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:67</code></p>
<p>Configures or reads on attach.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>onAttach</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-ondetach" class="helios-api-member-anchor"></a>

### `onDetach(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:79</code></p>
<p>Configures or reads on detach.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>onDetach</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-marktopologydirty" class="helios-api-member-anchor"></a>

### `markTopologyDirty(reason = 'manual')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:92</code></p>
<p>Configures or reads mark topology dirty.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;manual&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-bumpversion" class="helios-api-member-anchor"></a>

### `bumpVersion()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:97</code></p>
<p>Configures or reads bump version.</p>
</div>

<a id="method-ensuresynchronized" class="helios-api-member-anchor"></a>

### `ensureSynchronized(context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:141</code></p>
<p>Configures or reads ensure synchronized.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>ensureSynchronized</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-synchronizetopology" class="helios-api-member-anchor"></a>

### `synchronizeTopology()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/delegates/PositionDelegate.js:202</code></p>
<p>Configures or reads synchronize topology.</p>
</div>
