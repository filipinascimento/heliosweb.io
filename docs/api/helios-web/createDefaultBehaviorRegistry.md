# createDefaultBehaviorRegistry

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/behaviors/index.js:45</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Create a registry containing all built-in Helios Web behaviors.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function createDefaultBehaviorRegistry() {
```

</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Registry preloaded with appearance, exporter, mappers, filters, interface, layout, legends, labels, hover, and selection.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/BehaviorRegistry/"><code>BehaviorRegistry</code></a></span></div>
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
const registry = createDefaultBehaviorRegistry()
  .register('custom', CustomBehavior);
```

</div>
