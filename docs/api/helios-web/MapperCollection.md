# MapperCollection

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/pipeline/Mapper.js:1207</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Collection of named mappers for either node or edge visuals.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class MapperCollection {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type">&#x27;<code>node</code>&#x27;|&#x27;<code>edge</code>&#x27;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visual target scope.</td></tr>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Source graph.</td></tr>
<tr><td class="helios-api-param-name"><code>onChange</code></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Callback invoked when mapper configuration changes.</td></tr>
<tr><td class="helios-api-param-name"><code>debug</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>constructor</code>.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Collection with a default mapper.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/MapperCollection/"><code>MapperCollection</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Collections let apps keep multiple named mapper presets and combine
them before applying visual attributes.
</div>

## Mappers { #api-mappers .helios-api-section-title }

<p class="helios-api-section-description">Mapper configuration for node and edge visual channels. <a href="MappersBehavior.md">MappersBehavior</a> handles mapper UI state.</p>

<a id="method-createmapper" class="helios-api-member-anchor"></a>

### `createMapper(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1265</code></p>
<p>Configures or reads create mapper.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-tocombinedmapper" class="helios-api-member-anchor"></a>

### `toCombinedMapper(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1288</code></p>
<p>Merges all registered mappers into a single Mapper (channels override in insertion order).</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current to combined mapper value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.toCombinedMapper({
  enabled: true,
});
</code></pre>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setdefault" class="helios-api-member-anchor"></a>

### `setDefault(mapper)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1257</code></p>
<p>Replaces the default mapper.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mapper</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/Mapper/"><code>Mapper</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-channel" class="helios-api-member-anchor"></a>

### `channel(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1222</code></p>
<p>Returns a ChannelBuilder bound to the default mapper. Calling <code>.done()</code> will mark the collection dirty.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-add" class="helios-api-member-anchor"></a>

### `add(entry, name)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1239</code></p>
<p>Adds a Mapper instance or a descriptor object describing channels.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>entry</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/Mapper/"><code>Mapper</code></a> | <code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-buildfromdescriptor" class="helios-api-member-anchor"></a>

### `buildFromDescriptor(descriptor)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1271</code></p>
<p>Configures or reads build from descriptor.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>descriptor</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>buildFromDescriptor</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-touch" class="helios-api-member-anchor"></a>

### `touch()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1313</code></p>
<p>Configures or reads touch.</p>
</div>
