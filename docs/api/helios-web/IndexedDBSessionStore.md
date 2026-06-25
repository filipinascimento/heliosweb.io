# IndexedDBSessionStore

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/persistence/storage.js:92</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Session store backed by IndexedDB.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class IndexedDBSessionStore {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional IndexedDB factory, database name, object store name, and schema version.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Async session store implementation.</p><span class="helios-api-return-type"><strong>Type</strong> <code>IndexedDBSessionStore</code></span></div>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-get" class="helios-api-member-anchor"></a>

### `get(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:130</code></p>
<p>Returns the current get value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>get</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-getall" class="helios-api-member-anchor"></a>

### `getAll()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:138</code></p>
<p>Returns the current all value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getAll();
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-put" class="helios-api-member-anchor"></a>

### `put(record)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:120</code></p>
<p>Configures or reads put.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>record</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>put</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-delete" class="helios-api-member-anchor"></a>

### `delete(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:162</code></p>
<p>Configures or reads delete.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>delete</code>.</td></tr>
</tbody>
</table>
</div>
