# ensureDefaultStyles

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/ui/style/defaultStyles.js:2947</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Ensure the default Helios UI stylesheet is present in a document.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function ensureDefaultStyles(doc = document) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>doc</code></td><td class="helios-api-param-type"><code>Document</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>document</code></td><td class="helios-api-param-description">Target document.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Existing or inserted stylesheet element.</p><span class="helios-api-return-type"><strong>Type</strong> <code>HTMLStyleElement</code>|<code>null</code></span></div>
</div>
