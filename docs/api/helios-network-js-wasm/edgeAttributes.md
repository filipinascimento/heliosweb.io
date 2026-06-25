# edgeAttributes

<div class="helios-api-kind">method</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>method</dd>
<dt>Source</dt>
<dd>src/js/HeliosNetwork.js:5612</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Defines or updates several edge attributes and returns the network for chaining.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
edgeAttributes(names, valuesOrFn, options = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>names</code></td><td class="helios-api-param-type"><code>string</code>[]</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute identifiers.</td></tr>
<tr><td class="helios-api-param-name"><code>valuesOrFn</code></td><td class="helios-api-param-type"><code>Object</code>|<code>Array</code>|<code>function</code>(<code>Object</code>, <code>number</code>, <code>number</code>, <a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a>): (<code>Array</code>|<code>Object</code>)</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Sources for each attribute.</td></tr>
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
Use this when edge attributes are loaded from edge-table rows or
generated together. The helper keeps schema definition, value conversion, and
version updates in one call.
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
net.edgeAttributes(['weight', 'visible'], { weight: [1, 2], visible: true });
```

</div>
