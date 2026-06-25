# LocalStoragePreferenceStore

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/persistence/storage.js:18</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Preference store backed by the browser `localStorage` API.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class LocalStoragePreferenceStore {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional storage object, preference key, and unfinished-session key.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Async preference store implementation.</p><span class="helios-api-return-type"><strong>Type</strong> <code>LocalStoragePreferenceStore</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Inject `storage` for tests or app shells that need isolated storage.
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-clear" class="helios-api-member-anchor"></a>

### `clear()` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:42</code></p>
<p>Updates the clear state on the current instance.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-getunfinishedsessionid" class="helios-api-member-anchor"></a>

### `getUnfinishedSessionId(workspaceId = null, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:46</code></p>
<p>Returns the current unfinished session id value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>workspaceId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Value passed to <code>getUnfinishedSessionId</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-setunfinishedsessionid" class="helios-api-member-anchor"></a>

### `setUnfinishedSessionId(id, workspaceId = null)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:57</code></p>
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

<a id="method-unfinishedsessionkeyfor" class="helios-api-member-anchor"></a>

### `unfinishedSessionKeyFor(workspaceId = null)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:25</code></p>
<p>Configures or reads unfinished session key for.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>workspaceId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Value passed to <code>unfinishedSessionKeyFor</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-read" class="helios-api-member-anchor"></a>

### `read()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:30</code></p>
<p>Configures or reads read.</p>
</div>

<a id="method-write" class="helios-api-member-anchor"></a>

### `write(value)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/persistence/storage.js:36</code></p>
<p>Read or set the write setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New write value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current write value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.write(1);
</code></pre>
</div>
