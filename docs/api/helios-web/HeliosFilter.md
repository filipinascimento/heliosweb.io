# HeliosFilter

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/filters/HeliosFilter.js:227</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Builder for reusable graph filter rule sets.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class HeliosFilter {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Filter id, display name, graph scope, and initial rules.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Filter model that can be activated through <code>helios.activateHeliosFilter(...)</code> or <code>FilterBehavior</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/HeliosFilter/"><code>HeliosFilter</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Rules compile to Helios Network query expressions. Supported rule
types are `numeric`, `categorical`, `string`, and raw `query`.
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-tographfilteroptions" class="helios-api-member-anchor"></a>

### `toGraphFilterOptions()` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:427</code></p>
<p>Convert this model to the graph-filter options consumed by <code>Helios</code>.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Graph-filter options with node and edge query strings.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setscope" class="helios-api-member-anchor"></a>

### `setScope(scope)` &rarr; &#123;HeliosFilter&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:270</code></p>
<p>Set the graph filter scope.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type">&#x27;<code>render</code>&#x27;|&#x27;<code>render</code>+<code>layout</code>&#x27;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Graph filter scope.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This filter.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/HeliosFilter/"><code>HeliosFilter</code></a></span></div>
</div>

<a id="method-getscope" class="helios-api-member-anchor"></a>

### `getScope()` &rarr; &#123;&#x27;render&#x27;|&#x27;render+layout&#x27;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:280</code></p>
<p>Return the graph filter scope.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current graph filter scope.</p><span class="helios-api-return-type"><strong>Type</strong> &#x27;<code>render</code>&#x27;|&#x27;<code>render</code>+<code>layout</code>&#x27;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getScope();
</code></pre>
</div>

<a id="method-getrules" class="helios-api-member-anchor"></a>

### `getRules(scope = null)` &rarr; &#123;Array.&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:290</code></p>
<p>Return copied rules, optionally limited to node or edge rules.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type">&#x27;<code>node</code>&#x27;|&#x27;<code>edge</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional rule scope.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Copied rule descriptors.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>.&lt;<code>Object</code>&gt;</span></div>
</div>

<a id="method-clear" class="helios-api-member-anchor"></a>

### `clear(scope = null)` &rarr; &#123;HeliosFilter&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:379</code></p>
<p>Remove all rules, or all rules for one node/edge scope.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type">&#x27;<code>node</code>&#x27;|&#x27;<code>edge</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional rule scope to clear.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This filter.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/HeliosFilter/"><code>HeliosFilter</code></a></span></div>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-clone" class="helios-api-member-anchor"></a>

### `clone()` &rarr; &#123;HeliosFilter&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:255</code></p>
<p>Return a deep copy of this filter model.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Independent filter with copied rule descriptors.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/HeliosFilter/"><code>HeliosFilter</code></a></span></div>
</div>

<a id="method-addrule" class="helios-api-member-anchor"></a>

### `addRule(rule)` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:320</code></p>
<p>Add a filter rule.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>rule</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Rule descriptor.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Normalized copied rule descriptor.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

<a id="method-updaterule" class="helios-api-member-anchor"></a>

### `updateRule(ruleId, patch = {})` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:334</code></p>
<p>Update an existing rule by id.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>ruleId</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Rule id to update.</td></tr>
<tr><td class="helios-api-param-name"><code>patch</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Rule fields to replace.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Normalized copied rule descriptor.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

<a id="method-upsertrule" class="helios-api-member-anchor"></a>

### `upsertRule(rule)` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:352</code></p>
<p>Update a rule by id when it exists, otherwise add it.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>rule</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Rule descriptor.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Normalized copied rule descriptor.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

<a id="method-removerule" class="helios-api-member-anchor"></a>

### `removeRule(ruleId)` &rarr; &#123;boolean&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:366</code></p>
<p>Remove a rule by id.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>ruleId</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Rule id to remove.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>True when a rule was removed.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code></span></div>
</div>

<a id="method-compilescopequery" class="helios-api-member-anchor"></a>

### `compileScopeQuery(scope)` &rarr; &#123;string|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:397</code></p>
<p>Compile active rules for one node/edge scope into a query string.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type">&#x27;<code>node</code>&#x27;|&#x27;<code>edge</code>&#x27;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Rule scope to compile.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Query expression, or <code>null</code> when no active criteria apply.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<code>null</code></span></div>
</div>

<a id="method-hascriteria" class="helios-api-member-anchor"></a>

### `hasCriteria()` &rarr; &#123;boolean&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/filters/HeliosFilter.js:418</code></p>
<p>Test whether this filter has any active criteria.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>True when at least one rule compiles to a query.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.hasCriteria();
</code></pre>
</div>


## Example

<div markdown="1" class="helios-api-template-section">

```js
const filter = new HeliosFilter({ scope: 'render' })
  .addRule({ type: 'numeric', scope: 'node', attribute: 'score', min: 0.5, max: 1 });
```

</div>
