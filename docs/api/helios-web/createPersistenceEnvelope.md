# createPersistenceEnvelope

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/persistence/schema.js:302</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Create a versioned persistence envelope.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function createPersistenceEnvelope(kind, payload, metadata = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>kind</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">One of <code>preferences</code>, <code>visualization</code>, or <code>session</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>payload</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Payload to normalize for the selected kind.</td></tr>
<tr><td class="helios-api-param-name"><code>metadata</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Caller-owned metadata copied into the envelope.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Current-schema persistence envelope.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Envelopes are the boundary used by Helios persistence APIs and by
portable network visualization attachments. Unknown payload fields are
normalized rather than passed through blindly.
</div>
