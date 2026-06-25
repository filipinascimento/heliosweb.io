# AppearanceBehavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/AppearanceBehavior.js:463</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in behavior for global visual appearance and render quality.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class AppearanceBehavior extends Behavior {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Background, node/edge scale and opacity, shading, ambient occlusion, and adaptive edge quality options.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Behavior that keeps appearance settings serializable and synchronized with UI bindings.</p><span class="helios-api-return-type"><strong>Type</strong> <code>AppearanceBehavior</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Renderer capability affects some appearance options. Query
`supportsAmbientOcclusion()` after `await helios.ready` before exposing
ambient-occlusion controls.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:464</code></p>
<p>Id exposed by the class.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-getpublicstate" class="helios-api-member-anchor"></a>

### `getPublicState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:634</code></p>
<p>Returns the current public state value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getPublicState();
</code></pre>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-attach" class="helios-api-member-anchor"></a>

### `attach(context)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:473</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:504</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:618</code></p>
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

## Appearance { #api-appearance .helios-api-section-title }

<p class="helios-api-section-description">Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.</p>

<a id="method-supportsambientocclusion" class="helios-api-member-anchor"></a>

### `supportsAmbientOcclusion()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:630</code></p>
<p>Configures or reads supports ambient occlusion.</p>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:494</code></p>
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

<a id="method-stateentries" class="helios-api-member-anchor"></a>

### `stateEntries()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:510</code></p>
<p>Configures or reads state entries.</p>
</div>

<a id="method-appearance" class="helios-api-member-anchor"></a>

### `appearance(options)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:625</code></p>
<p>Read or set the appearance setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current appearance value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.appearance({
  enabled: true,
});
</code></pre>
</div>

<a id="method-emitchange" class="helios-api-member-anchor"></a>

### `emitChange(reason, detail = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/AppearanceBehavior.js:638</code></p>
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
