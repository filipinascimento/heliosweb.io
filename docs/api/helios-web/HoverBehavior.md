# HoverBehavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/HoverBehavior.js:34</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in behavior for hover picking and hover labels.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class HoverBehavior extends Behavior {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Hover options including <code>nodeHover</code>, <code>edgeHover</code>, <code>hoverLabel</code>, and connected-edge highlighting.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Behavior that tracks the current hovered node and edge.</p><span class="helios-api-return-type"><strong>Type</strong> <code>HoverBehavior</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Hover requires picking to be available on the active renderer. The
behavior coordinates with `LabelsBehavior` when transient hover labels are
enabled.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:35</code></p>
<p>Id exposed by the class.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-getpublicstate" class="helios-api-member-anchor"></a>

### `getPublicState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:179</code></p>
<p>Returns the current public state value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getPublicState();
</code></pre>
</div>

<a id="method-ensurestatestyledefaults" class="helios-api-member-anchor"></a>

### `ensureStateStyleDefaults()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:183</code></p>
<p>Configures or reads ensure state style defaults.</p>
</div>

<a id="method-applyotherelementsstate" class="helios-api-member-anchor"></a>

### `applyOtherElementsState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:203</code></p>
<p>Updates the other elements state state on the current instance.</p>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-attach" class="helios-api-member-anchor"></a>

### `attach(context)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:62</code></p>
<p>Configures or reads attach.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>attach</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-serialize" class="helios-api-member-anchor"></a>

### `serialize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:147</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:166</code></p>
<p>Updates the restore state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>restore</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-handlenetworkreplaced" class="helios-api-member-anchor"></a>

### `handleNetworkReplaced()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:257</code></p>
<p>Configures or reads handle network replaced.</p>
</div>

## Appearance { #api-appearance .helios-api-section-title }

<p class="helios-api-section-description">Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.</p>

<a id="method-applyhoverlabelconfig" class="helios-api-member-anchor"></a>

### `applyHoverLabelConfig()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:187</code></p>
<p>Updates the hover label config state on the current instance.</p>
</div>

<a id="method-resolvehoverlabelvalue" class="helios-api-member-anchor"></a>

### `resolveHoverLabelValue(index, network = this.context?.network ?? null)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:211</code></p>
<p>Configures or reads resolve hover label value.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node, edge, or attribute index.</td></tr>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>this.context?.network ?? null</code></td><td class="helios-api-param-description">Network instance to read from or mutate.</td></tr>
</tbody>
</table>
</div>

## Rendering And Picking { #api-rendering-and-picking .helios-api-section-title }

<p class="helios-api-section-description">Render requests, picking, framebuffer inspection, and attribute tracking. <a href="HoverBehavior.md">HoverBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> use these lower-level hooks.</p>

<a id="method-syncpicking" class="helios-api-member-anchor"></a>

### `syncPicking()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:207</code></p>
<p>Configures or reads sync picking.</p>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-clearnodehover" class="helios-api-member-anchor"></a>

### `clearNodeHover(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:215</code></p>
<p>Read or set the clear node hover setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current clear node hover value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.clearNodeHover({
  enabled: true,
});
</code></pre>
</div>

<a id="method-clearedgehover" class="helios-api-member-anchor"></a>

### `clearEdgeHover(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:223</code></p>
<p>Read or set the clear edge hover setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current clear edge hover value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.clearEdgeHover({
  enabled: true,
});
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-detach" class="helios-api-member-anchor"></a>

### `detach()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:89</code></p>
<p>Manages detach for the current instance.</p>
</div>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:102</code></p>
<p>Read or set the update setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current update value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.update({
  enabled: true,
});
</code></pre>
</div>

<a id="method-emitchange" class="helios-api-member-anchor"></a>

### `emitChange(reason, detail = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:175</code></p>
<p>Configures or reads emit change.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>detail</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Event payload passed to listeners.</td></tr>
</tbody>
</table>
</div>

<a id="method-applyhoverconnectededges" class="helios-api-member-anchor"></a>

### `applyHoverConnectedEdges()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:191</code></p>
<p>Updates the hover connected edges state on the current instance.</p>
</div>

<a id="method-applyhighlightconnectededges" class="helios-api-member-anchor"></a>

### `applyHighlightConnectedEdges()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:195</code></p>
<p>Updates the highlight connected edges state on the current instance.</p>
</div>

<a id="method-applyhoverstylepolicy" class="helios-api-member-anchor"></a>

### `applyHoverStylePolicy()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:199</code></p>
<p>Updates the hover style policy state on the current instance.</p>
</div>

<a id="method-handlenodehover" class="helios-api-member-anchor"></a>

### `handleNodeHover(event)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:231</code></p>
<p>Configures or reads handle node hover.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>event</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>handleNodeHover</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-handleedgehover" class="helios-api-member-anchor"></a>

### `handleEdgeHover(event)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:244</code></p>
<p>Configures or reads handle edge hover.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>event</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>handleEdgeHover</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-handleuibindingchange" class="helios-api-member-anchor"></a>

### `handleUiBindingChange(event)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:277</code></p>
<p>Configures or reads handle ui binding change.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>event</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>handleUiBindingChange</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-handlehighlightchange" class="helios-api-member-anchor"></a>

### `handleHighlightChange()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/HoverBehavior.js:284</code></p>
<p>Configures or reads handle highlight change.</p>
</div>
