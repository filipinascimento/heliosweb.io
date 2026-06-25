# BEHAVIOR_IDS

<div class="helios-api-kind">symbol</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>symbol</dd>
<dt>Source</dt>
<dd>src/behaviors/index.js:22</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Ordered ids for the built-in behavior set.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export const BEHAVIOR_IDS = Object.freeze([
```

</div>

## Notes

<div markdown="1" class="helios-api-template-section">
The order matches `createDefaultBehaviorRegistry()` registration and
is stable for UI/persistence code that needs to list built-ins.
</div>
