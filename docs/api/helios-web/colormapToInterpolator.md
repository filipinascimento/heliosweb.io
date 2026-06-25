# colormapToInterpolator

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/colors/colormaps.js:449</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Resolve a colormap to an interpolation function.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function colormapToInterpolator(input) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>input</code></td><td class="helios-api-param-type"><code>string</code>|<code>Function</code>|<code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Colormap reference.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Function that maps <code>0..1</code> values to colors.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Function</code>|<code>null</code></span></div>
</div>
