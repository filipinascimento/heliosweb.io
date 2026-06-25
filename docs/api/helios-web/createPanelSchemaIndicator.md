# createPanelSchemaIndicator

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/ui/panels/panelSchema.js:223</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Create a DOM indicator that reflects dirty status for a panel schema.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function createPanelSchemaIndicator({
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Indicator options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.helios"><span aria-hidden="true">|</span><code>helios</code></span></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Helios instance whose state manager is observed.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.schema"><span aria-hidden="true">|</span><code>schema</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel schema to observe.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.sectionId"><span aria-hidden="true">|</span><code>sectionId</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional section id to observe.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.attachTooltip"><span aria-hidden="true">|</span><code>attachTooltip</code></span></td><td class="helios-api-param-type"><code>Function</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional tooltip hook.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Indicator element with a <code>destroy()</code> cleanup method.</p><span class="helios-api-return-type"><strong>Type</strong> <code>HTMLElement</code></span></div>
</div>
