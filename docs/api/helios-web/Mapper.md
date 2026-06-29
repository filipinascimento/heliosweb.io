# Mapper

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/pipeline/Mapper.js:842</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Low-level mapper for one node or edge visual mode.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class Mapper {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mapper mode (<code>node</code> or <code>edge</code>), network, and optional bookkeeping dependencies.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Mapper with an initially empty channel set.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Mapper/"><code>Mapper</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Most applications should use `MapperCollection` or
`MappersBehavior`. Direct mapper access is still public for custom pipelines
that need to build visual attributes programmatically.
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setchannel" class="helios-api-member-anchor"></a>

### `setChannel(name, config)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:854</code></p>
<p>Set the channel setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setChannel</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-getchannel" class="helios-api-member-anchor"></a>

### `getChannel(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:866</code></p>
<p>Returns the current channel value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-channel" class="helios-api-member-anchor"></a>

### `channel(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:850</code></p>
<p>Configures or reads channel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-mapitem" class="helios-api-member-anchor"></a>

### `mapItem(item, context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:870</code></p>
<p>Configures or reads map item.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>item</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>mapItem</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>mapItem</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-mapitems" class="helios-api-member-anchor"></a>

### `mapItems(items, context = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:879</code></p>
<p>Configures or reads map items.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>items</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>mapItems</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>mapItems</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-ensurepercentilelookup" class="helios-api-member-anchor"></a>

### `ensurePercentileLookup(config)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:883</code></p>
<p>Configures or reads ensure percentile lookup.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>ensurePercentileLookup</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-ensurebuffersforchannel" class="helios-api-member-anchor"></a>

### `ensureBuffersForChannel(config)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:892</code></p>
<p>Configures or reads ensure buffers for channel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>ensureBuffersForChannel</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-shouldensurechannelbuffer" class="helios-api-member-anchor"></a>

### `shouldEnsureChannelBuffer(config, def)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:943</code></p>
<p>Configures or reads should ensure channel buffer.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>shouldEnsureChannelBuffer</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>def</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>shouldEnsureChannelBuffer</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-isnodepassthroughchannel" class="helios-api-member-anchor"></a>

### `isNodePassthroughChannel(config, def)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:951</code></p>
<p>Returns the current node passthrough channel value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>isNodePassthroughChannel</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>def</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>isNodePassthroughChannel</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-resolvenodesourceattribute" class="helios-api-member-anchor"></a>

### `resolveNodeSourceAttribute(config, def)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:959</code></p>
<p>Configures or reads resolve node source attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolveNodeSourceAttribute</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>def</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolveNodeSourceAttribute</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-resolvenodesourcedimension" class="helios-api-member-anchor"></a>

### `resolveNodeSourceDimension(sourceAttribute, def)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:971</code></p>
<p>Configures or reads resolve node source dimension.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>sourceAttribute</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolveNodeSourceDimension</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>def</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolveNodeSourceDimension</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-resolvepassthroughconfig" class="helios-api-member-anchor"></a>

### `resolvePassthroughConfig(config, def, sourceDimension, expectedDimension)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:988</code></p>
<p>Configures or reads resolve passthrough config.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolvePassthroughConfig</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>def</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolvePassthroughConfig</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>sourceDimension</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolvePassthroughConfig</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>expectedDimension</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resolvePassthroughConfig</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-ensurenodesourceattribute" class="helios-api-member-anchor"></a>

### `ensureNodeSourceAttribute(sourceAttribute, type, sourceDimension, channelName)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1025</code></p>
<p>Configures or reads ensure node source attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>sourceAttribute</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>ensureNodeSourceAttribute</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute value type.</td></tr>
<tr><td class="helios-api-param-name"><code>sourceDimension</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>ensureNodeSourceAttribute</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>channelName</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>ensureNodeSourceAttribute</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-removeedgeattribute" class="helios-api-member-anchor"></a>

### `removeEdgeAttribute(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1113</code></p>
<p>Manages edge attribute for the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-unregisternodetoedge" class="helios-api-member-anchor"></a>

### `unregisterNodeToEdge(attribute)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1126</code></p>
<p>Configures or reads unregister node to edge.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>attribute</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>unregisterNodeToEdge</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-unregisterchannel" class="helios-api-member-anchor"></a>

### `unregisterChannel(config)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/pipeline/Mapper.js:1139</code></p>
<p>Configures or reads unregister channel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>config</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>unregisterChannel</code>.</td></tr>
</tbody>
</table>
</div>
