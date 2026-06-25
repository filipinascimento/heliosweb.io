# MappersBehavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/MappersBehavior.js:90</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in behavior for node and edge visual mappers.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class MappersBehavior extends Behavior {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Serializable node/edge mapper snapshots or channel configurations for color, size, opacity, outline, and edge width.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Behavior that applies and serializes mapper channel state.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/MappersBehavior/"><code>MappersBehavior</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Mapper channel configs should avoid functions when they need to be
persisted. Use serializable `constant`, `linear`, `categorical`,
`colormap`, `nodeToEdge`, and `passthrough` configurations.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:91</code></p>
<p>Id exposed by the class.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-getpublicstate" class="helios-api-member-anchor"></a>

### `getPublicState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:207</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:99</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:127</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:194</code></p>
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

## Mappers { #api-mappers .helios-api-section-title }

<p class="helios-api-section-description">Mapper configuration for node and edge visual channels. <a href="MappersBehavior.md">MappersBehavior</a> handles mapper UI state.</p>

<a id="method-mappers" class="helios-api-member-anchor"></a>

### `mappers(options)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:211</code></p>
<p>Read or set the mappers setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current mappers value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.mappers({
  enabled: true,
});
</code></pre>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-getchannelconfig" class="helios-api-member-anchor"></a>

### `getChannelConfig(mode, channel)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:216</code></p>
<p>Returns the current channel config value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mode for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>channel</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Channel for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.getChannelConfig(&#x27;2d&#x27;);
</code></pre>
</div>

<a id="method-setmodesnapshot" class="helios-api-member-anchor"></a>

### `setModeSnapshot(mode, snapshot, { reason = 'mode', trackOverride = true } = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:300</code></p>
<p>Set the mode snapshot setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mode for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setModeSnapshot</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;mode&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>trackOverride</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true } = {}</code></td><td class="helios-api-param-description">Value passed to <code>setModeSnapshot</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setModeSnapshot(&#x27;2d&#x27;);
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:117</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:133</code></p>
<p>Configures or reads state entries.</p>
</div>

<a id="method-emitchange" class="helios-api-member-anchor"></a>

### `emitChange(reason, detail = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:203</code></p>
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

<a id="method-replacedefaultchannels" class="helios-api-member-anchor"></a>

### `replaceDefaultChannels(mode, channels = {}, { reason = 'channels', trackOverride = true } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:278</code></p>
<p>Updates the default channels state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mode for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>channels</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>replaceDefaultChannels</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;channels&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>trackOverride</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true } = {}</code></td><td class="helios-api-param-description">Value passed to <code>replaceDefaultChannels</code>.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.replaceDefaultChannels(&#x27;2d&#x27;);
</code></pre>
</div>

<a id="method-syncfromhelios" class="helios-api-member-anchor"></a>

### `syncFromHelios({ silent = false } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:314</code></p>
<p>Configures or reads sync from helios.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>silent</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false } = {}</code></td><td class="helios-api-param-description">Value passed to <code>syncFromHelios</code>.</td></tr>
</tbody>
</table>
</div>

## Mapper Configuration { #api-mapper-configuration .helios-api-section-title }

<a id="method-getserializedchannelconfig" class="helios-api-member-anchor"></a>

### `getSerializedChannelConfig(mode, channel)` &rarr; &#123;Object|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:234</code></p>
<p>Return a serializable snapshot for one visual channel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type">&#x27;<code>node</code>&#x27;|&#x27;<code>edge</code>&#x27;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mapper collection to inspect.</td></tr>
<tr><td class="helios-api-param-name"><code>channel</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visual channel name such as <code>color</code>, <code>size</code>, <code>opacity</code>, <code>outline</code>, or <code>width</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>JSON-safe channel configuration, or <code>null</code> when the channel is not registered.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.getSerializedChannelConfig(&#x27;2d&#x27;);
</code></pre>
</div>

<a id="method-setchannelconfig" class="helios-api-member-anchor"></a>

### `setChannelConfig(mode, channel, config, options = {})` &rarr; &#123;boolean&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/MappersBehavior.js:257</code></p>
<p>Replace the default mapper configuration for one visual channel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type">&#x27;<code>node</code>&#x27;|&#x27;<code>edge</code>&#x27;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mapper collection to update.</td></tr>
<tr><td class="helios-api-param-name"><code>channel</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visual channel name.</td></tr>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Serializable channel configuration.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p><code>true</code> when the channel was applied.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code></span></div>
<h4>Notes</h4>
<p>This mutates the active default mapper and emits a mapper change event. Persisted configurations should avoid functions.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.behavior.mappers.setChannelConfig(&#x27;node&#x27;, &#x27;color&#x27;, {
  type: &#x27;colormap&#x27;,
  attributes: &#x27;score&#x27;,
  colormap: &#x27;interpolateViridis&#x27;,
  domain: [0, 1],
});
</code></pre>
</div>


## Example

<div markdown="1" class="helios-api-template-section">

```js
helios.behavior.mappers.setChannelConfig('node', 'color', {
  type: 'colormap',
  attributes: 'score',
  colormap: 'interpolateViridis',
  domain: [0, 1],
});
```

</div>
