# SessionStore

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/storage/HeliosStorageManager.js:480</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Low-level session record store used by Helios storage managers.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class SessionStore {
```

</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-get" class="helios-api-member-anchor"></a>

### `get(id, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:627</code></p>
<p>Returns the current get value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>get</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-getall" class="helios-api-member-anchor"></a>

### `getAll()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:672</code></p>
<p>Returns the current all value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getAll();
</code></pre>
</div>

<a id="method-getunfinishedsessionid" class="helios-api-member-anchor"></a>

### `getUnfinishedSessionId(workspaceId = null)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:707</code></p>
<p>Returns the current unfinished session id value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>workspaceId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Value passed to <code>getUnfinishedSessionId</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-setunfinishedsessionid" class="helios-api-member-anchor"></a>

### `setUnfinishedSessionId(id, workspaceId = null)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:713</code></p>
<p>Set the unfinished session id setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setUnfinishedSessionId</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>workspaceId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Value passed to <code>setUnfinishedSessionId</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-key" class="helios-api-member-anchor"></a>

### `key(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:489</code></p>
<p>Configures or reads key.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>key</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-networkdatarecordid" class="helios-api-member-anchor"></a>

### `networkDataRecordId(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:493</code></p>
<p>Configures or reads network data record id.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>networkDataRecordId</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-positiondatarecordid" class="helios-api-member-anchor"></a>

### `positionDataRecordId(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:497</code></p>
<p>Configures or reads position data record id.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>positionDataRecordId</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-unfinishedsessionkeyfor" class="helios-api-member-anchor"></a>

### `unfinishedSessionKeyFor(workspaceId = null)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:501</code></p>
<p>Configures or reads unfinished session key for.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>workspaceId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Value passed to <code>unfinishedSessionKeyFor</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-put" class="helios-api-member-anchor"></a>

### `put(record)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:610</code></p>
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

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:694</code></p>
<p>Configures or reads delete.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>delete</code>.</td></tr>
</tbody>
</table>
</div>
