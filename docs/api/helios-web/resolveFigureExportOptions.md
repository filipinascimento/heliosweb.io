# resolveFigureExportOptions

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/export/figureExport.js:213</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Normalize figure export options into concrete dimensions and capture flags.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function resolveFigureExportOptions(options = {}, context = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Requested filename, format, preset, width, height, supersampling, overlay inclusion, transparency, and legend scale.</td></tr>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Renderer, viewport, device pixel ratio, and capability context.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Resolved export options including logical dimensions, bitmap dimensions, crop rectangle, filename, and capability fit status.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Callers should check `fitsCapability` before allocating render
targets for the result.
</div>
