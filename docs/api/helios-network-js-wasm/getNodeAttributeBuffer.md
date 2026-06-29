# getNodeAttributeBuffer

<div class="helios-api-kind">method</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>method</dd>
<dt>Source</dt>
<dd>src/js/HeliosNetwork.js:6124</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Retrieves a wrapper around the node attribute buffer.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
getNodeAttributeBuffer(name) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute identifier.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Wrapper providing type information and buffer helpers.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
const net = await HeliosNetwork.create();
net.defineNodeAttribute('flag', AttributeType.Boolean);
const nodes = net.addNodes(1);
net.withBufferAccess(() => {
  const attribute = net.getNodeAttributeBuffer('flag');
  attribute.view[nodes[0]] = 1;
});
```

</div>
