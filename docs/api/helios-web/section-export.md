
# Export

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

Figure export presets, capability checks, PNG/SVG capture, and preview helpers.

Export APIs capture figures and previews from the renderer. Presets describe
common output sizes and settings, while export helpers coordinate render
settling, background choices, and format-specific capture.

Use these APIs for screenshots, publication figures, thumbnail generation, and
host applications that need deterministic preview images.

<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../buildFigureExportPresetList/">
<span>function</span>
<strong>buildFigureExportPresetList</strong>
<em>Build export preset metadata for a viewport and renderer capability.</em>
</a>
<a class="helios-api-directory-item" href="../getFigureExportCapability/">
<span>function</span>
<strong>getFigureExportCapability</strong>
<em>Resolve renderer limits that constrain figure export dimensions.</em>
</a>
<a class="helios-api-directory-item" href="../resolveFigureExportOptions/">
<span>function</span>
<strong>resolveFigureExportOptions</strong>
<em>Normalize figure export options into concrete dimensions and capture flags.</em>
</a>
</div>
