# networkAttribute

<div class="helios-api-kind">method</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>method</dd>
<dt>Source</dt>
<dd>src/js/HeliosNetwork.js:5635</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Defines or updates one network-level attribute and returns the network for chaining. Network attributes store one graph-wide value at id/ordinal `0`. Missing attributes are defined from `options.type` / `options.dimension`, or inferred from the provided value or callback result.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
networkAttribute(name, valueOrFn, options = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute identifier.</td></tr>
<tr><td class="helios-api-param-name"><code>valueOrFn</code></td><td class="helios-api-param-type">*|<code>function</code>(*, <code>number</code>, <code>number</code>, <a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a>): *</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Scalar, vector, or callback.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>AttributeWriteOptions</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional type and dimension controls.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>This network.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Network attributes store graph-wide metadata such as titles,
coordinate bounds, import provenance, or visualization defaults. They have one
logical value and do not iterate over nodes or edges.
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
net
  .networkAttribute('title', 'Example graph')
  .networkAttribute('bounds', [0, 1], { type: 'float', dimension: 2 });
```

</div>
