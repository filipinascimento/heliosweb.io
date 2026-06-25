# getFigureExportCapability

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/export/figureExport.js:180</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Resolve renderer limits that constrain figure export dimensions.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function getFigureExportCapability(renderer, supersampling = 1) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>renderer</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Active Helios renderer.</td></tr>
<tr><td class="helios-api-param-name"><code>supersampling</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>1</code></td><td class="helios-api-param-description">Requested supersampling factor.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Export capability for the current WebGL/WebGPU device.</p><span class="helios-api-return-type"><strong>Type</strong> {<code>supersampling</code>:<code>number</code>,<code>maxBitmapDimension</code>:<code>number</code>,<code>maxFigureDimension</code>:<code>number</code>}</span></div>
</div>
