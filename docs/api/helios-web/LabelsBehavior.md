# LabelsBehavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/LabelsBehavior.js:108</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in behavior for SVG label overlays.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class LabelsBehavior extends Behavior {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Label options including <code>enabled</code>, <code>source</code>, <code>selectionMode</code>, <code>maxVisible</code>, collision settings, font settings, and export compatibility flags.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Behavior controlling the live label overlay.</p><span class="helios-api-return-type"><strong>Type</strong> <code>LabelsBehavior</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Labels can be driven by a node attribute, callback, selection state,
hover state, and screen-space collision/ranking limits.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:109</code></p>
<p>Id exposed by the class.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-getpublicstate" class="helios-api-member-anchor"></a>

### `getPublicState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:351</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:123</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:153</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:344</code></p>
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

## Camera And View { #api-camera-and-view .helios-api-section-title }

<p class="helios-api-section-description">Camera framing, target following, dimensional mode, and transitions. <a href="InterfaceBehavior.md">InterfaceBehavior</a> can expose these controls.</p>

<a id="method-mode" class="helios-api-member-anchor"></a>

### `mode(value, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:385</code></p>
<p>Configures or reads mode.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New mode value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.mode(&#x27;auto&#x27;);
</code></pre>
</div>

## Appearance { #api-appearance .helios-api-section-title }

<p class="helios-api-section-description">Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.</p>

<a id="method-fontsizescale" class="helios-api-member-anchor"></a>

### `fontSizeScale(value)` &rarr; &#123;number|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:408</code></p>
<p>Read or set the font size scale setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New font size scale value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current font size scale value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.fontSizeScale(1);
</code></pre>
</div>

<a id="method-outlinewidth" class="helios-api-member-anchor"></a>

### `outlineWidth(value)` &rarr; &#123;number|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:422</code></p>
<p>Read or set the outline width setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New outline width value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current outline width value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.outlineWidth(1);
</code></pre>
</div>

<a id="method-outlinecolor" class="helios-api-member-anchor"></a>

### `outlineColor(value)` &rarr; &#123;string|Array&lt;number&gt;|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:462</code></p>
<p>Read or set the outline color setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New outline color value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current outline color value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.outlineColor(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-sethoverpolicy" class="helios-api-member-anchor"></a>

### `setHoverPolicy({ enabled = false, source = null } = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:487</code></p>
<p>Set the hover policy setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>enabled</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Value passed to <code>setHoverPolicy</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>source</code></td><td class="helios-api-param-type"><code>Blob</code>|<code>ArrayBuffer</code>|<code>string</code>|<code>File</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null } = {}</code></td><td class="helios-api-param-description">Network or input source used by the operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-clearhoverpolicy" class="helios-api-member-anchor"></a>

### `clearHoverPolicy(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:497</code></p>
<p>Read or set the clear hover policy setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current clear hover policy value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.clearHoverPolicy({
  enabled: true,
});
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {}, changeOptions = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:135</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:159</code></p>
<p>Configures or reads state entries.</p>
</div>

<a id="method-emitchange" class="helios-api-member-anchor"></a>

### `emitChange(reason, detail = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:360</code></p>
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

<a id="method-labels" class="helios-api-member-anchor"></a>

### `labels(options)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:364</code></p>
<p>Read or set the labels setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current labels value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labels({
  enabled: true,
});
</code></pre>
</div>

<a id="method-enabled" class="helios-api-member-anchor"></a>

### `enabled(value, options = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:380</code></p>
<p>Configures or reads enabled.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New enabled value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.enabled(true);
</code></pre>
</div>

<a id="method-selectedonlyspaceaware" class="helios-api-member-anchor"></a>

### `selectedOnlySpaceAware(value)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:398</code></p>
<p>Read or set the selected only space aware setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New selected only space aware value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current selected only space aware value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.selectedOnlySpaceAware(1);
</code></pre>
</div>

<a id="method-maxvisible" class="helios-api-member-anchor"></a>

### `maxVisible(value)` &rarr; &#123;number|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:403</code></p>
<p>Read or set the max visible setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New max visible value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current max visible value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.maxVisible(1);
</code></pre>
</div>

<a id="method-minscreenradius" class="helios-api-member-anchor"></a>

### `minScreenRadius(value)` &rarr; &#123;number|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:415</code></p>
<p>Read or set the min screen radius setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New min screen radius value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current min screen radius value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.minScreenRadius(1);
</code></pre>
</div>

<a id="method-offsetradiusfactor" class="helios-api-member-anchor"></a>

### `offsetRadiusFactor(value)` &rarr; &#123;number|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:429</code></p>
<p>Read or set the offset radius factor setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New offset radius factor value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current offset radius factor value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.offsetRadiusFactor(1);
</code></pre>
</div>

<a id="method-offsetpx" class="helios-api-member-anchor"></a>

### `offsetPx(value)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:436</code></p>
<p>Read or set the offset px setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New offset px value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current offset px value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.offsetPx(1);
</code></pre>
</div>

<a id="method-maxchars" class="helios-api-member-anchor"></a>

### `maxChars(value)` &rarr; &#123;number|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:443</code></p>
<p>Read or set the max chars setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New max chars value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current max chars value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.maxChars(1);
</code></pre>
</div>

<a id="method-maxrows" class="helios-api-member-anchor"></a>

### `maxRows(value)` &rarr; &#123;number|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:450</code></p>
<p>Read or set the max rows setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New max rows value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current max rows value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.maxRows(1);
</code></pre>
</div>

<a id="method-fill" class="helios-api-member-anchor"></a>

### `fill(value)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:457</code></p>
<p>Read or set the fill setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New fill value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current fill value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.fill(1);
</code></pre>
</div>

<a id="method-fontfamily" class="helios-api-member-anchor"></a>

### `fontFamily(value)` &rarr; &#123;string|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:467</code></p>
<p>Read or set the font family setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New font family value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current font family value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.fontFamily(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-source" class="helios-api-member-anchor"></a>

### `source(value)` &rarr; &#123;string|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:472</code></p>
<p>Read or set the source setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New source value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current source value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.source(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-applyselectiondefaults" class="helios-api-member-anchor"></a>

### `applySelectionDefaults()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:479</code></p>
<p>Updates the selection defaults state on the current instance.</p>
</div>

<a id="method-applyconfig" class="helios-api-member-anchor"></a>

### `applyConfig({ silent = false } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LabelsBehavior.js:504</code></p>
<p>Updates the config state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>silent</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false } = {}</code></td><td class="helios-api-param-description">Value passed to <code>applyConfig</code>.</td></tr>
</tbody>
</table>
</div>


## Example

<div markdown="1" class="helios-api-template-section">

```js
helios.behavior.labels.update({
  enabled: true,
  source: 'label',
  selectionMode: 'ranked',
  maxVisible: 80,
});
```

</div>
