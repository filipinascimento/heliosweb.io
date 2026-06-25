# panelSchemaSectionKeys

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/ui/panels/panelSchema.js:187</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Return all state keys referenced by one panel schema section.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function panelSchemaSectionKeys(schema = {}, sectionId = '') {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>schema</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel schema to inspect.</td></tr>
<tr><td class="helios-api-param-name"><code>sectionId</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Section id to inspect.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Unique state keys referenced by the section.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>[]</span></div>
</div>
