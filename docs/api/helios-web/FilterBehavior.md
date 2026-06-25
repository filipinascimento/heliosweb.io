# FilterBehavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/FilterBehavior.js:50</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in behavior for graph filtering.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class FilterBehavior extends Behavior {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<a href="/docs/api/helios-web/HeliosFilter/"><code>HeliosFilter</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Filter model or rule options for numeric, categorical, string, and query rules.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Behavior that applies render-only or render-plus-layout filtered graph views.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/FilterBehavior/"><code>FilterBehavior</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
`scope: "render"` keeps the layout topology intact; `scope:
"render+layout"` rebuilds the active graph view used by both rendering and
dynamic layouts.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:51</code></p>
<p>Id exposed by the class.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-getpublicstate" class="helios-api-member-anchor"></a>

### `getPublicState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:179</code></p>
<p>Returns the current public state value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getPublicState();
</code></pre>
</div>

<a id="method-replacerules" class="helios-api-member-anchor"></a>

### `replaceRules({ nodeRules = [], edgeRules = [], scope } = {})` &rarr; &#123;FilterBehavior&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:217</code></p>
<p>Replace all active node and edge filter rules.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Replacement filter options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.nodeRules"><span aria-hidden="true">|</span><code>nodeRules</code></span></td><td class="helios-api-param-type"><code>Array</code>.&lt;<code>Object</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node rules to apply.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.edgeRules"><span aria-hidden="true">|</span><code>edgeRules</code></span></td><td class="helios-api-param-type"><code>Array</code>.&lt;<code>Object</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge rules to apply.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.scope"><span aria-hidden="true">|</span><code>scope</code></span></td><td class="helios-api-param-type">&#x27;<code>render</code>&#x27;|&#x27;<code>render</code>+<code>layout</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Filter scope.</td></tr>
<tr><td class="helios-api-param-name"><code>nodeRules</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>[]</code></td><td class="helios-api-param-description">Value passed to <code>replaceRules</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>edgeRules</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>[]</code></td><td class="helios-api-param-description">Value passed to <code>replaceRules</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Attribute scope: node, edge, or network.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This behavior instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/FilterBehavior/"><code>FilterBehavior</code></a></span></div>
<h4>Notes</h4>
<p><code>render+layout</code> changes the graph view consumed by dynamic layouts. Use <code>render</code> when hiding items should not change layout forces.</p>
</div>

<a id="method-clear" class="helios-api-member-anchor"></a>

### `clear()` &rarr; &#123;FilterBehavior&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:234</code></p>
<p>Remove the active graph filter and restore the unfiltered render view.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This behavior instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/FilterBehavior/"><code>FilterBehavior</code></a></span></div>
</div>

<a id="method-setfiltermodel" class="helios-api-member-anchor"></a>

### `setFilterModel(model, { reason = 'model', trackOverride = true } = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:255</code></p>
<p>Set the filter model setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>model</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setFilterModel</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;model&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>trackOverride</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true } = {}</code></td><td class="helios-api-param-description">Value passed to <code>setFilterModel</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-attach" class="helios-api-member-anchor"></a>

### `attach(context)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:60</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:92</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:161</code></p>
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

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-getmodel" class="helios-api-member-anchor"></a>

### `getModel()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:187</code></p>
<p>Returns the current model value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getModel();
</code></pre>
</div>

<a id="method-setscope" class="helios-api-member-anchor"></a>

### `setScope(scope)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:198</code></p>
<p>Set the scope setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute scope: node, edge, or network.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:75</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:105</code></p>
<p>Configures or reads state entries.</p>
</div>

<a id="method-emitchange" class="helios-api-member-anchor"></a>

### `emitChange(reason, detail = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:175</code></p>
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

<a id="method-filters" class="helios-api-member-anchor"></a>

### `filters(options)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:191</code></p>
<p>Read or set the filters setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current filters value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.filters({
  enabled: true,
});
</code></pre>
</div>

<a id="method-syncfromhelios" class="helios-api-member-anchor"></a>

### `syncFromHelios({ preferActiveModel = false, silent = false } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/FilterBehavior.js:275</code></p>
<p>Configures or reads sync from helios.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>preferActiveModel</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Value passed to <code>syncFromHelios</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>silent</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false } = {}</code></td><td class="helios-api-param-description">Value passed to <code>syncFromHelios</code>.</td></tr>
</tbody>
</table>
</div>
