# PERSISTENCE_KINDS

<div class="helios-api-kind">symbol</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>symbol</dd>
<dt>Source</dt>
<dd>src/persistence/schema.js:15</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Supported persistence envelope kinds.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export const PERSISTENCE_KINDS = Object.freeze({
```

</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Preferences, visualization snapshots, and full sessions share the
same envelope shape but validate different payload structures.
</div>
