# createCategoricalColormap

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/colors/colormaps.js:529</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Create a categorical palette from a colormap.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function createCategoricalColormap(colormapInput, count) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>colormapInput</code></td><td class="helios-api-param-type"><code>string</code>|<code>Function</code>|<code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Colormap reference.</td></tr>
<tr><td class="helios-api-param-name"><code>count</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Number of categories.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>RGBA colors for categories.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>Array</code>&lt;<code>number</code>&gt;&gt;</span></div>
</div>
