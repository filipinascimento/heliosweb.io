# EVENTS

<div class="helios-api-kind">symbol</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>symbol</dd>
<dt>Source</dt>
<dd>src/Helios.js:2070</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Stable event names emitted by `Helios` instances.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export const EVENTS = Object.freeze({
```

</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Event payloads are delivered through `CustomEvent.detail` where the
browser supports `CustomEvent`. Use these constants instead of string
literals when wiring app behavior to render, layout, camera, picking, mapper,
filter, or network replacement changes.
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
helios.on(EVENTS.NODE_HOVER, (event) => {
  console.log(event.detail?.index);
});
```

</div>
