# edgeAttribute

<div class="helios-api-kind">method</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>method</dd>
<dt>Source</dt>
<dd>src/js/HeliosNetwork.js:5574</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Defines or updates one edge attribute and returns the network for chaining.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
edgeAttribute(name, valueOrFn, options = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute identifier.</td></tr>
<tr><td class="helios-api-param-name"><code>valueOrFn</code></td><td class="helios-api-param-type">*|<code>function</code>(*, <code>number</code>, <code>number</code>, <a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a>): *</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Scalar, array-like values, or callback.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>AttributeWriteOptions</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional type, dimension, and indexing controls.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>This network.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Array-like values are aligned to the active edge ordinal by default.
Pass `{ indexBy: 'id' }` when your values are keyed by stable edge id instead.
For bulk streaming writes into existing typed arrays, use the explicit buffer API.
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
net.edgeAttribute('capacity', [10, 20, 30]);
```

</div>
