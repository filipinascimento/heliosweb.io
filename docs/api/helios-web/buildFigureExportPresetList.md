# buildFigureExportPresetList

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/export/figureExport.js:335</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Build export preset metadata for a viewport and renderer capability.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function buildFigureExportPresetList(windowSize = {}, capability = { maxBitmapDimension: Infinity }, supersampling = 1) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>windowSize</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Current logical viewport size.</td></tr>
<tr><td class="helios-api-param-name"><code>capability</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Result of <code>getFigureExportCapability</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>supersampling</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>1</code></td><td class="helios-api-param-description">Requested supersampling factor.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Preset records with dimensions and availability.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>.&lt;<code>Object</code>&gt;</span></div>
</div>
