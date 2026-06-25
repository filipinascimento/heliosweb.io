# VisualAttributes

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/pipeline/VisualAttributes.js:166</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Ensures required visual attributes exist on the Helios network, seeds defaults, and provides helpers to apply mappers into sparse buffers.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class VisualAttributes {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
<tr><td class="helios-api-param-name"><code>debug</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>constructor</code>.</td></tr>
</tbody>
</table>
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-nodepositions" class="helios-api-member-anchor"></a>

### `nodePositions`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:181</code></p>
<p>Node positions exposed by the class.</p>
</div>

<a id="property-nodecolors" class="helios-api-member-anchor"></a>

### `nodeColors`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:185</code></p>
<p>Node colors exposed by the class.</p>
</div>

<a id="property-nodesizes" class="helios-api-member-anchor"></a>

### `nodeSizes`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:189</code></p>
<p>Node sizes exposed by the class.</p>
</div>

<a id="property-nodestates" class="helios-api-member-anchor"></a>

### `nodeStates`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:193</code></p>
<p>Node states exposed by the class.</p>
</div>

<a id="property-nodeoutlinewidths" class="helios-api-member-anchor"></a>

### `nodeOutlineWidths`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:197</code></p>
<p>Node outline widths exposed by the class.</p>
</div>

<a id="property-nodeoutlinecolors" class="helios-api-member-anchor"></a>

### `nodeOutlineColors`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:201</code></p>
<p>Node outline colors exposed by the class.</p>
</div>

<a id="property-edgecolors" class="helios-api-member-anchor"></a>

### `edgeColors`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:205</code></p>
<p>Edge colors exposed by the class.</p>
</div>

<a id="property-edgewidths" class="helios-api-member-anchor"></a>

### `edgeWidths`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:209</code></p>
<p>Edge widths exposed by the class.</p>
</div>

<a id="property-edgeopacities" class="helios-api-member-anchor"></a>

### `edgeOpacities`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:213</code></p>
<p>Edge opacities exposed by the class.</p>
</div>

<a id="property-edgestates" class="helios-api-member-anchor"></a>

### `edgeStates`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:217</code></p>
<p>Edge states exposed by the class.</p>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-setnetworkvisualconfig" class="helios-api-member-anchor"></a>

### `setNetworkVisualConfig(config)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:341</code></p>
<p>Set the network visual config setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setNetworkVisualConfig</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-markpositionsdirty" class="helios-api-member-anchor"></a>

### `markPositionsDirty()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:740</code></p>
<p>Configures or reads mark positions dirty.</p>
</div>

<a id="method-seedmissingpositions" class="helios-api-member-anchor"></a>

### `seedMissingPositions(bounds = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:845</code></p>
<p>Seeds missing node positions with random values so downstream layouts/renderers always have finite coordinates to start with.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>bounds</code></td><td class="helios-api-param-type">{<code>width</code>?: <code>number</code>, <code>height</code>?: <code>number</code>, <code>depth</code>?: <code>number</code>, <code>mode</code>?: <code>string</code>, <code>center</code>?: <code>number</code>[]}</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
</tbody>
</table>
</div>

## Mappers { #api-mappers .helios-api-section-title }

<p class="helios-api-section-description">Mapper configuration for node and edge visual channels. <a href="MappersBehavior.md">MappersBehavior</a> handles mapper UI state.</p>

<a id="method-applymappers" class="helios-api-member-anchor"></a>

### `applyMappers({ nodeMapper, edgeMapper } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:327</code></p>
<p>Updates the mappers state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeMapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>applyMappers</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>edgeMapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>applyMappers</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-applynodemapper" class="helios-api-member-anchor"></a>

### `applyNodeMapper(mapper, visualConfig)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:504</code></p>
<p>Updates the node mapper state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>applyNodeMapper</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>visualConfig</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>applyNodeMapper</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-applyedgemapper" class="helios-api-member-anchor"></a>

### `applyEdgeMapper(mapper, visualConfig)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:562</code></p>
<p>Updates the edge mapper state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>applyEdgeMapper</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>visualConfig</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>applyEdgeMapper</code>.</td></tr>
</tbody>
</table>
</div>

## Appearance { #api-appearance .helios-api-section-title }

<p class="helios-api-section-description">Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.</p>

<a id="method-seedmissingedgeopacity" class="helios-api-member-anchor"></a>

### `seedMissingEdgeOpacity()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:300</code></p>
<p>When networks are populated before Helios is created, edge opacity buffers start at zero which hides edges entirely. Seed a reasonable default for any active edge that still has an uninitialized (zero/invalid) opacity.</p>
</div>

<a id="method-resolveedgecolorpair" class="helios-api-member-anchor"></a>

### `resolveEdgeColorPair(value)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1359</code></p>
<p>Read or set the resolve edge color pair setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New resolve edge color pair value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current resolve edge color pair value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.resolveEdgeColorPair(1);
</code></pre>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-getnodeattributeview" class="helios-api-member-anchor"></a>

### `getNodeAttributeView(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:221</code></p>
<p>Returns the current node attribute view value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-getedgeattributeview" class="helios-api-member-anchor"></a>

### `getEdgeAttributeView(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:226</code></p>
<p>Returns the current edge attribute view value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-getpreparednodeattributeview" class="helios-api-member-anchor"></a>

### `getPreparedNodeAttributeView(prepared, name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:277</code></p>
<p>Returns the current prepared node attribute view value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>prepared</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>getPreparedNodeAttributeView</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-getpreparededgeattributeview" class="helios-api-member-anchor"></a>

### `getPreparedEdgeAttributeView(prepared, name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:286</code></p>
<p>Returns the current prepared edge attribute view value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>prepared</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>getPreparedEdgeAttributeView</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-normalizelookupname" class="helios-api-member-anchor"></a>

### `normalizeLookupName(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:231</code></p>
<p>Configures or reads normalize lookup name.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-preparenodeattributelookups" class="helios-api-member-anchor"></a>

### `prepareNodeAttributeLookups(names, { allowMissing = false } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:235</code></p>
<p>Configures or reads prepare node attribute lookups.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>names</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>prepareNodeAttributeLookups</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>allowMissing</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false } = {}</code></td><td class="helios-api-param-description">Value passed to <code>prepareNodeAttributeLookups</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-prepareedgeattributelookups" class="helios-api-member-anchor"></a>

### `prepareEdgeAttributeLookups(names, { allowMissing = false } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:256</code></p>
<p>Configures or reads prepare edge attribute lookups.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>names</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>prepareEdgeAttributeLookups</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>allowMissing</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false } = {}</code></td><td class="helios-api-param-description">Value passed to <code>prepareEdgeAttributeLookups</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-buildvisualconstantconfig" class="helios-api-member-anchor"></a>

### `buildVisualConstantConfig({ nodeMapper, edgeMapper } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:350</code></p>
<p>Configures or reads build visual constant config.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeMapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>buildVisualConstantConfig</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>edgeMapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>buildVisualConstantConfig</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-buildnodeconstantconfig" class="helios-api-member-anchor"></a>

### `buildNodeConstantConfig(mapper)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:358</code></p>
<p>Configures or reads build node constant config.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>buildNodeConstantConfig</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-buildedgeconstantconfig" class="helios-api-member-anchor"></a>

### `buildEdgeConstantConfig(mapper, nodeConfig = null)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:379</code></p>
<p>Configures or reads build edge constant config.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>buildEdgeConstantConfig</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>nodeConfig</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Value passed to <code>buildEdgeConstantConfig</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-augmentedgesourceconfig" class="helios-api-member-anchor"></a>

### `augmentEdgeSourceConfig(edgeConfig, mapper)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:422</code></p>
<p>Configures or reads augment edge source config.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>edgeConfig</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>augmentEdgeSourceConfig</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>mapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>augmentEdgeSourceConfig</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-ensurevisualattributesforconfig" class="helios-api-member-anchor"></a>

### `ensureVisualAttributesForConfig({ nodeMapper, edgeMapper, visualConfig } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:634</code></p>
<p>Configures or reads ensure visual attributes for config.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeMapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>ensureVisualAttributesForConfig</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>edgeMapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>ensureVisualAttributesForConfig</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>visualConfig</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>ensureVisualAttributesForConfig</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-ensureattributes" class="helios-api-member-anchor"></a>

### `ensureAttributes()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:683</code></p>
<p>Configures or reads ensure attributes.</p>
</div>

<a id="method-bumpnodeattributes" class="helios-api-member-anchor"></a>

### `bumpNodeAttributes(...names)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:689</code></p>
<p>Configures or reads bump node attributes.</p>
</div>

<a id="method-bumpedgeattributes" class="helios-api-member-anchor"></a>

### `bumpEdgeAttributes(...names)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:715</code></p>
<p>Configures or reads bump edge attributes.</p>
</div>

<a id="method-applynodedefaults" class="helios-api-member-anchor"></a>

### `applyNodeDefaults(indices)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:748</code></p>
<p>Initializes basic node visuals. Can be re-used whenever nodes are added.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Iterable</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.applyNodeDefaults([0, 1, 2]);
</code></pre>
</div>

<a id="method-applyedgedefaults" class="helios-api-member-anchor"></a>

### `applyEdgeDefaults(indices)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:805</code></p>
<p>Initializes basic edge visuals. Can be re-used whenever edges are added.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Iterable</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.applyEdgeDefaults([0, 1, 2]);
</code></pre>
</div>

<a id="method-ensurenodeattribute" class="helios-api-member-anchor"></a>

### `ensureNodeAttribute(name, type, dimension)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:951</code></p>
<p>Configures or reads ensure node attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute value type.</td></tr>
<tr><td class="helios-api-param-name"><code>dimension</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Element width or memory-stride setting.</td></tr>
</tbody>
</table>
</div>

<a id="method-ensureedgeattribute" class="helios-api-member-anchor"></a>

### `ensureEdgeAttribute(name, type, dimension)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1013</code></p>
<p>Configures or reads ensure edge attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute value type.</td></tr>
<tr><td class="helios-api-param-name"><code>dimension</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Element width or memory-stride setting.</td></tr>
</tbody>
</table>
</div>

<a id="method-ensurenodetoedgeattribute" class="helios-api-member-anchor"></a>

### `ensureNodeToEdgeAttribute(sourceName, edgeName, sourceDimension)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1075</code></p>
<p>Configures or reads ensure node to edge attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>sourceName</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
<tr><td class="helios-api-param-name"><code>edgeName</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
<tr><td class="helios-api-param-name"><code>sourceDimension</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>ensureNodeToEdgeAttribute</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-collectattributenames" class="helios-api-member-anchor"></a>

### `collectAttributeNames(mapper, mode)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1133</code></p>
<p>Configures or reads collect attribute names.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>collectAttributeNames</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mode for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-resolvenodeattributebuffers" class="helios-api-member-anchor"></a>

### `resolveNodeAttributeBuffers(names)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1159</code></p>
<p>Configures or reads resolve node attribute buffers.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>names</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolveNodeAttributeBuffers</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-resolveedgeattributebuffers" class="helios-api-member-anchor"></a>

### `resolveEdgeAttributeBuffers(names)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1179</code></p>
<p>Configures or reads resolve edge attribute buffers.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>names</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolveEdgeAttributeBuffers</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-buildattributeobject" class="helios-api-member-anchor"></a>

### `buildAttributeObject(buffers, index)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1198</code></p>
<p>Configures or reads build attribute object.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>buffers</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>buildAttributeObject</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node, edge, or attribute index.</td></tr>
</tbody>
</table>
</div>

<a id="method-buildedgeattributeobject" class="helios-api-member-anchor"></a>

### `buildEdgeAttributeObject(buffers, edgeId)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1218</code></p>
<p>Configures or reads build edge attribute object.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>buffers</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>buildEdgeAttributeObject</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>edgeId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>buildEdgeAttributeObject</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-writenodevisuals" class="helios-api-member-anchor"></a>

### `writeNodeVisuals(nodeId, mapped, visuals)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1222</code></p>
<p>Configures or reads write node visuals.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node or edge identifiers/indices used by the operation.</td></tr>
<tr><td class="helios-api-param-name"><code>mapped</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeNodeVisuals</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>visuals</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeNodeVisuals</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-writeedgevisuals" class="helios-api-member-anchor"></a>

### `writeEdgeVisuals(edgeId, mapped, visuals)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1255</code></p>
<p>Configures or reads write edge visuals.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>edgeId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeEdgeVisuals</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>mapped</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeEdgeVisuals</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>visuals</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeEdgeVisuals</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-torgba" class="helios-api-member-anchor"></a>

### `toRgba(value)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1291</code></p>
<p>Read or set the to rgba setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New to rgba value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current to rgba value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.toRgba(1);
</code></pre>
</div>

<a id="method-resolveedgescalarpair" class="helios-api-member-anchor"></a>

### `resolveEdgeScalarPair(value)` &rarr; &#123;boolean|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1380</code></p>
<p>Read or set the resolve edge scalar pair setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New resolve edge scalar pair value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current resolve edge scalar pair value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.resolveEdgeScalarPair(true);
</code></pre>
</div>

<a id="method-writeedgedefaults" class="helios-api-member-anchor"></a>

### `writeEdgeDefaults(index, color, width, opacity, colorView, widthView, opacityView)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1454</code></p>
<p>Configures or reads write edge defaults.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node, edge, or attribute index.</td></tr>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New write edge defaults value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>width</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeEdgeDefaults</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>opacity</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeEdgeDefaults</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>colorView</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeEdgeDefaults</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>widthView</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeEdgeDefaults</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>opacityView</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>writeEdgeDefaults</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-withbufferaccess" class="helios-api-member-anchor"></a>

### `withBufferAccess(fn)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1481</code></p>
<p>Configures or reads with buffer access.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>fn</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>withBufferAccess</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-flushpendingattributebumps" class="helios-api-member-anchor"></a>

### `flushPendingAttributeBumps()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/VisualAttributes.js:1501</code></p>
<p>Configures or reads flush pending attribute bumps.</p>
</div>
