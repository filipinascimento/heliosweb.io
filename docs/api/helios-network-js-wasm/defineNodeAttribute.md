# defineNodeAttribute

<div class="helios-api-kind">method</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>method</dd>
<dt>Source</dt>
<dd>src/js/HeliosNetwork.js:5679</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Defines a node attribute backed by linear WASM memory.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
defineNodeAttribute(name, type, dimension = 1) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute identifier.</td></tr>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>AttributeType</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute type constant.</td></tr>
<tr><td class="helios-api-param-name"><code>dimension</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>1</code></td><td class="helios-api-param-description">Number of elements per node.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> <code>void</code></span></div>
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
import HeliosNetwork, { AttributeType } from 'helios-network';
const net = await HeliosNetwork.create({ initialNodes: 2 });
net.defineNodeAttribute('weight', AttributeType.Float);
net.withBufferAccess(() => {
  const weightBuffer = net.getNodeAttributeBuffer('weight').view;
  weightBuffer[0] = 1.5;
});
```

</div>
