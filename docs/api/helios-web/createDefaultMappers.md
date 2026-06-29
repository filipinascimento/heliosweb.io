# createDefaultMappers

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/pipeline/Mapper.js:1162</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Create the default node and edge mapper collections for a network.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function createDefaultMappers(network) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Source graph.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Default node and edge mappers used when Helios is constructed without custom mappers.</p><span class="helios-api-return-type"><strong>Type</strong> {<code>nodeMapper</code>:<a href="/docs/api/helios-web/Mapper/"><code>Mapper</code></a>,<code>edgeMapper</code>:<a href="/docs/api/helios-web/Mapper/"><code>Mapper</code></a>}</span></div>
</div>
