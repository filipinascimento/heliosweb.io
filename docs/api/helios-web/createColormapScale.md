# createColormapScale

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/colors/colormaps.js:483</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Create a numeric colormap scale.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function createColormapScale(colormapInput, options = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>colormapInput</code></td><td class="helios-api-param-type"><code>string</code>|<code>Function</code>|<code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Colormap reference.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Scale options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.domain"><span aria-hidden="true">|</span><code>domain</code></span></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Numeric input domain.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.alpha"><span aria-hidden="true">|</span><code>alpha</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Output alpha override.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Function that maps values to RGBA colors.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Function</code></span></div>
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
const color = createColormapScale('interpolateViridis', { domain: [0, 1] });
```

</div>
