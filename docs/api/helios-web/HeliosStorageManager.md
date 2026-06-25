# HeliosStorageManager

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/storage/HeliosStorageManager.js:729</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Base storage facade for Helios state snapshots, sessions, and portable network state.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class HeliosStorageManager extends EventTarget {
```

</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-destroy" class="helios-api-member-anchor"></a>

### `destroy()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2907</code></p>
<p>Manages destroy for the current instance.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-pendingstatechangecount" class="helios-api-member-anchor"></a>

### `pendingStateChangeCount()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1500</code></p>
<p>Configures or reads pending state change count.</p>
</div>

<a id="method-haspendingstatechanges" class="helios-api-member-anchor"></a>

### `hasPendingStateChanges()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1504</code></p>
<p>Returns the current pending state changes value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.hasPendingStateChanges();
</code></pre>
</div>

<a id="method-recordportablestate" class="helios-api-member-anchor"></a>

### `recordPortableState(path, value, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1829</code></p>
<p>Configures or reads record portable state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>path</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Filesystem path to read from or write to.</td></tr>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New record portable state value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-restoreportablestatefromnetwork" class="helios-api-member-anchor"></a>

### `restorePortableStateFromNetwork(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2831</code></p>
<p>Read or set the restore portable state from network setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current restore portable state from network value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.restorePortableStateFromNetwork({
  enabled: true,
});
</code></pre>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-loadpreferences" class="helios-api-member-anchor"></a>

### `loadPreferences()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:989</code></p>
<p>Handles preferences for the current graph or visualization state.</p>
</div>

<a id="method-marknetworkdirty" class="helios-api-member-anchor"></a>

### `markNetworkDirty(reason = 'network-change')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1021</code></p>
<p>Configures or reads mark network dirty.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;network-change&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-serializesnapshot" class="helios-api-member-anchor"></a>

### `serializeSnapshot(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1878</code></p>
<p>Read or set the serialize snapshot setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current serialize snapshot value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.serializeSnapshot({
  enabled: true,
});
</code></pre>
</div>

<a id="method-serializesessionsnapshot" class="helios-api-member-anchor"></a>

### `serializeSessionSnapshot(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2082</code></p>
<p>Read or set the serialize session snapshot setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current serialize session snapshot value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.serializeSessionSnapshot({
  enabled: true,
});
</code></pre>
</div>

<a id="method-savesessionsnapshot" class="helios-api-member-anchor"></a>

### `saveSessionSnapshot(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2263</code></p>
<p>Read or set the save session snapshot setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current save session snapshot value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.saveSessionSnapshot({
  enabled: true,
});
</code></pre>
</div>

<a id="method-restoresessionsnapshot" class="helios-api-member-anchor"></a>

### `restoreSessionSnapshot(snapshot = {}, options = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2306</code></p>
<p>Updates the session snapshot state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>restoreSessionSnapshot</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-serializenetworksnapshot" class="helios-api-member-anchor"></a>

### `serializeNetworkSnapshot(options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2402</code></p>
<p>Serialize a visualization envelope suitable for attachment to a portable network export. The envelope includes the current <code>storageState</code> snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Snapshot options forwarded to Helios.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Visualization-state envelope.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.serializeNetworkSnapshot({
  enabled: true,
});
</code></pre>
</div>

<a id="method-attachvisualizationstatetonetwork" class="helios-api-member-anchor"></a>

### `attachVisualizationStateToNetwork(snapshot = null, options = {})` &rarr; &#123;Promise&lt;unknown&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2438</code></p>
<p>Attach a visualization-state envelope to the active network.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Existing visualization envelope, or <code>null</code> to capture one through storage.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attachment options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>The underlying Helios attachment result.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>unknown</code>&gt;</span></div>
</div>

<a id="method-savenetworksnapshot" class="helios-api-member-anchor"></a>

### `saveNetworkSnapshot(format = 'zxnet', options = {})` &rarr; &#123;Promise&lt;unknown&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2453</code></p>
<p>Save the active network with visualization state attached.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>format</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;zxnet&#x27;</code></td><td class="helios-api-param-description">Portable network format.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Save options forwarded to Helios.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Serialized network payload.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>unknown</code>&gt;</span></div>
</div>

<a id="method-restorenetworksnapshot" class="helios-api-member-anchor"></a>

### `restoreNetworkSnapshot(source, options = {})` &rarr; &#123;Promise&lt;unknown&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2471</code></p>
<p>Restore a portable network snapshot through Helios network loading.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>source</code></td><td class="helios-api-param-type"><code>unknown</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Network payload or file-like source.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Restore options forwarded to Helios.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Loaded network result.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>unknown</code>&gt;</span></div>
</div>

<a id="method-restoresnapshot" class="helios-api-member-anchor"></a>

### `restoreSnapshot(snapshot = {}, options = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2479</code></p>
<p>Updates the snapshot state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>restoreSnapshot</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-loadsession" class="helios-api-member-anchor"></a>

### `loadSession(sessionId = this.sessionId, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2497</code></p>
<p>Handles session for the current graph or visualization state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>sessionId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>this.sessionId</code></td><td class="helios-api-param-description">Value passed to <code>loadSession</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-restoreactivesession" class="helios-api-member-anchor"></a>

### `restoreActiveSession(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2567</code></p>
<p>Read or set the restore active session setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current restore active session value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.restoreActiveSession({
  enabled: true,
});
</code></pre>
</div>

<a id="method-savesession" class="helios-api-member-anchor"></a>

### `saveSession(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2694</code></p>
<p>Read or set the save session setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current save session value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.saveSession({
  enabled: true,
});
</code></pre>
</div>

<a id="method-restoresession" class="helios-api-member-anchor"></a>

### `restoreSession(sessionIdOrRecord, options = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2799</code></p>
<p>Updates the session state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>sessionIdOrRecord</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>restoreSession</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-markpositionsdirty" class="helios-api-member-anchor"></a>

### `markPositionsDirty(reason = 'positions-change')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1045</code></p>
<p>Configures or reads mark positions dirty.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;positions-change&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-getunfinishedsessionid" class="helios-api-member-anchor"></a>

### `getUnfinishedSessionId()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:803</code></p>
<p>Returns the current unfinished session id value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getUnfinishedSessionId();
</code></pre>
</div>

<a id="method-setunfinishedsessionid" class="helios-api-member-anchor"></a>

### `setUnfinishedSessionId(id)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:807</code></p>
<p>Set the unfinished session id setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setUnfinishedSessionId</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-setoverridetrackingready" class="helios-api-member-anchor"></a>

### `setOverrideTrackingReady(ready = true)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:811</code></p>
<p>Set the override tracking ready setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>ready</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Value passed to <code>setOverrideTrackingReady</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-getpreferences" class="helios-api-member-anchor"></a>

### `getPreferences()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:977</code></p>
<p>Returns the current preferences value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getPreferences();
</code></pre>
</div>

<a id="method-setsessionnickname" class="helios-api-member-anchor"></a>

### `setSessionNickname(nickname, id = this.sessionId)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1075</code></p>
<p>Set the session nickname setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nickname</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setSessionNickname</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>this.sessionId</code></td><td class="helios-api-param-description">Value passed to <code>setSessionNickname</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-getsession" class="helios-api-member-anchor"></a>

### `getSession(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2712</code></p>
<p>Returns the current session value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>getSession</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-getresumesessions" class="helios-api-member-anchor"></a>

### `getResumeSessions(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2749</code></p>
<p>Read or set the get resume sessions setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current get resume sessions value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.getResumeSessions({
  enabled: true,
});
</code></pre>
</div>

<a id="method-getresumeprompt" class="helios-api-member-anchor"></a>

### `getResumePrompt(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2778</code></p>
<p>Read or set the get resume prompt setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current get resume prompt value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.getResumePrompt({
  enabled: true,
});
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-configure" class="helios-api-member-anchor"></a>

### `configure(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:922</code></p>
<p>Read or set the configure setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current configure value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.configure({
  enabled: true,
});
</code></pre>
</div>

<a id="method-updatepreferences" class="helios-api-member-anchor"></a>

### `updatePreferences(patch = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:993</code></p>
<p>Configures or reads update preferences.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>patch</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>updatePreferences</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-acknowledgesavedsnapshot" class="helios-api-member-anchor"></a>

### `acknowledgeSavedSnapshot(reason = 'save-acknowledged', options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1508</code></p>
<p>Configures or reads acknowledge saved snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;save-acknowledged&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-debugstats" class="helios-api-member-anchor"></a>

### `debugStats(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1771</code></p>
<p>Read or set the debug stats setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current debug stats value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.debugStats({
  enabled: true,
});
</code></pre>
</div>

<a id="method-status" class="helios-api-member-anchor"></a>

### `status()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1838</code></p>
<p>Configures or reads status.</p>
</div>

<a id="method-persistencestatus" class="helios-api-member-anchor"></a>

### `persistenceStatus()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:1842</code></p>
<p>Configures or reads persistence status.</p>
</div>

<a id="method-deserializesessionsnapshot" class="helios-api-member-anchor"></a>

### `deserializeSessionSnapshot(snapshot = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2218</code></p>
<p>Configures or reads deserialize session snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>deserializeSessionSnapshot</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-capturesessionthumbnail" class="helios-api-member-anchor"></a>

### `captureSessionThumbnail(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2222</code></p>
<p>Read or set the capture session thumbnail setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current capture session thumbnail value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.captureSessionThumbnail({
  enabled: true,
});
</code></pre>
</div>

<a id="method-configuresession" class="helios-api-member-anchor"></a>

### `configureSession(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2529</code></p>
<p>Read or set the configure session setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current configure session value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.configureSession({
  enabled: true,
});
</code></pre>
</div>

<a id="method-startnewsession" class="helios-api-member-anchor"></a>

### `startNewSession(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2608</code></p>
<p>Read or set the start new session setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current start new session value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.startNewSession({
  enabled: true,
});
</code></pre>
</div>

<a id="method-flushprevioussessionforswitch" class="helios-api-member-anchor"></a>

### `flushPreviousSessionForSwitch(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2644</code></p>
<p>Read or set the flush previous session for switch setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current flush previous session for switch value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.flushPreviousSessionForSwitch({
  enabled: true,
});
</code></pre>
</div>

<a id="method-listsessions" class="helios-api-member-anchor"></a>

### `listSessions(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2719</code></p>
<p>Read or set the list sessions setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current list sessions value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.listSessions({
  enabled: true,
});
</code></pre>
</div>

<a id="method-listsessionsummaries" class="helios-api-member-anchor"></a>

### `listSessionSummaries(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2742</code></p>
<p>Read or set the list session summaries setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current list session summaries value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.listSessionSummaries({
  enabled: true,
});
</code></pre>
</div>

<a id="method-resumesession" class="helios-api-member-anchor"></a>

### `resumeSession(sessionId, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2794</code></p>
<p>Configures or reads resume session.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>sessionId</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resumeSession</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-deletesession" class="helios-api-member-anchor"></a>

### `deleteSession(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2806</code></p>
<p>Configures or reads delete session.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>deleteSession</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-marksessionfinished" class="helios-api-member-anchor"></a>

### `markSessionFinished(id = this.sessionId)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2817</code></p>
<p>Configures or reads mark session finished.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>this.sessionId</code></td><td class="helios-api-param-description">Value passed to <code>markSessionFinished</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-flush" class="helios-api-member-anchor"></a>

### `flush(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2842</code></p>
<p>Read or set the flush setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current flush value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.flush({
  enabled: true,
});
</code></pre>
</div>

<a id="method-sync" class="helios-api-member-anchor"></a>

### `sync(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2880</code></p>
<p>Read or set the sync setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current sync value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.sync({
  enabled: true,
});
</code></pre>
</div>

<a id="method-flushautosync" class="helios-api-member-anchor"></a>

### `flushAutosync(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/storage/HeliosStorageManager.js:2884</code></p>
<p>Read or set the flush autosync setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current flush autosync value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.flushAutosync({
  enabled: true,
});
</code></pre>
</div>
