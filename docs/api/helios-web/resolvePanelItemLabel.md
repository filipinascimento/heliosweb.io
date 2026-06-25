# resolvePanelItemLabel

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/ui/panels/panelSchema.js:92</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Resolve the display label for a panel schema item.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function resolvePanelItemLabel(item, stateManager = null) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>item</code></td><td class="helios-api-param-type"><code>string</code>|<code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel schema item descriptor.</td></tr>
<tr><td class="helios-api-param-name"><code>stateManager</code></td><td class="helios-api-param-type"><code>HeliosStateManager</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional state manager for state entry labels.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Display label for the item.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code></span></div>
</div>
