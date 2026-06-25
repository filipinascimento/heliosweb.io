# extractLayoutTuningFeatures

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/layouts/layoutTuningModel.generated.js:145</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Extract graph features used by the layout tuning model.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function extractLayoutTuningFeatures(network, hints = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Helios network or network-like object.</td></tr>
<tr><td class="helios-api-param-name"><code>hints</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional feature overrides such as nodeCount or edgeCount.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Feature record and model input vector.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>
