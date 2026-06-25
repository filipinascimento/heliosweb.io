# decodeColormapData

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/colors/colormaps.js:54</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Decode packed RGB colormap bytes into color tuples.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function decodeColormapData(b64, expectedN) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>b64</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Base64-encoded RGB byte payload.</td></tr>
<tr><td class="helios-api-param-name"><code>expectedN</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Expected number of colors.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>RGB colors in byte space.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>Array</code>&lt;<code>number</code>&gt;&gt;</span></div>
</div>
