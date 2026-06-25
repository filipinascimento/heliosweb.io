# nodeAttribute

<div class="helios-api-kind">method</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>method</dd>
<dt>Source</dt>
<dd>src/js/HeliosNetwork.js:5556</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Defines or updates one node attribute and returns the network for chaining. Missing attributes are defined from `options.type` / `options.dimension`, or inferred from the provided scalar, array-like value, or callback result. Array-like values are indexed by active ordinal by default; pass `{ indexBy: 'id' }` to index them by node id instead.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
nodeAttribute(name, valueOrFn, options = {}) {
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
This is the recommended API for normal application code. It performs
any needed allocation before writing values, so callers do not need to manage
WASM typed-array view lifetime directly. Use `withBufferAccess(...)` only when
you intentionally want the lower-level fast path for very large writes.
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
net
  .nodeAttribute('weight', 1)
  .nodeAttribute('label', (_current, id) => `node-${id}`, { type: 'string' });
```

</div>
