# LegendsBehavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/LegendsBehavior.js:109</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in behavior for legend overlays.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class LegendsBehavior extends Behavior {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Legend visibility, placement, typography, scale, title, and export compatibility options.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Behavior controlling SVG legends for mapper and density channels.</p><span class="helios-api-return-type"><strong>Type</strong> <code>LegendsBehavior</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Legends read mapper and density configuration from the live Helios
instance and preserve serializable placement, title, and visibility state.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:110</code></p>
<p>Id exposed by the class.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-getpublicstate" class="helios-api-member-anchor"></a>

### `getPublicState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:269</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:122</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:166</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:262</code></p>
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

<a id="method-getlegenditems" class="helios-api-member-anchor"></a>

### `getLegendItems(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:298</code></p>
<p>Read or set the get legend items setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current get legend items value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.getLegendItems({
  enabled: true,
});
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {}, changeOptions = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:144</code></p>
<p>Configures or reads update.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>changeOptions</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>update</code>.</td></tr>
</tbody>
</table>
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

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:172</code></p>
<p>Configures or reads state entries.</p>
</div>

<a id="method-emitchange" class="helios-api-member-anchor"></a>

### `emitChange(reason, detail = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:273</code></p>
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

<a id="method-legends" class="helios-api-member-anchor"></a>

### `legends(options)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:277</code></p>
<p>Read or set the legends setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current legends value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.legends({
  enabled: true,
});
</code></pre>
</div>

<a id="method-enabled" class="helios-api-member-anchor"></a>

### `enabled(value)` &rarr; &#123;boolean|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:283</code></p>
<p>Read or set the enabled setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New enabled value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current enabled value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.enabled(true);
</code></pre>
</div>

<a id="method-titles" class="helios-api-member-anchor"></a>

### `titles(value)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:288</code></p>
<p>Read or set the titles setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New titles value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current titles value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.titles(1);
</code></pre>
</div>

<a id="method-placements" class="helios-api-member-anchor"></a>

### `placements(value)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:293</code></p>
<p>Read or set the placements setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New placements value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current placements value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.placements(1);
</code></pre>
</div>

<a id="method-applyconfig" class="helios-api-member-anchor"></a>

### `applyConfig({ silent = false } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LegendsBehavior.js:312</code></p>
<p>Updates the config state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>silent</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false } = {}</code></td><td class="helios-api-param-description">Value passed to <code>applyConfig</code>.</td></tr>
</tbody>
</table>
</div>
