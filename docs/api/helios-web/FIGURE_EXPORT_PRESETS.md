# FIGURE_EXPORT_PRESETS

<div class="helios-api-kind">symbol</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>symbol</dd>
<dt>Source</dt>
<dd>src/export/figureExport.js:9</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in figure size presets for Helios exports.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export const FIGURE_EXPORT_PRESETS = Object.freeze([
```

</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Presets include current-window sizes, common video/print raster
sizes, and a custom target. Availability still depends on renderer texture
limits and requested supersampling.
</div>
