# serializePersistenceEnvelope

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/persistence/schema.js:491</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Serialize a persistence envelope to JSON.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function serializePersistenceEnvelope(envelope, pretty = true) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>envelope</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Envelope or partial payload to normalize first.</td></tr>
<tr><td class="helios-api-param-name"><code>pretty</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Whether to emit indented JSON.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Stable JSON string.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code></span></div>
</div>
