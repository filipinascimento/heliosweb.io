# diffOverrideMaps

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/persistence/schema.js:418</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Compute sparse override differences between two flattened override maps.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function diffOverrideMaps(base = {}, current = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>base</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Baseline dotted-path values.</td></tr>
<tr><td class="helios-api-param-name"><code>current</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Current dotted-path values.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Dotted paths whose values differ from the baseline.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>
