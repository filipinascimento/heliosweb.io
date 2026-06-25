# defineHeliosWebComponents

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/ui/web-components/defineHeliosWebComponents.js:11</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Register Helios Web custom elements in a document or window.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function defineHeliosWebComponents(docOrWin = document) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>docOrWin</code></td><td class="helios-api-param-type"><code>Document</code>|<code>Window</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>document</code></td><td class="helios-api-param-description">Registration target.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Registration result.</p><span class="helios-api-return-type"><strong>Type</strong> {<code>defined</code>:<code>Array</code>&lt;<code>string</code>&gt;,<code>supported</code>:<code>boolean</code>}</span></div>
</div>
