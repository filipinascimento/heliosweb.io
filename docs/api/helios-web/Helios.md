# Helios

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/Helios.js:2236</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Main Helios Web visualization controller for one `helios-network` graph.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class Helios extends EventTarget {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">WASM-backed graph store that supplies topology, attributes, and serialization.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Renderer, layout, behavior, mapper, interface, persistence, touch, camera, and quality options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.container"><span aria-hidden="true">|</span><code>container</code></span></td><td class="helios-api-param-type"><code>Element</code>|<code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>document.body</code></td><td class="helios-api-param-description">Element or selector that receives the Helios canvas, SVG overlays, and interaction layers.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.renderer"><span aria-hidden="true">|</span><code>renderer</code></span></td><td class="helios-api-param-type">&#x27;<code>auto</code>&#x27;|&#x27;<code>webgpu</code>&#x27;|&#x27;<code>webgl</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;auto&#x27;</code></td><td class="helios-api-param-description">Preferred renderer backend. <code>auto</code> chooses WebGPU when available and falls back to WebGL2.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.mode"><span aria-hidden="true">|</span><code>mode</code></span></td><td class="helios-api-param-type">&#x27;2d&#x27;|&#x27;3d&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;2d&#x27;</code></td><td class="helios-api-param-description">Initial dimensional mode.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.projection"><span aria-hidden="true">|</span><code>projection</code></span></td><td class="helios-api-param-type">&#x27;<code>perspective</code>&#x27;|&#x27;<code>orthographic</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;perspective&#x27;</code></td><td class="helios-api-param-description">Initial 3D camera projection.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.layout"><span aria-hidden="true">|</span><code>layout</code></span></td><td class="helios-api-param-type"><code>Object</code>|<code>Layout</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Layout configuration or a layout instance to use for graph positions.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.layout.type"><span aria-hidden="true">|</span><code>type</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;gpu-force&#x27;</code></td><td class="helios-api-param-description">Built-in layout key used when <code>options.layout</code> is a configuration object.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.layout.options"><span aria-hidden="true">|</span><code>options</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Layout-specific options passed to the selected layout implementation.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.startup"><span aria-hidden="true">|</span><code>startup</code></span></td><td class="helios-api-param-type"><code>Object</code>|<code>false</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">First-frame startup behavior, or <code>false</code> to disable the loading overlay, canvas hiding, and layout warmup.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.startup.loadingOverlay"><span aria-hidden="true">|</span><code>loadingOverlay</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Show a centered loading spinner while Helios is preparing the first visible frame.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.startup.hideCanvasUntilFirstFrame"><span aria-hidden="true">|</span><code>hideCanvasUntilFirstFrame</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Keep the canvas hidden until the first intended graph frame is rendered.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.startup.layoutIterations"><span aria-hidden="true">|</span><code>layoutIterations</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>100</code></td><td class="helios-api-param-description">Optional number of layout updates to wait before the first visible graph frame.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.startup.layoutDurationMs"><span aria-hidden="true">|</span><code>layoutDurationMs</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>1000</code></td><td class="helios-api-param-description">Optional layout warmup time to wait before the first visible graph frame. When both layout warmup limits are set, the first one reached releases the frame. Large initial networks use a 5000 ms default duration unless this option is set.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.behaviors"><span aria-hidden="true">|</span><code>behaviors</code></span></td><td class="helios-api-param-type"><code>Object</code>|<code>false</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Built-in behavior options, custom behavior instances, or <code>false</code> to disable default behaviors.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.mappers"><span aria-hidden="true">|</span><code>mappers</code></span></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Initial node and edge mapper configuration. Pass <code>null</code> to skip default mapper setup.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.interpolation"><span aria-hidden="true">|</span><code>interpolation</code></span></td><td class="helios-api-param-type"><code>Object</code>|<code>false</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Position interpolation controls used when switching layouts or applying saved positions.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.labels"><span aria-hidden="true">|</span><code>labels</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Initial label overlay options handled by <code>LabelsBehavior</code>.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.legends"><span aria-hidden="true">|</span><code>legends</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Initial legend overlay options handled by <code>LegendsBehavior</code>.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.density"><span aria-hidden="true">|</span><code>density</code></span></td><td class="helios-api-param-type"><code>boolean</code>|<code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Density layer enablement or density layer options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.transparencyModeEdges"><span aria-hidden="true">|</span><code>transparencyModeEdges</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;weighted&#x27;</code></td><td class="helios-api-param-description">Edge transparency mode. The default weighted mode accumulates overlapping edges without forcing every edge through the same alpha curve.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.camera"><span aria-hidden="true">|</span><code>camera</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Camera framing, controls, and target tracking options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.camera.largeNetworkStartupFit"><span aria-hidden="true">|</span><code>largeNetworkStartupFit</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Start large initial networks from a wider fit and settle toward the normal fit while automatic fitting remains enabled.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.camera.largeNetworkStartupNodeThreshold"><span aria-hidden="true">|</span><code>largeNetworkStartupNodeThreshold</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>1000000</code></td><td class="helios-api-param-description">Node count threshold for wide startup fitting.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.camera.largeNetworkStartupEdgeThreshold"><span aria-hidden="true">|</span><code>largeNetworkStartupEdgeThreshold</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>1000000</code></td><td class="helios-api-param-description">Edge count threshold for wide startup fitting.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.camera.largeNetworkStartupScale"><span aria-hidden="true">|</span><code>largeNetworkStartupScale</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>4</code></td><td class="helios-api-param-description">Multiplier used to move the startup fit farther from the graph before settling.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.camera.largeNetworkStartupDurationMs"><span aria-hidden="true">|</span><code>largeNetworkStartupDurationMs</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>2200</code></td><td class="helios-api-param-description">Duration of the automatic startup settle animation.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.quickControls"><span aria-hidden="true">|</span><code>quickControls</code></span></td><td class="helios-api-param-type"><code>boolean</code>|<code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Compact top-right auto-fit, layout pause/run, and zoom controls. Pass <code>false</code> to disable all controls, or disable individual groups with <code>autoFit</code>, <code>layout</code>, or <code>zoom</code>.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.ui"><span aria-hidden="true">|</span><code>ui</code></span></td><td class="helios-api-param-type"><code>boolean</code>|<code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Optional HeliosUI creation. Pass <code>true</code> to create the standard panel set, or an object with HeliosUI options and <code>panels</code> set to a panel name, array of names, <code>true</code>, or <code>false</code>.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.networkSource"><span aria-hidden="true">|</span><code>networkSource</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Metadata for the active network, such as <code>name</code>, <code>baseName</code>, <code>format</code>, and provenance fields used by persistence and file actions.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.fileDrop"><span aria-hidden="true">|</span><code>fileDrop</code></span></td><td class="helios-api-param-type"><code>boolean</code>|<code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">File-drop behavior for loading supported network files into the active view.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.storage"><span aria-hidden="true">|</span><code>storage</code></span></td><td class="helios-api-param-type"><code>boolean</code>|<code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Storage backend configuration. Pass <code>false</code> to disable persistent sessions, <code>true</code> for browser storage, or an object accepted by <code>createHeliosStorageManager</code>.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.session"><span aria-hidden="true">|</span><code>session</code></span></td><td class="helios-api-param-type"><code>boolean</code>|<code>Object</code>|<code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Session persistence controls or explicit session id used by browser/native storage backends.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.workspaceId"><span aria-hidden="true">|</span><code>workspaceId</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;default&#x27;</code></td><td class="helios-api-param-description">Workspace namespace for persisted preferences and sessions.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.persistNetwork"><span aria-hidden="true">|</span><code>persistNetwork</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Persist the network payload as part of browser/native session saves.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.networkPersistence"><span aria-hidden="true">|</span><code>networkPersistence</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Network payload persistence policy, size limits, and backend-specific options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.positionPersistence"><span aria-hidden="true">|</span><code>positionPersistence</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Separate layout-position persistence policy for storage backends that support split payloads.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.sessionThumbnail"><span aria-hidden="true">|</span><code>sessionThumbnail</code></span></td><td class="helios-api-param-type"><code>boolean</code>|<code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Thumbnail capture policy for saved sessions.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.suppressBrowserGestures"><span aria-hidden="true">|</span><code>suppressBrowserGestures</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Prevent native browser pan, zoom, and selection gestures over the visualization.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.autoCleanup"><span aria-hidden="true">|</span><code>autoCleanup</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Destroy this Helios instance when its root or container is removed from the DOM.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.disposeNetworkOnDestroy"><span aria-hidden="true">|</span><code>disposeNetworkOnDestroy</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Dispose the active network when <code>destroy()</code> runs.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.manualRendering"><span aria-hidden="true">|</span><code>manualRendering</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Disable automatic scheduler rendering so the host application can request frames explicitly.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.maxFps"><span aria-hidden="true">|</span><code>maxFps</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional scheduler FPS cap.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.powerPreference"><span aria-hidden="true">|</span><code>powerPreference</code></span></td><td class="helios-api-param-type">&#x27;<code>high</code>-<code>performance</code>&#x27;|&#x27;<code>low</code>-<code>power</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;high-performance&#x27;</code></td><td class="helios-api-param-description">Preferred GPU class for WebGL and WebGPU initialization.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.webglContextAttributes"><span aria-hidden="true">|</span><code>webglContextAttributes</code></span></td><td class="helios-api-param-type"><code>WebGLContextAttributes</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Extra WebGL2 context attributes merged over Helios defaults.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.webgpuAdapterOptions"><span aria-hidden="true">|</span><code>webgpuAdapterOptions</code></span></td><td class="helios-api-param-type"><code>GPURequestAdapterOptions</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Extra WebGPU adapter options merged over Helios defaults.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.webgpuDeviceDescriptor"><span aria-hidden="true">|</span><code>webgpuDeviceDescriptor</code></span></td><td class="helios-api-param-type"><code>GPUDeviceDescriptor</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Extra WebGPU device descriptor options. Explicit <code>requiredLimits</code> are merged with Helios&#x27; graph-oriented limit requests.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.webgpuCanvasConfiguration"><span aria-hidden="true">|</span><code>webgpuCanvasConfiguration</code></span></td><td class="helios-api-param-type"><code>Partial</code>&lt;<code>GPUCanvasConfiguration</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Extra WebGPU canvas configuration values merged over Helios defaults.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.supersampling"><span aria-hidden="true">|</span><code>supersampling</code></span></td><td class="helios-api-param-type"><code>boolean</code>|<code>string</code>|<code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Canvas supersampling mode or scale factor.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.theme"><span aria-hidden="true">|</span><code>theme</code></span></td><td class="helios-api-param-type">&#x27;<code>dark</code>&#x27;|&#x27;<code>light</code>&#x27;|<code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Initial renderer/UI theme. When omitted, Helios follows <code>data-helios-theme</code>, <code>data-theme</code>, <code>data-md-color-scheme</code>, or the browser color-scheme preference.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.background"><span aria-hidden="true">|</span><code>background</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Renderer background color. Takes precedence over theme-derived defaults.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.clearColor"><span aria-hidden="true">|</span><code>clearColor</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Renderer clear color. Takes precedence over theme-derived defaults.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Visualization controller with a <code>ready</code> promise that resolves after renderer, scheduler, layers, behaviors, and initial geometry are initialized.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
`options.container` should be an element or selector that already
has stable dimensions. `options.renderer` can prefer `webgpu` or `webgl`;
Helios falls back according to renderer availability. Built-in behaviors are
attached by default; `options.behaviors` accepts behavior options or custom
behavior instances when an app needs to tune or extend them. Set
`suppressBrowserGestures: true` for touch-first embedded canvases. Helios
automatically destroys itself when its root or container is removed from the
DOM unless `options.autoCleanup` is `false`. Destroying Helios disposes the
current network by default; pass `disposeNetworkOnDestroy: false` when the
application will keep using the same network after unmount.
</div>

## Static Properties { #api-static-properties .helios-api-section-title }

<p class="helios-api-section-description">Constants and metadata exposed directly on the class.</p>

<a id="property-states" class="helios-api-member-anchor"></a>

### `STATES` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:2244</code></p>
<p>Built-in bit flags used by node and edge interaction state.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>State bit constants for filtered, selected, and highlighted items.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

<a id="property-state_bits" class="helios-api-member-anchor"></a>

### `STATE_BITS` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:2257</code></p>
<p>Alias for <code>STATES</code> kept for compatibility with earlier public APIs.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>State bit constants.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

<a id="property-ui_bindings" class="helios-api-member-anchor"></a>

### `UI_BINDINGS` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:2266</code></p>
<p>Metadata describing settings that can be bound to controls in the UI.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>UI binding descriptors keyed by Helios setting name.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-initialize" class="helios-api-member-anchor"></a>

### `initialize()` &rarr; &#123;Promise&lt;void&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8257</code></p>
<p>Initialize layout, renderer, picking, attribute tracking, and scheduler state.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Resolves when the first renderer and layout setup is complete.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>void</code>&gt;</span></div>
<h4>Notes</h4>
<p>The constructor calls this automatically and exposes the promise as <code>helios.ready</code>; applications usually await <code>ready</code> instead of calling this directly.</p>
</div>

<a id="method-prewarm" class="helios-api-member-anchor"></a>

### `prewarm(options = {})` &rarr; &#123;Promise&lt;void&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12610</code></p>
<p>Pre-runs mapper application before first render. Useful for large graphs where the first geometry pass is expensive. Can be awaited before <code>helios.ready</code> to shorten time to first render.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Reserved for future prewarm controls.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Resolves when mapper prewarm work has completed.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>void</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.prewarm({
  enabled: true,
});
</code></pre>
</div>

<a id="method-destroy" class="helios-api-member-anchor"></a>

### `destroy()` &rarr; &#123;void&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:15281</code></p>
<p>Dispose renderer resources, UI bindings, workers, timers, and event listeners owned by this instance.</p>
<h4>Returns</h4>
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> <code>void</code></span></div>
</div>

## Behaviors { #api-behaviors .helios-api-section-title }

<p class="helios-api-section-description">Behavior registration and state. Built-in behavior implementations are documented under <a href="section-behaviors.md">Behaviors</a>.</p>

<a id="method-hasbehavior" class="helios-api-member-anchor"></a>

### `hasBehavior(name)` &rarr; &#123;boolean&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:3858</code></p>
<p>Check whether a behavior is active or registered.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Behavior id.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>True when the behavior is active or available in the registry.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code></span></div>
</div>

<a id="method-getbehavior" class="helios-api-member-anchor"></a>

### `getBehavior(name)` &rarr; &#123;Behavior|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:3872</code></p>
<p>Return an active behavior, lazily creating registered built-ins when needed.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Behavior id.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Active behavior instance, or <code>null</code> when unavailable.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Behavior/"><code>Behavior</code></a>|<code>null</code></span></div>
</div>

<a id="method-registerbehavior" class="helios-api-member-anchor"></a>

### `registerBehavior(name, behaviorCtor)` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:3890</code></p>
<p>Register a behavior constructor or factory for later activation.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Behavior id.</td></tr>
<tr><td class="helios-api-param-name"><code>behaviorCtor</code></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Constructor or factory that creates a behavior.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-usebehavior" class="helios-api-member-anchor"></a>

### `useBehavior(name, behaviorOrOptions)` &rarr; &#123;Behavior&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:3907</code></p>
<p>Activate a behavior, update an existing behavior, or return the active one.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Behavior id.</td></tr>
<tr><td class="helios-api-param-name"><code>behaviorOrOptions</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/Behavior/"><code>Behavior</code></a>|<code>Object</code>|<code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Behavior instance, behavior options, or <code>true</code> to activate with defaults.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Active behavior instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Behavior/"><code>Behavior</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const selection = helios.useBehavior(&#x27;selection&#x27;, { multiple: true });
</code></pre>
</div>

<a id="method-serializebehaviorstate" class="helios-api-member-anchor"></a>

### `serializeBehaviorState()` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7023</code></p>
<p>Serialize state held by active behaviors.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Behavior state keyed by behavior id.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

<a id="method-restorebehaviorstate" class="helios-api-member-anchor"></a>

### `restoreBehaviorState(snapshot = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7035</code></p>
<p>Restore state for active behaviors.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Behavior state keyed by behavior id.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-getgraphfilter" class="helios-api-member-anchor"></a>

### `getGraphFilter()` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6446</code></p>
<p>Return the active graph filter state and filtered graph sizes.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Filter state with <code>enabled</code>, <code>scope</code>, normalized <code>options</code>, filtered/base node and edge counts, and the last filter error.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const state = helios.getGraphFilter();
if (state.enabled) console.log(state.nodeCount, state.edgeCount);
</code></pre>
</div>

<a id="method-graphfilter" class="helios-api-member-anchor"></a>

### `graphFilter(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6479</code></p>
<p>Read or replace the active graph filter.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>false</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Filter options, <code>false</code>, or <code>null</code>. Omit the argument to read the current state.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current filter state when called without arguments, otherwise this Helios instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.graphFilter({
  nodeRules: [{ attribute: &#x27;degree&#x27;, operator: &#x27;&gt;=&#x27;, value: 3 }],
  scope: &#x27;render&#x27;,
});
</code></pre>
</div>

<a id="method-setgraphfilter" class="helios-api-member-anchor"></a>

### `setGraphFilter(options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6508</code></p>
<p>Apply a render or render-and-layout graph filter.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<a href="/docs/api/helios-web/HeliosFilter/"><code>HeliosFilter</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Filter rule set or reusable <code>HeliosFilter</code> instance.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.nodeRules"><span aria-hidden="true">|</span><code>nodeRules</code></span></td><td class="helios-api-param-type"><code>Array</code>.&lt;<code>Object</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node rules to apply.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.edgeRules"><span aria-hidden="true">|</span><code>edgeRules</code></span></td><td class="helios-api-param-type"><code>Array</code>.&lt;<code>Object</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge rules to apply.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.scope"><span aria-hidden="true">|</span><code>scope</code></span></td><td class="helios-api-param-type">&#x27;<code>render</code>&#x27;|&#x27;<code>render</code>+<code>layout</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Filter scope.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Notes</h4>
<p><code>render</code> hides filtered items without changing dynamic layout forces. <code>render+layout</code> also feeds the filtered graph to the active layout.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setGraphFilter({
  nodeRules: [{ attribute: &#x27;group&#x27;, operator: &#x27;==&#x27;, value: &#x27;core&#x27; }],
  scope: &#x27;render+layout&#x27;,
});
</code></pre>
</div>

<a id="method-activateheliosfilter" class="helios-api-member-anchor"></a>

### `activateHeliosFilter(filter)` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6560</code></p>
<p>Activate a reusable <code>HeliosFilter</code> instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>filter</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/HeliosFilter/"><code>HeliosFilter</code></a>|<code>null</code>|<code>false</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Filter instance to activate, or <code>null</code>/<code>false</code> to clear filtering.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const filter = new HeliosFilter({ nodeRules: [{ attribute: &#x27;kind&#x27;, value: &#x27;paper&#x27; }] });
helios.activateHeliosFilter(filter);
</code></pre>
</div>

<a id="method-getactiveheliosfilter" class="helios-api-member-anchor"></a>

### `getActiveHeliosFilter()` &rarr; &#123;HeliosFilter|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6578</code></p>
<p>Return the reusable filter currently attached to this view.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Active reusable filter, if one was supplied.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/HeliosFilter/"><code>HeliosFilter</code></a>|<code>null</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getActiveHeliosFilter();
</code></pre>
</div>

<a id="method-reapplyactiveheliosfilter" class="helios-api-member-anchor"></a>

### `reapplyActiveHeliosFilter()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6589</code></p>
<p>Re-run the active reusable filter after its rules or source data changed.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-cleargraphfilter" class="helios-api-member-anchor"></a>

### `clearGraphFilter()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6603</code></p>
<p>Remove the active graph filter and restore the base graph view.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.clearGraphFilter();
</code></pre>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-replacenetwork" class="helios-api-member-anchor"></a>

### `replaceNetwork(nextNetwork, options = {})` &rarr; &#123;Promise&lt;Helios&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6642</code></p>
<p>Replace the graph store while preserving visualization state by default.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nextNetwork</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Replacement graph.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Replacement behavior options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.disposeOld"><span aria-hidden="true">|</span><code>disposeOld</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Dispose the previous network.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.keepCamera"><span aria-hidden="true">|</span><code>keepCamera</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Preserve the current camera.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.keepMappers"><span aria-hidden="true">|</span><code>keepMappers</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Preserve mapper settings.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.markNetworkDirty"><span aria-hidden="true">|</span><code>markNetworkDirty</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Mark persistence network data dirty after replacement.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance after the renderer and layout are rebound to the new graph.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
await helios.replaceNetwork(nextNetwork, { keepCamera: false });
</code></pre>
</div>

<a id="method-loadnetwork" class="helios-api-member-anchor"></a>

### `loadNetwork(source, options = {})` &rarr; &#123;Promise&lt;HeliosNetwork&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6908</code></p>
<p>Load a serialized network and replace the active graph.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>source</code></td><td class="helios-api-param-type"><code>Blob</code>|<code>ArrayBuffer</code>|<code>string</code>|<code>File</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Network payload or file-like object.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Load and replacement options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.format"><span aria-hidden="true">|</span><code>format</code></span></td><td class="helios-api-param-type">&#x27;<code>xnet</code>&#x27;|&#x27;<code>zxnet</code>&#x27;|&#x27;<code>bxnet</code>&#x27;|&#x27;<code>gml</code>&#x27;|&#x27;<code>gt</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Input format when it cannot be inferred from <code>source.name</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Loaded network instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const network = await helios.loadNetwork(file, { format: &#x27;bxnet&#x27; });
</code></pre>
</div>

<a id="method-savenetwork" class="helios-api-member-anchor"></a>

### `saveNetwork(format = 'bxnet', options = {})` &rarr; &#123;Promise&lt;Blob|string|ArrayBuffer&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6985</code></p>
<p>Serialize the active graph in a Helios Network format.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>format</code></td><td class="helios-api-param-type">&#x27;<code>xnet</code>&#x27;|&#x27;<code>zxnet</code>&#x27;|&#x27;<code>bxnet</code>&#x27;|&#x27;<code>gml</code>&#x27;|&#x27;<code>gt</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;bxnet&#x27;</code></td><td class="helios-api-param-description">Output format.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Save options forwarded to the network serializer.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Serialized network payload.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Blob</code>|<code>string</code>|<code>ArrayBuffer</code>&gt;</span></div>
</div>

<a id="method-serializevisualizationstate" class="helios-api-member-anchor"></a>

### `serializeVisualizationState(options = {})` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7084</code></p>
<p>Build a portable visualization-state envelope.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Serialization options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Visualization-state envelope containing UI, behavior, camera, and network-source state.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.serializeVisualizationState({
  enabled: true,
});
</code></pre>
</div>

<a id="method-serializevisualizationstateasync" class="helios-api-member-anchor"></a>

### `serializeVisualizationStateAsync(options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7111</code></p>
<p>Build a portable visualization-state envelope and await async layout snapshots.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Serialization options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Visualization-state envelope containing UI, behavior, camera, network-source, storage, and async layout runtime state.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.serializeVisualizationStateAsync({
  enabled: true,
});
</code></pre>
</div>

<a id="method-importvisualizationstate" class="helios-api-member-anchor"></a>

### `importVisualizationState(source, options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7137</code></p>
<p>Import a visualization-state envelope and apply it to this view.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>source</code></td><td class="helios-api-param-type"><code>Object</code>|<code>string</code>|<code>Blob</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visualization-state envelope or JSON payload.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Restore options forwarded to behaviors.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Parsed persistence envelope.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
</div>

<a id="method-restorevisualizationstate" class="helios-api-member-anchor"></a>

### `restoreVisualizationState(source, options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7214</code></p>
<p>Alias for <code>importVisualizationState</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>source</code></td><td class="helios-api-param-type"><code>Object</code>|<code>string</code>|<code>Blob</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visualization-state envelope or JSON payload.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Restore options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Parsed persistence envelope.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
</div>

<a id="method-exportvisualizationstate" class="helios-api-member-anchor"></a>

### `exportVisualizationState(options = {})` &rarr; &#123;Object|string|Blob&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7227</code></p>
<p>Export visualization state as an object, JSON string, or Blob.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Export options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.format"><span aria-hidden="true">|</span><code>format</code></span></td><td class="helios-api-param-type">&#x27;<code>Object</code>&#x27;|&#x27;<code>string</code>&#x27;|&#x27;<code>blob</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;object&#x27;</code></td><td class="helios-api-param-description">Output shape.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Visualization-state payload.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>string</code>|<code>Blob</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.exportVisualizationState({
  enabled: true,
});
</code></pre>
</div>

<a id="method-serializetrackedvisualizationstate" class="helios-api-member-anchor"></a>

### `serializeTrackedVisualizationState(options = {})` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7246</code></p>
<p>Build a sparse visualization-state envelope from tracked state overrides.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Serialization options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.includeLayoutRuntime"><span aria-hidden="true">|</span><code>includeLayoutRuntime</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Include layout runtime state.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Sparse visualization-state envelope suitable for portable state attachment.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.serializeTrackedVisualizationState({
  enabled: true,
});
</code></pre>
</div>

<a id="method-serializetrackedvisualizationstateasync" class="helios-api-member-anchor"></a>

### `serializeTrackedVisualizationStateAsync(options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7275</code></p>
<p>Build a sparse visualization-state envelope and await async layout snapshots.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Serialization options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.includeLayoutRuntime"><span aria-hidden="true">|</span><code>includeLayoutRuntime</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Include layout runtime state.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Sparse visualization-state envelope suitable for portable state attachment.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.serializeTrackedVisualizationStateAsync({
  enabled: true,
});
</code></pre>
</div>

<a id="method-getattachedvisualizationstate" class="helios-api-member-anchor"></a>

### `getAttachedVisualizationState(network = this.network, options = {})` &rarr; &#123;Object|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7304</code></p>
<p>Read a visualization-state envelope stored on a network attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>this.network</code></td><td class="helios-api-param-description">Network to inspect.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute lookup options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Parsed envelope, or <code>null</code> when no valid state is attached.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code></span></div>
</div>

<a id="method-attachvisualizationstatetonetwork" class="helios-api-member-anchor"></a>

### `attachVisualizationStateToNetwork(snapshot = null, options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7325</code></p>
<p>Store visualization state on a network string attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Existing envelope, or <code>null</code> to capture current state.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attachment options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-clearattachedvisualizationstate" class="helios-api-member-anchor"></a>

### `clearAttachedVisualizationState(options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7345</code></p>
<p>Remove visualization state attached to the active network.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute removal options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.clearAttachedVisualizationState({
  enabled: true,
});
</code></pre>
</div>

<a id="method-saveportablenetwork" class="helios-api-member-anchor"></a>

### `savePortableNetwork(format = 'bxnet', options = {})` &rarr; &#123;Promise&lt;Blob|string|ArrayBuffer&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7364</code></p>
<p>Save the graph with optional embedded visualization state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>format</code></td><td class="helios-api-param-type">&#x27;<code>xnet</code>&#x27;|&#x27;<code>zxnet</code>&#x27;|&#x27;<code>bxnet</code>&#x27;|&#x27;<code>gml</code>&#x27;|&#x27;<code>gt</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;bxnet&#x27;</code></td><td class="helios-api-param-description">Output network format.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Portable save options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.includeVisualization"><span aria-hidden="true">|</span><code>includeVisualization</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Attach current visualization state before saving.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Serialized network payload.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Blob</code>|<code>string</code>|<code>ArrayBuffer</code>&gt;</span></div>
</div>

<a id="method-addnodes" class="helios-api-member-anchor"></a>

### `addNodes(count, initializer)` &rarr; &#123;Uint32Array&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12687</code></p>
<p>Add nodes to the backing network and initialize their visual state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>count</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Number of nodes to add.</td></tr>
<tr><td class="helios-api-param-name"><code>initializer</code></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional callback receiving created node ids and the visual attribute manager.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created node indices.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Uint32Array</code></span></div>
</div>

<a id="method-addedges" class="helios-api-member-anchor"></a>

### `addEdges(edges, initializer)` &rarr; &#123;Uint32Array&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12716</code></p>
<p>Add edges to the backing network and initialize their visual state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>edges</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>Array</code>&lt;<code>number</code>&gt;&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge pairs to insert.</td></tr>
<tr><td class="helios-api-param-name"><code>initializer</code></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional callback receiving created edge ids and the visual attribute manager.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created edge indices.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Uint32Array</code></span></div>
</div>

## Figure Export { #api-figure-export .helios-api-section-title }

<p class="helios-api-section-description">High-resolution figure capture and download. <a href="ExporterBehavior.md">ExporterBehavior</a> provides the built-in export interface.</p>

<a id="method-getfigureexportcapabilities" class="helios-api-member-anchor"></a>

### `getFigureExportCapabilities(options = {})` &rarr; &#123;{maxBitmapDimension:number,maxFigureDimension:number,defaultPreset:string,presets:Array.&lt;Object&gt;}&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7552</code></p>
<p>Return renderer-aware figure export limits and preset availability.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type">{<code>supersampling</code>?: <code>number</code>|<code>string</code>}</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Supersampling request used when computing max safe output dimensions.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Export capability record for the current renderer and viewport.</p><span class="helios-api-return-type"><strong>Type</strong> {<code>maxBitmapDimension</code>:<code>number</code>,<code>maxFigureDimension</code>:<code>number</code>,<code>defaultPreset</code>:<code>string</code>,<code>presets</code>:<code>Array</code>.&lt;<code>Object</code>&gt;}</span></div>
<h4>Notes</h4>
<p>WebGL and WebGPU expose different maximum texture dimensions, so this method should be called after <code>await helios.ready</code> and whenever supersampling changes.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.getFigureExportCapabilities({
  enabled: true,
});
</code></pre>
</div>

<a id="method-exportfigureblob" class="helios-api-member-anchor"></a>

### `exportFigureBlob(options = {})` &rarr; &#123;Promise&lt;Blob&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:7973</code></p>
<p>Capture the current visualization as a PNG or SVG <code>Blob</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Figure export options including <code>format</code>, <code>preset</code>, <code>width</code>, <code>height</code>, <code>supersampling</code>, <code>includeLabels</code>, <code>includeLegends</code>, <code>includeInterface</code>, <code>transparentBackground</code>, and <code>legendScale</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Image blob for the requested figure.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Blob</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const blob = await helios.exportFigureBlob({
  format: &#x27;png&#x27;,
  width: 1920,
  height: 1080,
  includeLabels: true,
  includeLegends: true,
});
</code></pre>
</div>

<a id="method-exportfigurepreviewblob" class="helios-api-member-anchor"></a>

### `exportFigurePreviewBlob(options = {}, previewOptions = {})` &rarr; &#123;Promise&lt;Blob&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8013</code></p>
<p>Capture a scaled PNG preview for a full-size figure export request.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Full export options that should be previewed.</td></tr>
<tr><td class="helios-api-param-name"><code>previewOptions</code></td><td class="helios-api-param-type">{<code>maxWidth</code>?:<code>number</code>,<code>maxHeight</code>?:<code>number</code>,<code>supersampling</code>?:<code>number</code>|<code>string</code>}</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Preview output constraints.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>PNG preview blob.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Blob</code>&gt;</span></div>
<h4>Notes</h4>
<p>Preview capture keeps the full export&#x27;s framing and overlay intent while using smaller raster dimensions for UI previews.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.exportFigurePreviewBlob({
  enabled: true,
});
</code></pre>
</div>

<a id="method-exportfigure" class="helios-api-member-anchor"></a>

### `exportFigure(filenameOrOptions, maybeOptions = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8066</code></p>
<p>Capture and download the current visualization.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>filenameOrOptions</code></td><td class="helios-api-param-type"><code>string</code>|<code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Download filename or figure export options.</td></tr>
<tr><td class="helios-api-param-name"><code>maybeOptions</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Figure export options when the first argument is a filename.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Download metadata containing <code>blob</code>, <code>filename</code>, <code>format</code>, logical dimensions, bitmap dimensions, and supersampling.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
<h4>Notes</h4>
<p>In non-browser runtimes the method still creates the figure blob and returns metadata, but no download link is clicked.</p>
</div>

## Events { #api-events .helios-api-section-title }

<p class="helios-api-section-description">Event subscription helpers and emitted interaction events.</p>

<a id="method-on" class="helios-api-member-anchor"></a>

### `on(type, handler, options)` &rarr; &#123;Function&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8109</code></p>
<p>Add an event listener and receive an unsubscribe function.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Event type, usually one of the <code>EVENTS</code> constants.</td></tr>
<tr><td class="helios-api-param-name"><code>handler</code></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Listener function.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">DOM <code>addEventListener</code> options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Function that removes the listener.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Function</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const unsubscribe = helios.on(EVENTS.NODE_CLICK, (event) =&gt; {
  console.log(event.detail.index);
});
</code></pre>
</div>

<a id="method-listen" class="helios-api-member-anchor"></a>

### `listen(typeWithNamespace, handler, options)` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8137</code></p>
<p>Add or replace a namespaced event listener.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>typeWithNamespace</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Event type, optionally followed by <code>.namespace</code> for replacement/removal.</td></tr>
<tr><td class="helios-api-param-name"><code>handler</code></td><td class="helios-api-param-type"><code>Function</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Listener function, or <code>null</code> to remove.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">DOM listener options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.listen(`${EVENTS.NODE_HOVER}.tooltip`, ({ detail }) =&gt; {
  updateTooltip(detail);
});
</code></pre>
</div>

<a id="method-off" class="helios-api-member-anchor"></a>

### `off(type, handler, options)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8195</code></p>
<p>Remove an event listener.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Event type.</td></tr>
<tr><td class="helios-api-param-name"><code>handler</code></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Listener function originally registered.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">DOM listener options.</td></tr>
</tbody>
</table>
</div>

<a id="method-onany" class="helios-api-member-anchor"></a>

### `onAny(handler, options)` &rarr; &#123;Function&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8208</code></p>
<p>Observe every event emitted through Helios.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>handler</code></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Listener receiving <code>{ type, detail, event, target }</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Listener options, including <code>signal</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Function that removes the listener.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Function</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const stop = helios.onAny(EVENTS.NODE_CLICK, (event) =&gt; {
  console.log(event.detail);
});
</code></pre>
</div>

<a id="method-emit" class="helios-api-member-anchor"></a>

### `emit(type, detail)` &rarr; &#123;CustomEvent&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8232</code></p>
<p>Dispatch a Helios event.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Event type.</td></tr>
<tr><td class="helios-api-param-name"><code>detail</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Event detail payload.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Dispatched event object.</p><span class="helios-api-return-type"><strong>Type</strong> <code>CustomEvent</code></span></div>
</div>

## Camera And View { #api-camera-and-view .helios-api-section-title }

<p class="helios-api-section-description">Camera framing, target following, dimensional mode, and transitions. <a href="InterfaceBehavior.md">InterfaceBehavior</a> can expose these controls.</p>

<a id="method-requestframenetwork" class="helios-api-member-anchor"></a>

### `requestFrameNetwork(options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6829</code></p>
<p>Queue a camera fit once the renderer and graph bounds are ready.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Camera fit options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.maxAttempts"><span aria-hidden="true">|</span><code>maxAttempts</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>25</code></td><td class="helios-api-param-description">Maximum geometry ticks to retry.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.requestFrameNetwork({
  enabled: true,
});
</code></pre>
</div>

<a id="method-framenetwork" class="helios-api-member-anchor"></a>

### `frameNetwork(options = {})` &rarr; &#123;boolean&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:6863</code></p>
<p>Fit the camera to the current visible graph or selected node set.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Camera fit options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.nodeIndices"><span aria-hidden="true">|</span><code>nodeIndices</code></span></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node indices to frame.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.animate"><span aria-hidden="true">|</span><code>animate</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Animate the transition.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.paddingRatio"><span aria-hidden="true">|</span><code>paddingRatio</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Extra viewport padding ratio.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>True when a camera pose was applied.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.frameNetwork({ animate: true, paddingRatio: 0.08 });
</code></pre>
</div>

<a id="method-camerapose" class="helios-api-member-anchor"></a>

### `cameraPose()` &rarr; &#123;Object|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10977</code></p>
<p>Capture the current camera pose.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Serializable camera pose, or <code>null</code> before a renderer is available.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code></span></div>
</div>

<a id="method-cameracontrols" class="helios-api-member-anchor"></a>

### `cameraControls(options, stateOptions = {})` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10990</code></p>
<p>Read or update automatic camera-control policy.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Camera-control fields to update. Omit to read the current snapshot.</td></tr>
<tr><td class="helios-api-param-name"><code>stateOptions</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State tracking options for persistence-aware writes.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current camera-control snapshot when called without arguments; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.cameraControls({
  enabled: true,
});
</code></pre>
</div>

<a id="method-cameratargetnodes" class="helios-api-member-anchor"></a>

### `cameraTargetNodes(nodeIndices, options = {})` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11052</code></p>
<p>Focus the camera on a set of node indices.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeIndices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node indices to target. Omit to read the current target list.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Focus, zoom, animation, and follow options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current target list when called without arguments; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.cameraTargetNodes([0, 1, 2]);
</code></pre>
</div>

<a id="method-camerafollownodes" class="helios-api-member-anchor"></a>

### `cameraFollowNodes(nodeIndices, options = {})` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11107</code></p>
<p>Keep the camera centered on moving node indices.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeIndices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node indices to follow. Pass an empty list to disable following.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Follow interval, framing, zoom, and animation options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current followed node list when called without arguments; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.cameraFollowNodes([0, 1, 2]);
</code></pre>
</div>

<a id="method-setcamerapose" class="helios-api-member-anchor"></a>

### `setCameraPose(pose, options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11149</code></p>
<p>Apply a camera pose immediately.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>pose</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Camera pose fields to merge into the current pose.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Render, state tracking, and manual-interaction options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-transitioncamera" class="helios-api-member-anchor"></a>

### `transitionCamera(pose, options = {})` &rarr; &#123;Promise&lt;Helios&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11211</code></p>
<p>Animate the camera from its current pose to a target pose.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>pose</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Target camera pose fields.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Transition duration, starting pose, render, and interaction options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance after the transition completes.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a>&gt;</span></div>
</div>

<a id="method-stopcameratransition" class="helios-api-member-anchor"></a>

### `stopCameraTransition()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11241</code></p>
<p>Stop any active camera transition.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-mode" class="helios-api-member-anchor"></a>

### `mode()` &rarr; &#123;&#x27;2d&#x27;|&#x27;3d&#x27;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11253</code></p>
<p>Return the active dimensional rendering mode.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current camera/rendering mode.</p><span class="helios-api-return-type"><strong>Type</strong> &#x27;2d&#x27;|&#x27;3d&#x27;</span></div>
</div>

<a id="method-setmode" class="helios-api-member-anchor"></a>

### `setMode(mode, options = {})` &rarr; &#123;Promise&lt;Helios&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11266</code></p>
<p>Switch between 2D and 3D rendering modes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type">&#x27;2d&#x27;|&#x27;3d&#x27;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Target dimensional mode.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Animation, delegate-sync, and camera framing options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance after the mode switch completes.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
await helios.setMode(&#x27;2d&#x27;);
</code></pre>
</div>

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-createlayout" class="helios-api-member-anchor"></a>

### `createLayout(layoutOption)` &rarr; &#123;Layout&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12642</code></p>
<p>Create a layout instance from a layout option object or return an existing layout.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>layoutOption</code></td><td class="helios-api-param-type"><code>Object</code>|<code>Layout</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Layout instance or descriptor such as <code>{ type: &#x27;gpu-force&#x27; }</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Layout instance bound to the current render network.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Layout</code></span></div>
</div>

<a id="method-layout" class="helios-api-member-anchor"></a>

### `layout(layout)` &rarr; &#123;Layout|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13432</code></p>
<p>Read or replace the active layout instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>layout</code></td><td class="helios-api-param-type"><code>Layout</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Layout instance extending the Helios layout base class.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current layout when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Layout</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-getlayoutpositionattributechoices" class="helios-api-member-anchor"></a>

### `getLayoutPositionAttributeChoices(options = {})` &rarr; &#123;Array.&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13490</code></p>
<p>List node attributes that can seed layout positions.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Choice discovery options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.network"><span aria-hidden="true">|</span><code>network</code></span></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Network to inspect. Defaults to the active network.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.mode"><span aria-hidden="true">|</span><code>mode</code></span></td><td class="helios-api-param-type">&#x27;2d&#x27;|&#x27;3d&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mode used to label random seed choices.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Position choices with <code>value</code>, <code>label</code>, and <code>dimension</code> fields.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>.&lt;<code>Object</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.getLayoutPositionAttributeChoices({
  enabled: true,
});
</code></pre>
</div>

<a id="method-setlayoutpositionsfromnodeattribute" class="helios-api-member-anchor"></a>

### `setLayoutPositionsFromNodeAttribute(name, options = {})` &rarr; &#123;boolean&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13545</code></p>
<p>Copy a numeric node attribute into the canonical layout-position attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Source node attribute name, or the random seed choice value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Position-copy options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.network"><span aria-hidden="true">|</span><code>network</code></span></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Network to update. Defaults to the active network.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p><code>true</code> when positions were written.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code></span></div>
</div>

<a id="method-positions" class="helios-api-member-anchor"></a>

### `positions(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13680</code></p>
<p>Read or update the active position source used for rendering and layout handoff.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Position pipeline options, or <code>null</code> to reset to network-backed positions.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.source"><span aria-hidden="true">|</span><code>source</code></span></td><td class="helios-api-param-type">&#x27;<code>network</code>&#x27;|&#x27;<code>delegate</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Source for current positions.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.delegate"><span aria-hidden="true">|</span><code>delegate</code></span></td><td class="helios-api-param-type"><code>PositionDelegate</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Delegate used when <code>source</code> is <code>delegate</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current position source when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.positions({
  enabled: true,
});
</code></pre>
</div>

<a id="method-snapshotdelegatepositions" class="helios-api-member-anchor"></a>

### `snapshotDelegatePositions(options = {})` &rarr; &#123;Promise&lt;Float32Array|null&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13711</code></p>
<p>Snapshot all node positions from the active or supplied position delegate.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Delegate readback options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.delegate"><span aria-hidden="true">|</span><code>delegate</code></span></td><td class="helios-api-param-type"><code>PositionDelegate</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Delegate to read. Defaults to the active delegate.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Packed <code>x,y,z</code> positions, or <code>null</code> when no delegate is available.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Float32Array</code>|<code>null</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.snapshotDelegatePositions({
  enabled: true,
});
</code></pre>
</div>

<a id="method-snapshotnodepositions" class="helios-api-member-anchor"></a>

### `snapshotNodePositions(nodeIds, options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13739</code></p>
<p>Snapshot selected node positions from the active position source.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeIds</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node indices to read.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Readback options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.out"><span aria-hidden="true">|</span><code>out</code></span></td><td class="helios-api-param-type"><code>Float32Array</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional output buffer.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.delegate"><span aria-hidden="true">|</span><code>delegate</code></span></td><td class="helios-api-param-type"><code>PositionDelegate</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Delegate override.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Readback result with ids, packed positions, count, version, and source.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.snapshotNodePositions([0, 1, 2]);
</code></pre>
</div>

<a id="method-snapshotnodeposition" class="helios-api-member-anchor"></a>

### `snapshotNodePosition(nodeId, options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13816</code></p>
<p>Snapshot one node position from the active position source.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeId</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node index to read.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Readback options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.out"><span aria-hidden="true">|</span><code>out</code></span></td><td class="helios-api-param-type"><code>Float32Array</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional output buffer with length at least three.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Readback result with id, position, version, and source.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
</div>

<a id="method-snapshotnodecentroid" class="helios-api-member-anchor"></a>

### `snapshotNodeCentroid(nodeIds, options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13848</code></p>
<p>Compute the centroid of selected nodes from the active position source.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeIds</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node indices to include.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Readback options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.out"><span aria-hidden="true">|</span><code>out</code></span></td><td class="helios-api-param-type"><code>Float32Array</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional output buffer with length at least three.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Centroid result with centroid, count, version, and source.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.snapshotNodeCentroid([0, 1, 2]);
</code></pre>
</div>

<a id="method-syncdelegatepositionstonetwork" class="helios-api-member-anchor"></a>

### `syncDelegatePositionsToNetwork(options = {})` &rarr; &#123;Promise&lt;boolean&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13885</code></p>
<p>Write the active delegate position snapshot back into the network position attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Delegate synchronization options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.delegate"><span aria-hidden="true">|</span><code>delegate</code></span></td><td class="helios-api-param-type"><code>PositionDelegate</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Delegate to synchronize. Defaults to the active delegate.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p><code>true</code> when network positions were updated.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>boolean</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.syncDelegatePositionsToNetwork({
  enabled: true,
});
</code></pre>
</div>

<a id="method-interpolation" class="helios-api-member-anchor"></a>

### `interpolation(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13915</code></p>
<p>Read or update GPU position interpolation settings.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Interpolation options, mode string, or <code>null</code> to disable interpolation.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.enabled"><span aria-hidden="true">|</span><code>enabled</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable position interpolation.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.durationMode"><span aria-hidden="true">|</span><code>durationMode</code></span></td><td class="helios-api-param-type">&#x27;<code>adaptive</code>&#x27;|&#x27;<code>fixed</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Duration strategy.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.durationMs"><span aria-hidden="true">|</span><code>durationMs</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Fixed interpolation duration in milliseconds.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current interpolation snapshot when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.interpolation({
  enabled: true,
});
</code></pre>
</div>

<a id="method-setlayout" class="helios-api-member-anchor"></a>

### `setLayout(layout)` &rarr; &#123;Layout|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14065</code></p>
<p>Alias for <code>layout(layout)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>layout</code></td><td class="helios-api-param-type"><code>Layout</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Replacement layout.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>layout(layout)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Layout</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-setpositions" class="helios-api-member-anchor"></a>

### `setPositions(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14074</code></p>
<p>Alias for <code>positions(options)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Position pipeline options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>positions(options)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setPositions({
  enabled: true,
});
</code></pre>
</div>

<a id="method-setinterpolation" class="helios-api-member-anchor"></a>

### `setInterpolation(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14083</code></p>
<p>Alias for <code>interpolation(options)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>string</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Interpolation options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>interpolation(options)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setInterpolation({
  enabled: true,
});
</code></pre>
</div>

<a id="method-startlayout" class="helios-api-member-anchor"></a>

### `startLayout(algo = null, params = null)` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14226</code></p>
<p>Enable layout execution and optionally request a layout algorithm or parameters.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>algo</code></td><td class="helios-api-param-type"><code>string</code>|<code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Optional layout type or parameter object.</td></tr>
<tr><td class="helios-api-param-name"><code>params</code></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Optional parameters when <code>algo</code> is a string.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-stoplayout" class="helios-api-member-anchor"></a>

### `stopLayout(reason = 'user')` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14246</code></p>
<p>Disable layout execution.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;user&#x27;</code></td><td class="helios-api-param-description">Reason recorded for the scheduler state change.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

## Mappers { #api-mappers .helios-api-section-title }

<p class="helios-api-section-description">Mapper configuration for node and edge visual channels. <a href="MappersBehavior.md">MappersBehavior</a> handles mapper UI state.</p>

<a id="method-mappers" class="helios-api-member-anchor"></a>

### `mappers({ nodeMapper, edgeMapper } = {})` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13386</code></p>
<p>Read, replace, or reset the default node and edge mapper collections.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mappers</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mapper replacements. Omit to read active mapper collections.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="mappers.nodeMapper"><span aria-hidden="true">|</span><code>nodeMapper</code></span></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/Mapper/"><code>Mapper</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Replacement default node mapper.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="mappers.edgeMapper"><span aria-hidden="true">|</span><code>edgeMapper</code></span></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/Mapper/"><code>Mapper</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Replacement default edge mapper.</td></tr>
<tr><td class="helios-api-param-name"><code>nodeMapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>mappers</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>edgeMapper</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>mappers</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current mapper collections when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-setmappers" class="helios-api-member-anchor"></a>

### `setMappers(mappers)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14119</code></p>
<p>Alias for <code>mappers(mappers)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mappers</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Mapper replacements.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>mappers(mappers)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

## Appearance { #api-appearance .helios-api-section-title }

<p class="helios-api-section-description">Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.</p>

<a id="method-edgewidthscale" class="helios-api-member-anchor"></a>

### `edgeWidthScale(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10104</code></p>
<p>Read or set the multiplier applied to edge width attributes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge width scale multiplier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeWidthScale(1);
</code></pre>
</div>

<a id="method-edgewidthbase" class="helios-api-member-anchor"></a>

### `edgeWidthBase(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10117</code></p>
<p>Read or set the constant edge width added before scaling.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Base edge width in render units.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeWidthBase(1);
</code></pre>
</div>

<a id="method-edgeopacityscale" class="helios-api-member-anchor"></a>

### `edgeOpacityScale(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10130</code></p>
<p>Read or set the multiplier applied to edge opacity attributes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge opacity scale multiplier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeOpacityScale(1);
</code></pre>
</div>

<a id="method-edgeopacitybase" class="helios-api-member-anchor"></a>

### `edgeOpacityBase(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10143</code></p>
<p>Read or set the constant edge opacity added before scaling.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Base edge opacity.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeOpacityBase(1);
</code></pre>
</div>

<a id="method-nodeopacityscale" class="helios-api-member-anchor"></a>

### `nodeOpacityScale(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10156</code></p>
<p>Read or set the multiplier applied to node opacity attributes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node opacity scale multiplier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeOpacityScale(1);
</code></pre>
</div>

<a id="method-nodeopacitybase" class="helios-api-member-anchor"></a>

### `nodeOpacityBase(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10169</code></p>
<p>Read or set the constant node opacity added before scaling.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Base node opacity.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeOpacityBase(1);
</code></pre>
</div>

<a id="method-nodesizescale" class="helios-api-member-anchor"></a>

### `nodeSizeScale(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10182</code></p>
<p>Read or set the multiplier applied to node size attributes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node size scale multiplier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeSizeScale(true);
</code></pre>
</div>

<a id="method-nodesizebase" class="helios-api-member-anchor"></a>

### `nodeSizeBase(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10195</code></p>
<p>Read or set the constant node radius added before scaling.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Base node radius in render units.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeSizeBase(true);
</code></pre>
</div>

<a id="method-semanticzoomexponent" class="helios-api-member-anchor"></a>

### `semanticZoomExponent(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10208</code></p>
<p>Read or set semantic zoom compensation for node and label sizing.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Exponent controlling how strongly zoom affects apparent size.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.semanticZoomExponent(1);
</code></pre>
</div>

<a id="method-nodeoutlinewidthscale" class="helios-api-member-anchor"></a>

### `nodeOutlineWidthScale(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10223</code></p>
<p>Read or set the multiplier applied to node outline width attributes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node outline width scale multiplier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeOutlineWidthScale(1);
</code></pre>
</div>

<a id="method-nodeoutlinewidthbase" class="helios-api-member-anchor"></a>

### `nodeOutlineWidthBase(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10236</code></p>
<p>Read or set the constant node outline width added before scaling.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Base node outline width in render units.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeOutlineWidthBase(1);
</code></pre>
</div>

<a id="method-nodeoutlinecolor" class="helios-api-member-anchor"></a>

### `nodeOutlineColor(color)` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10249</code></p>
<p>Read or set the default node outline color.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS hex color or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current RGBA color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeOutlineColor(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-nodeoutlineuseattributes" class="helios-api-member-anchor"></a>

### `nodeOutlineUseAttributes(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10266</code></p>
<p>Read or set whether outline attributes participate in node styling.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable outline attribute mapping.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeOutlineUseAttributes(1);
</code></pre>
</div>

<a id="method-edgeendpointtrim" class="helios-api-member-anchor"></a>

### `edgeEndpointTrim(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10279</code></p>
<p>Read or set how far edge geometry is trimmed away from node centers.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Trim amount in node-radius units.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeEndpointTrim(1);
</code></pre>
</div>

<a id="method-edgewidthclamptonodediameter" class="helios-api-member-anchor"></a>

### `edgeWidthClampToNodeDiameter(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10292</code></p>
<p>Read or set whether rendered edge width is clamped by endpoint node diameter.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Clamp thick edges to avoid overpowering small nodes.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeWidthClampToNodeDiameter(1);
</code></pre>
</div>

<a id="method-nodeblendwithedges" class="helios-api-member-anchor"></a>

### `nodeBlendWithEdges(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10308</code></p>
<p>Read or set whether node rendering blends visually with adjacent edges.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable node/edge blending.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeBlendWithEdges(true);
</code></pre>
</div>

<a id="method-edgedepthwrite" class="helios-api-member-anchor"></a>

### `edgeDepthWrite(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10321</code></p>
<p>Read or set whether edge fragments write to the depth buffer.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable depth writes for edges.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeDepthWrite(true);
</code></pre>
</div>

<a id="method-edgefastrendering" class="helios-api-member-anchor"></a>

### `edgeFastRendering(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10334</code></p>
<p>Read or set the manual fast edge-rendering override.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable the fast edge rendering path.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeFastRendering(true);
</code></pre>
</div>

<a id="method-shadedenabled" class="helios-api-member-anchor"></a>

### `shadedEnabled(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10347</code></p>
<p>Read or set whether shaded rendering is enabled.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable lighting-based shading.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedEnabled(true);
</code></pre>
</div>

<a id="method-shadednodes" class="helios-api-member-anchor"></a>

### `shadedNodes(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10363</code></p>
<p>Read or set whether node geometry receives shaded lighting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable shading for nodes.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedNodes(true);
</code></pre>
</div>

<a id="method-shadededges" class="helios-api-member-anchor"></a>

### `shadedEdges(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10379</code></p>
<p>Read or set whether edge geometry receives shaded lighting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable shading for edges.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedEdges(true);
</code></pre>
</div>

<a id="method-shadedlightdirection" class="helios-api-member-anchor"></a>

### `shadedLightDirection(value)` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10395</code></p>
<p>Read or set the directional light vector used by shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Light direction as <code>[x,y,z]</code> or direction-like object.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current direction when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedLightDirection(1);
</code></pre>
</div>

<a id="method-shadedlightdirectionx" class="helios-api-member-anchor"></a>

### `shadedLightDirectionX(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10410</code></p>
<p>Read or set the x component of the shaded light direction.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">X component.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedLightDirectionX(1);
</code></pre>
</div>

<a id="method-shadedlightdirectiony" class="helios-api-member-anchor"></a>

### `shadedLightDirectionY(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10425</code></p>
<p>Read or set the y component of the shaded light direction.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Y component.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedLightDirectionY(1);
</code></pre>
</div>

<a id="method-shadedlightdirectionz" class="helios-api-member-anchor"></a>

### `shadedLightDirectionZ(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10440</code></p>
<p>Read or set the z component of the shaded light direction.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Z component.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedLightDirectionZ(1);
</code></pre>
</div>

<a id="method-shadedlightcolor" class="helios-api-member-anchor"></a>

### `shadedLightColor(color)` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10455</code></p>
<p>Read or set the direct light color used by shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS hex color or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current RGBA color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedLightColor(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-shadedambienttopcolor" class="helios-api-member-anchor"></a>

### `shadedAmbientTopColor(color)` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10474</code></p>
<p>Read or set the upper hemisphere ambient color for shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS hex color or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current RGBA color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedAmbientTopColor(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-shadedambientbottomcolor" class="helios-api-member-anchor"></a>

### `shadedAmbientBottomColor(color)` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10493</code></p>
<p>Read or set the lower hemisphere ambient color for shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS hex color or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current RGBA color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedAmbientBottomColor(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-shadeddiffusestrength" class="helios-api-member-anchor"></a>

### `shadedDiffuseStrength(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10512</code></p>
<p>Read or set diffuse lighting strength for shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Non-negative diffuse strength.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedDiffuseStrength(1);
</code></pre>
</div>

<a id="method-shadedambientstrength" class="helios-api-member-anchor"></a>

### `shadedAmbientStrength(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10530</code></p>
<p>Read or set ambient lighting strength for shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Non-negative ambient strength.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedAmbientStrength(1);
</code></pre>
</div>

<a id="method-shadedspecularcolor" class="helios-api-member-anchor"></a>

### `shadedSpecularColor(color)` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10548</code></p>
<p>Read or set the specular highlight color for shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS hex color or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current RGBA color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedSpecularColor(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-shadedspecularstrength" class="helios-api-member-anchor"></a>

### `shadedSpecularStrength(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10567</code></p>
<p>Read or set specular highlight strength for shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Non-negative specular strength.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedSpecularStrength(1);
</code></pre>
</div>

<a id="method-shadedshininess" class="helios-api-member-anchor"></a>

### `shadedShininess(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10585</code></p>
<p>Read or set specular shininess for shaded rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Shininess exponent.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.shadedShininess(1);
</code></pre>
</div>

<a id="method-ambientocclusionenabled" class="helios-api-member-anchor"></a>

### `ambientOcclusionEnabled(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10603</code></p>
<p>Read or set whether screen-space ambient occlusion is enabled.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable ambient occlusion when the renderer supports it.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionEnabled(true);
</code></pre>
</div>

<a id="method-ambientocclusionnodes" class="helios-api-member-anchor"></a>

### `ambientOcclusionNodes(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10619</code></p>
<p>Read or set whether ambient occlusion is applied to nodes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable node occlusion.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionNodes(true);
</code></pre>
</div>

<a id="method-ambientocclusionedges" class="helios-api-member-anchor"></a>

### `ambientOcclusionEdges(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10635</code></p>
<p>Read or set whether ambient occlusion is applied to edges.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable edge occlusion.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionEdges(true);
</code></pre>
</div>

<a id="method-ambientocclusionstrength" class="helios-api-member-anchor"></a>

### `ambientOcclusionStrength(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10651</code></p>
<p>Read or set ambient occlusion strength.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Non-negative occlusion strength.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionStrength(1);
</code></pre>
</div>

<a id="method-ambientocclusionradius" class="helios-api-member-anchor"></a>

### `ambientOcclusionRadius(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10669</code></p>
<p>Read or set ambient occlusion sampling radius.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Radius in screen-space sample units.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionRadius(1);
</code></pre>
</div>

<a id="method-ambientocclusionbias" class="helios-api-member-anchor"></a>

### `ambientOcclusionBias(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10687</code></p>
<p>Read or set ambient occlusion depth bias.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Non-negative depth bias.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionBias(1);
</code></pre>
</div>

<a id="method-ambientocclusionmode" class="helios-api-member-anchor"></a>

### `ambientOcclusionMode(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10705</code></p>
<p>Read or set ambient occlusion compositing mode.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Ambient occlusion mode identifier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current mode when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionMode(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-ambientocclusionintensityscale" class="helios-api-member-anchor"></a>

### `ambientOcclusionIntensityScale(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10725</code></p>
<p>Read or set ambient occlusion intensity scaling.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Non-negative intensity multiplier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionIntensityScale(1);
</code></pre>
</div>

<a id="method-ambientocclusionintensityshift" class="helios-api-member-anchor"></a>

### `ambientOcclusionIntensityShift(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10743</code></p>
<p>Read or set ambient occlusion intensity offset.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Non-negative intensity offset.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionIntensityShift(1);
</code></pre>
</div>

<a id="method-ambientocclusionquality" class="helios-api-member-anchor"></a>

### `ambientOcclusionQuality(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10761</code></p>
<p>Read or set ambient occlusion quality preset.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Ambient occlusion quality preset.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current quality when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.ambientOcclusionQuality(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-edgeadaptivequality" class="helios-api-member-anchor"></a>

### `edgeAdaptiveQuality(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10781</code></p>
<p>Read or update the adaptive edge-quality policy used to switch fast edge rendering on slow frames.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Adaptive quality configuration. Omit to read the current configuration and runtime status.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current policy snapshot when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeAdaptiveQuality({
  enabled: true,
});
</code></pre>
</div>

<a id="method-edgeadaptivequalityenabled" class="helios-api-member-anchor"></a>

### `edgeAdaptiveQualityEnabled(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10824</code></p>
<p>Read or set whether adaptive edge quality is enabled.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable adaptive edge quality.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeAdaptiveQualityEnabled(true);
</code></pre>
</div>

<a id="method-edgeadaptivequalityslowframethresholdms" class="helios-api-member-anchor"></a>

### `edgeAdaptiveQualitySlowFrameThresholdMs(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10838</code></p>
<p>Read or set the frame-time threshold that counts as slow for adaptive edge quality.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Slow-frame threshold in milliseconds.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeAdaptiveQualitySlowFrameThresholdMs(1);
</code></pre>
</div>

<a id="method-edgeadaptivequalityslowframeconsecutiveframes" class="helios-api-member-anchor"></a>

### `edgeAdaptiveQualitySlowFrameConsecutiveFrames(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10852</code></p>
<p>Read or set how many recent frames are averaged before adaptive quality changes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Frame sample window size.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeAdaptiveQualitySlowFrameConsecutiveFrames(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-edgeadaptivequalityprobeintervalms" class="helios-api-member-anchor"></a>

### `edgeAdaptiveQualityProbeIntervalMs(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10866</code></p>
<p>Read or set how often adaptive quality probes full-quality edge rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Probe interval in milliseconds.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeAdaptiveQualityProbeIntervalMs(1);
</code></pre>
</div>

<a id="method-edgeadaptivequalityinteractionholdms" class="helios-api-member-anchor"></a>

### `edgeAdaptiveQualityInteractionHoldMs(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10880</code></p>
<p>Read or set how long adaptive quality stays fast after interaction.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Hold duration in milliseconds.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeAdaptiveQualityInteractionHoldMs(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-edgeadaptivequalityfastduringcamera" class="helios-api-member-anchor"></a>

### `edgeAdaptiveQualityFastDuringCamera(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10894</code></p>
<p>Read or set whether camera interaction forces fast edge rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Use fast edges while the camera is moving.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeAdaptiveQualityFastDuringCamera(true);
</code></pre>
</div>

<a id="method-edgeadaptivequalityfastduringlayout" class="helios-api-member-anchor"></a>

### `edgeAdaptiveQualityFastDuringLayout(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10908</code></p>
<p>Read or set whether active layout ticks force fast edge rendering.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Use fast edges while layout is running.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeAdaptiveQualityFastDuringLayout(true);
</code></pre>
</div>

<a id="method-background" class="helios-api-member-anchor"></a>

### `background(color)` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10922</code></p>
<p>Read or set the renderer background color.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS hex color or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current RGBA color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.background(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-clearcolor" class="helios-api-member-anchor"></a>

### `clearColor(color)` &rarr; &#123;Array&lt;number&gt;|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10939</code></p>
<p>Alias for <code>background(color)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS hex color or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current RGBA color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.clearColor(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-supersampling" class="helios-api-member-anchor"></a>

### `supersampling(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:10952</code></p>
<p>Read or set the renderer supersampling preset.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type">&#x27;<code>auto</code>&#x27;|&#x27;<code>on</code>&#x27;|&#x27;<code>off</code>&#x27;|<code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Supersampling preset or legacy boolean.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current preset when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.supersampling(1);
</code></pre>
</div>

<a id="method-edgetransparencymode" class="helios-api-member-anchor"></a>

### `edgeTransparencyMode(mode)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11757</code></p>
<p>Read or set the edge transparency compositing mode.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Transparency mode supported by the active renderer.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current mode when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeTransparencyMode(&#x27;2d&#x27;);
</code></pre>
</div>

## Rendering And Picking { #api-rendering-and-picking .helios-api-section-title }

<p class="helios-api-section-description">Render requests, picking, framebuffer inspection, and attribute tracking. <a href="HoverBehavior.md">HoverBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> use these lower-level hooks.</p>

<a id="method-requestrender" class="helios-api-member-anchor"></a>

### `requestRender()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14258</code></p>
<p>Schedule a render frame.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-performrendering" class="helios-api-member-anchor"></a>

### `performRendering()` &rarr; &#123;void&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14270</code></p>
<p>Render one frame immediately when manual rendering is enabled.</p>
<h4>Returns</h4>
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> <code>void</code></span></div>
</div>

<a id="method-enableattributetracking" class="helios-api-member-anchor"></a>

### `enableAttributeTracking(nodeAttribute = '$index', edgeAttribute = null, options = {})` &rarr; &#123;AttributeTracker|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14319</code></p>
<p>Enable offscreen attribute tracking for picking.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>nodeAttribute</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;$index&#x27;</code></td><td class="helios-api-param-description">Node attribute to encode into the tracking target.</td></tr>
<tr><td class="helios-api-param-name"><code>edgeAttribute</code></td><td class="helios-api-param-type"><code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Edge attribute to encode into the tracking target.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Tracking resolution and auto-update options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Attribute tracker instance, or <code>null</code> before renderer initialization.</p><span class="helios-api-return-type"><strong>Type</strong> <code>AttributeTracker</code>|<code>null</code></span></div>
</div>

<a id="method-disableattributetracking" class="helios-api-member-anchor"></a>

### `disableAttributeTracking(scope)` &rarr; &#123;void&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14342</code></p>
<p>Disable attribute tracking for a scope or for all scopes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type">&#x27;<code>node</code>&#x27;|&#x27;<code>edge</code>&#x27;|<code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Scope to disable. Omit to disable all configured tracking.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> <code>void</code></span></div>
</div>

<a id="method-renderattributetracking" class="helios-api-member-anchor"></a>

### `renderAttributeTracking()` &rarr; &#123;Promise&lt;Object|null&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14353</code></p>
<p>Render the attribute-tracking target for the current frame.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Tracking render result, or <code>null</code> when tracking is disabled.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>|<code>null</code>&gt;</span></div>
</div>

<a id="method-pickattributesat" class="helios-api-member-anchor"></a>

### `pickAttributesAt(clientX, clientY)` &rarr; &#123;Promise&lt;{node:number, edge:number}&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14373</code></p>
<p>Pick encoded node and edge attributes at viewport coordinates.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>clientX</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Viewport x coordinate.</td></tr>
<tr><td class="helios-api-param-name"><code>clientY</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Viewport y coordinate.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Picked node and edge ids, or <code>-1</code> for misses.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;{<code>node</code>:<code>number</code>, <code>edge</code>:<code>number</code>}&gt;</span></div>
</div>

<a id="method-getframebufferversionsbyrefmap" class="helios-api-member-anchor"></a>

### `getFramebufferVersionsByRefMap()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14386</code></p>
<p>Returns a Map of framebuffer/attachment references to monotonically increasing &quot;version&quot; counters (wrapping at Number.MAX_SAFE_INTEGER). Keys are live object references (e.g. RenderTarget instances, WebGLFramebuffer, GPUTexture) so they can be used for identity comparisons.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getFramebufferVersionsByRefMap();
</code></pre>
</div>

<a id="method-getframebufferinformation" class="helios-api-member-anchor"></a>

### `getFramebufferInformation()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14428</code></p>
<p>Returns framebuffer/attachment information keyed by a meaningful name. Values include the version counter and a minimal shape description. Key format conventions: - <code>attributes.&lt;attributeName&gt;.&lt;scope&gt;.&lt;tracking|picking&gt;[.&lt;depth&gt;]</code> - <code>render.&lt;variation&gt;</code></p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getFramebufferInformation();
</code></pre>
</div>

<a id="method-getframebufferversions" class="helios-api-member-anchor"></a>

### `getFramebufferVersions()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14558</code></p>
<p>Returns an object keyed by a meaningful framebuffer name, where each value is the version counter. Key format conventions: - <code>attributes.&lt;attributeName&gt;.&lt;scope&gt;.&lt;tracking|picking&gt;[.&lt;depth&gt;]</code> - <code>render.&lt;variation&gt;</code></p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getFramebufferVersions();
</code></pre>
</div>

<a id="method-getframebufferversionsbyref" class="helios-api-member-anchor"></a>

### `getFramebufferVersionsByRef()` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14626</code></p>
<p>Return framebuffer resource versions keyed by reference for renderer diagnostics.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Plain object mapping framebuffer references to version numbers.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getFramebufferVersionsByRef();
</code></pre>
</div>

<a id="method-enablenodepicking" class="helios-api-member-anchor"></a>

### `enableNodePicking(options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14638</code></p>
<p>Enable pointer picking for nodes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Picking behavior options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.enableNodePicking({
  enabled: true,
});
</code></pre>
</div>

<a id="method-enableedgepicking" class="helios-api-member-anchor"></a>

### `enableEdgePicking(options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14654</code></p>
<p>Enable pointer picking for edges.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Picking behavior options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.enableEdgePicking({
  enabled: true,
});
</code></pre>
</div>

<a id="method-disablenodepicking" class="helios-api-member-anchor"></a>

### `disableNodePicking()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14669</code></p>
<p>Disable node pointer picking.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-disableedgepicking" class="helios-api-member-anchor"></a>

### `disableEdgePicking()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14682</code></p>
<p>Disable edge pointer picking.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-uibindinginfo" class="helios-api-member-anchor"></a>

### `uiBindingInfo(name)` &rarr; &#123;Object|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:2733</code></p>
<p>Return the UI control metadata registered for one Helios setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">UI binding name such as <code>nodeSizeScale</code> or <code>labelsEnabled</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Binding descriptor, or <code>null</code> when the name is unknown.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code></span></div>
</div>

## Density And Labels { #api-density-and-labels .helios-api-section-title }

<a id="method-density" class="helios-api-member-anchor"></a>

### `density(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11429</code></p>
<p>Read or update the screen-space density overlay configuration.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>false</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Density configuration, or <code>false</code>/<code>null</code> to disable the overlay.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.enabled"><span aria-hidden="true">|</span><code>enabled</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable density rendering.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.qualityScale"><span aria-hidden="true">|</span><code>qualityScale</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Density texture scale relative to the viewport.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.property"><span aria-hidden="true">|</span><code>property</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node attribute used as the primary density weight.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.compareProperty"><span aria-hidden="true">|</span><code>compareProperty</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional comparison attribute for diverging/log-ratio density.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.colormap"><span aria-hidden="true">|</span><code>colormap</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Sequential colormap name.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.divergingColormap"><span aria-hidden="true">|</span><code>divergingColormap</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Diverging colormap name.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current density snapshot when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.density({
  enabled: true,
});
</code></pre>
</div>

<a id="method-densityenabled" class="helios-api-member-anchor"></a>

### `densityEnabled(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11590</code></p>
<p>Read or set whether the density overlay is enabled.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable density rendering.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityEnabled(true);
</code></pre>
</div>

<a id="method-densityscale" class="helios-api-member-anchor"></a>

### `densityScale(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11603</code></p>
<p>Read or set the density overlay quality scale.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Texture scale relative to the viewport.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityScale(1);
</code></pre>
</div>

<a id="method-densitytopographic" class="helios-api-member-anchor"></a>

### `densityTopographic(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11616</code></p>
<p>Read or set whether density is rendered with topographic contours.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable contour-style rendering.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityTopographic(true);
</code></pre>
</div>

<a id="method-densityscalewithzoom" class="helios-api-member-anchor"></a>

### `densityScaleWithZoom(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11629</code></p>
<p>Read or set whether density bandwidth scales with camera zoom.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Scale density evaluation with zoom.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityScaleWithZoom(1);
</code></pre>
</div>

<a id="method-densitybandwidth" class="helios-api-member-anchor"></a>

### `densityBandwidth(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11642</code></p>
<p>Read or set the density kernel bandwidth.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Positive kernel bandwidth.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityBandwidth(1);
</code></pre>
</div>

<a id="method-densityweight" class="helios-api-member-anchor"></a>

### `densityWeight(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11655</code></p>
<p>Read or set the scalar multiplier applied to density weights.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Density weight multiplier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityWeight(1);
</code></pre>
</div>

<a id="method-densityproperty" class="helios-api-member-anchor"></a>

### `densityProperty(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11668</code></p>
<p>Read or set the node attribute used as the primary density property.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node attribute name.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current attribute name when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityProperty(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-densityvsproperty" class="helios-api-member-anchor"></a>

### `densityVsProperty(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11681</code></p>
<p>Read or set the comparison property used for diverging density views.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node attribute name to compare against the primary property.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current comparison attribute when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityVsProperty(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-densitynormalizevs" class="helios-api-member-anchor"></a>

### `densityNormalizeVs(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11694</code></p>
<p>Read or set whether comparison density values are normalized before differencing.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Normalize comparison density.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityNormalizeVs(true);
</code></pre>
</div>

<a id="method-densitycolormap" class="helios-api-member-anchor"></a>

### `densityColormap(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11707</code></p>
<p>Read or set the sequential colormap used by the density overlay.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Colormap name.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current colormap when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityColormap(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-densitydivergingcolormap" class="helios-api-member-anchor"></a>

### `densityDivergingColormap(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11720</code></p>
<p>Read or set the diverging colormap used by comparison density overlays.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Diverging colormap name.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current colormap when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.densityDivergingColormap(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-updatedensitymap" class="helios-api-member-anchor"></a>

### `updateDensityMap()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11732</code></p>
<p>Request a density overlay update on the next render frame.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-redrawdensitymap" class="helios-api-member-anchor"></a>

### `redrawDensityMap()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11744</code></p>
<p>Alias for <code>updateDensityMap()</code>.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-labels" class="helios-api-member-anchor"></a>

### `labels(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11779</code></p>
<p>Read or update label rendering options.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Label options, or <code>null</code> to disable labels.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.enabled"><span aria-hidden="true">|</span><code>enabled</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable ranked or selected labels.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.selectionMode"><span aria-hidden="true">|</span><code>selectionMode</code></span></td><td class="helios-api-param-type">&#x27;<code>ranked</code>&#x27;|&#x27;<code>selected</code>-<code>only</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Label selection policy.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.maxVisible"><span aria-hidden="true">|</span><code>maxVisible</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Maximum number of labels to render.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.source"><span aria-hidden="true">|</span><code>source</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>Function</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute name or callback used for label text.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current label configuration when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labels({
  enabled: true,
});
</code></pre>
</div>

<a id="method-legends" class="helios-api-member-anchor"></a>

### `legends(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11839</code></p>
<p>Read or update legend rendering options.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>false</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Legend configuration, or <code>false</code>/<code>null</code> to disable legends.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.enabled"><span aria-hidden="true">|</span><code>enabled</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable legend rendering.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current legend configuration when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.legends({
  enabled: true,
});
</code></pre>
</div>

<a id="method-legendsenabled" class="helios-api-member-anchor"></a>

### `legendsEnabled(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:11859</code></p>
<p>Read or set whether legends are enabled.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable legends.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.legendsEnabled(true);
</code></pre>
</div>

<a id="method-overlayinsets" class="helios-api-member-anchor"></a>

### `overlayInsets(insets)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12344</code></p>
<p>Read or set reserved viewport insets for overlays such as labels and legends.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>insets</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Insets in CSS pixels.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="insets.top"><span aria-hidden="true">|</span><code>top</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Top inset.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="insets.right"><span aria-hidden="true">|</span><code>right</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Right inset.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="insets.bottom"><span aria-hidden="true">|</span><code>bottom</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Bottom inset.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="insets.left"><span aria-hidden="true">|</span><code>left</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Left inset.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current inset object when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-labelsenabled" class="helios-api-member-anchor"></a>

### `labelsEnabled(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12368</code></p>
<p>Read or set whether labels are enabled.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable labels.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsEnabled(true);
</code></pre>
</div>

<a id="method-labelsmode" class="helios-api-member-anchor"></a>

### `labelsMode(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12384</code></p>
<p>Read or set the label selection mode.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type">&#x27;<code>auto</code>&#x27;|&#x27;<code>selected</code>-<code>only</code>&#x27;|&#x27;<code>off</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Label mode.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current mode when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsMode(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-labelsmaxvisible" class="helios-api-member-anchor"></a>

### `labelsMaxVisible(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12414</code></p>
<p>Read or set the maximum number of visible labels.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Maximum label count.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsMaxVisible(1);
</code></pre>
</div>

<a id="method-labelsselectedonlyspaceaware" class="helios-api-member-anchor"></a>

### `labelsSelectedOnlySpaceAware(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12429</code></p>
<p>Read or set whether selected-only labels still avoid spatial collisions.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable collision-aware selected labels.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsSelectedOnlySpaceAware(1);
</code></pre>
</div>

<a id="method-labelsfontsizescale" class="helios-api-member-anchor"></a>

### `labelsFontSizeScale(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12442</code></p>
<p>Read or set the label font-size multiplier.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Font-size scale.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsFontSizeScale(1);
</code></pre>
</div>

<a id="method-labelsminscreenradius" class="helios-api-member-anchor"></a>

### `labelsMinScreenRadius(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12457</code></p>
<p>Read or set the minimum on-screen node radius required for label candidates.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Minimum radius in CSS pixels.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsMinScreenRadius(1);
</code></pre>
</div>

<a id="method-labelsoutlinewidth" class="helios-api-member-anchor"></a>

### `labelsOutlineWidth(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12472</code></p>
<p>Read or set label outline width.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Outline width in CSS pixels.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsOutlineWidth(1);
</code></pre>
</div>

<a id="method-labelsoffsetradiusfactor" class="helios-api-member-anchor"></a>

### `labelsOffsetRadiusFactor(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12487</code></p>
<p>Read or set the radial node-size multiplier used to offset labels.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Offset radius multiplier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsOffsetRadiusFactor(1);
</code></pre>
</div>

<a id="method-labelsoffsetpx" class="helios-api-member-anchor"></a>

### `labelsOffsetPx(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12502</code></p>
<p>Read or set the fixed pixel offset added to label placement.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Offset in CSS pixels.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsOffsetPx(1);
</code></pre>
</div>

<a id="method-labelsmaxchars" class="helios-api-member-anchor"></a>

### `labelsMaxChars(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12517</code></p>
<p>Read or set the maximum number of characters per label row.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Maximum characters, or zero for no truncation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsMaxChars(1);
</code></pre>
</div>

<a id="method-labelsmaxrows" class="helios-api-member-anchor"></a>

### `labelsMaxRows(value)` &rarr; &#123;number|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12532</code></p>
<p>Read or set the maximum number of rows per wrapped label.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Maximum rows.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelsMaxRows(1);
</code></pre>
</div>

<a id="method-labelfill" class="helios-api-member-anchor"></a>

### `labelFill(color)` &rarr; &#123;string|Array&lt;number&gt;|Helios|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12547</code></p>
<p>Read or set label fill color.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS color string or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a>|<code>null</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelFill(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-labeloutlinecolor" class="helios-api-member-anchor"></a>

### `labelOutlineColor(color)` &rarr; &#123;string|Array&lt;number&gt;|Helios|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12563</code></p>
<p>Read or set label outline color.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>color</code></td><td class="helios-api-param-type"><code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">CSS color string or normalized RGBA tuple.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current color when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<code>Array</code>&lt;<code>number</code>&gt;|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a>|<code>null</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelOutlineColor(&#x27;#4aa3ff&#x27;);
</code></pre>
</div>

<a id="method-labelfontfamily" class="helios-api-member-anchor"></a>

### `labelFontFamily(value)` &rarr; &#123;string|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12579</code></p>
<p>Read or set the CSS font-family used by labels.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Font family string.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current font family when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelFontFamily(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-labelsource" class="helios-api-member-anchor"></a>

### `labelSource(value)` &rarr; &#123;string|Function|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12593</code></p>
<p>Read or set the label text source.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>string</code>|<code>Function</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute name, callback, or <code>null</code> for default labels.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current source when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>string</code>|<code>Function</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.labelSource(&#x27;auto&#x27;);
</code></pre>
</div>

<a id="method-setdensity" class="helios-api-member-anchor"></a>

### `setDensity(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14092</code></p>
<p>Alias for <code>density(options)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>false</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Density options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>density(options)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setDensity({
  enabled: true,
});
</code></pre>
</div>

<a id="method-setlabels" class="helios-api-member-anchor"></a>

### `setLabels(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14101</code></p>
<p>Alias for <code>labels(options)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Label options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>labels(options)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setLabels({
  enabled: true,
});
</code></pre>
</div>

<a id="method-setlegends" class="helios-api-member-anchor"></a>

### `setLegends(options)` &rarr; &#123;Object|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14110</code></p>
<p>Alias for <code>legends(options)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code>|<code>false</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Legend options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>legends(options)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setLegends({
  enabled: true,
});
</code></pre>
</div>

## Interaction { #api-interaction .helios-api-section-title }

<a id="method-interactionrenderorder" class="helios-api-member-anchor"></a>

### `interactionRenderOrder(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12796</code></p>
<p>Read or set whether selected and highlighted items are promoted later in render order.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable interaction-aware render-order promotion.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.interactionRenderOrder(1);
</code></pre>
</div>

<a id="method-nodestate" class="helios-api-member-anchor"></a>

### `nodeState(indices, mask, options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12867</code></p>
<p>Apply a state bitmask to node indices.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node indices to update.</td></tr>
<tr><td class="helios-api-param-name"><code>mask</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code>|<code>Array</code>&lt;<code>string</code>&gt;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State bitmask or named state such as <code>SELECTED</code> or <code>HIGHLIGHTED</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State update options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.mode"><span aria-hidden="true">|</span><code>mode</code></span></td><td class="helios-api-param-type">&#x27;<code>replace</code>&#x27;|&#x27;<code>add</code>&#x27;|&#x27;<code>remove</code>&#x27;|&#x27;<code>toggle</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;replace&#x27;</code></td><td class="helios-api-param-description">How to combine the mask with the existing state.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.nodeState([0, 1, 2]);
</code></pre>
</div>

<a id="method-edgestate" class="helios-api-member-anchor"></a>

### `edgeState(indices, mask, options = {})` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12924</code></p>
<p>Apply a state bitmask to edge indices.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge indices to update.</td></tr>
<tr><td class="helios-api-param-name"><code>mask</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code>|<code>Array</code>&lt;<code>string</code>&gt;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State bitmask or named state such as <code>SELECTED</code> or <code>HIGHLIGHTED</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State update options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.mode"><span aria-hidden="true">|</span><code>mode</code></span></td><td class="helios-api-param-type">&#x27;<code>replace</code>&#x27;|&#x27;<code>add</code>&#x27;|&#x27;<code>remove</code>&#x27;|&#x27;<code>toggle</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;replace&#x27;</code></td><td class="helios-api-param-description">How to combine the mask with the existing state.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.edgeState([0, 1, 2]);
</code></pre>
</div>

<a id="method-hovernodestate" class="helios-api-member-anchor"></a>

### `hoverNodeState(index, mask)` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:12970</code></p>
<p>Set transient hover state for a node.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Hovered node index, or <code>null</code> to clear.</td></tr>
<tr><td class="helios-api-param-name"><code>mask</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code>|<code>Array</code>&lt;<code>string</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;HOVERED&#x27;</code></td><td class="helios-api-param-description">State mask applied while hovered.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-hoveredgestate" class="helios-api-member-anchor"></a>

### `hoverEdgeState(index, mask)` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13008</code></p>
<p>Set transient hover state for an edge.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Hovered edge index, or <code>null</code> to clear.</td></tr>
<tr><td class="helios-api-param-name"><code>mask</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code>|<code>Array</code>&lt;<code>string</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;HOVERED&#x27;</code></td><td class="helios-api-param-description">State mask applied while hovered.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-highlightconnectededges" class="helios-api-member-anchor"></a>

### `highlightConnectedEdges(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13110</code></p>
<p>Read or set whether highlighted nodes also highlight their connected edges.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable connected-edge highlighting.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.highlightConnectedEdges(true);
</code></pre>
</div>

<a id="method-nodestatestyle" class="helios-api-member-anchor"></a>

### `nodeStateStyle(slot, style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13130</code></p>
<p>Read or set styling for nodes carrying a state bit.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>slot</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State slot index or name.</td></tr>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node state style with scale, opacity, outline, discard, and color fields.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current style when <code>style</code> is omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-nodenostatestyle" class="helios-api-member-anchor"></a>

### `nodeNoStateStyle(style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13174</code></p>
<p>Read or set styling for nodes with no active state bits.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node style applied to unselected/unhighlighted nodes.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current style when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-edgestatestyle" class="helios-api-member-anchor"></a>

### `edgeStateStyle(slot, style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13206</code></p>
<p>Read or set styling for edges carrying a state bit.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>slot</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State slot index or name.</td></tr>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge state style with width, opacity, discard, and color fields.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current style when <code>style</code> is omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-edgenostatestyle" class="helios-api-member-anchor"></a>

### `edgeNoStateStyle(style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13249</code></p>
<p>Read or set styling for edges with no active state bits.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge style applied to unselected/unhighlighted edges.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current style when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-nodehoverstyle" class="helios-api-member-anchor"></a>

### `nodeHoverStyle(style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13279</code></p>
<p>Read or set the transient hover style for nodes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node hover style.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current style when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-edgehoverstyle" class="helios-api-member-anchor"></a>

### `edgeHoverStyle(style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13308</code></p>
<p>Read or set the transient hover style for edges.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge hover style.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current style when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-hoverstylefromhighlight" class="helios-api-member-anchor"></a>

### `hoverStyleFromHighlight(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13344</code></p>
<p>Read or set whether hover style follows the highlighted-state style.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Copy highlighted styles into hover styles.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current value when omitted; otherwise this Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.hoverStyleFromHighlight(1);
</code></pre>
</div>

<a id="method-resetstatestyles" class="helios-api-member-anchor"></a>

### `resetStateStyles()` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:13362</code></p>
<p>Reset all node and edge state styles to renderer defaults.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-setnodestate" class="helios-api-member-anchor"></a>

### `setNodeState(indices, mask, options)` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14130</code></p>
<p>Alias for <code>nodeState(indices, mask, options)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node indices.</td></tr>
<tr><td class="helios-api-param-name"><code>mask</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code>|<code>Array</code>&lt;<code>string</code>&gt;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State mask.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setNodeState([0, 1, 2]);
</code></pre>
</div>

<a id="method-setedgestate" class="helios-api-member-anchor"></a>

### `setEdgeState(indices, mask, options)` &rarr; &#123;Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14141</code></p>
<p>Alias for <code>edgeState(indices, mask, options)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge indices.</td></tr>
<tr><td class="helios-api-param-name"><code>mask</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code>|<code>Array</code>&lt;<code>string</code>&gt;</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State mask.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This Helios instance.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setEdgeState([0, 1, 2]);
</code></pre>
</div>

<a id="method-setnodestatestyle" class="helios-api-member-anchor"></a>

### `setNodeStateStyle(slot, style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14151</code></p>
<p>Alias for <code>nodeStateStyle(slot, style)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>slot</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State slot.</td></tr>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node style.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>nodeStateStyle(slot, style)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-setedgestatestyle" class="helios-api-member-anchor"></a>

### `setEdgeStateStyle(slot, style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14161</code></p>
<p>Alias for <code>edgeStateStyle(slot, style)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>slot</code></td><td class="helios-api-param-type"><code>number</code>|<code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State slot.</td></tr>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge style.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>edgeStateStyle(slot, style)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-setnodenostatestyle" class="helios-api-member-anchor"></a>

### `setNodeNoStateStyle(style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14170</code></p>
<p>Alias for <code>nodeNoStateStyle(style)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node style.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>nodeNoStateStyle(style)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-setedgenostatestyle" class="helios-api-member-anchor"></a>

### `setEdgeNoStateStyle(style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14179</code></p>
<p>Alias for <code>edgeNoStateStyle(style)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge style.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>edgeNoStateStyle(style)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-setnodehoverstyle" class="helios-api-member-anchor"></a>

### `setNodeHoverStyle(style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14188</code></p>
<p>Alias for <code>nodeHoverStyle(style)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node hover style.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>nodeHoverStyle(style)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-setedgehoverstyle" class="helios-api-member-anchor"></a>

### `setEdgeHoverStyle(style)` &rarr; &#123;Object|null|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14197</code></p>
<p>Alias for <code>edgeHoverStyle(style)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>style</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Edge hover style.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>edgeHoverStyle(style)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
</div>

<a id="method-sethoverstylefromhighlight" class="helios-api-member-anchor"></a>

### `setHoverStyleFromHighlight(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14206</code></p>
<p>Alias for <code>hoverStyleFromHighlight(value)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable hover style from highlight.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>hoverStyleFromHighlight(value)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setHoverStyleFromHighlight(1);
</code></pre>
</div>

<a id="method-sethighlightconnectededges" class="helios-api-member-anchor"></a>

### `setHighlightConnectedEdges(value)` &rarr; &#123;boolean|Helios&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:14215</code></p>
<p>Alias for <code>highlightConnectedEdges(value)</code>.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Enable connected-edge highlighting.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Result of <code>highlightConnectedEdges(value)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code>|<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setHighlightConnectedEdges(true);
</code></pre>
</div>

## State And Persistence { #api-state-and-persistence .helios-api-section-title }

<a id="method-snapshotlayoutruntimestate" class="helios-api-member-anchor"></a>

### `snapshotLayoutRuntimeState(options = {})` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8635</code></p>
<p>Capture scheduler, layout, and optional node-position runtime state for persistence.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Snapshot controls.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.includePositions"><span aria-hidden="true">|</span><code>includePositions</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Include packed node positions when they fit within <code>maxPositionBytes</code>.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.maxPositionBytes"><span aria-hidden="true">|</span><code>maxPositionBytes</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Maximum encoded position payload size.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Serializable layout runtime snapshot.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.snapshotLayoutRuntimeState({
  enabled: true,
});
</code></pre>
</div>

<a id="method-snapshotlayoutruntimestateasync" class="helios-api-member-anchor"></a>

### `snapshotLayoutRuntimeStateAsync(options = {})` &rarr; &#123;Promise&lt;Object&gt;&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8650</code></p>
<p>Capture layout runtime state, preferring async delegate readback when active.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Snapshot controls and optional delegate override.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.preferDelegate"><span aria-hidden="true">|</span><code>preferDelegate</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Read positions from the active delegate even when network positions are available.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.positions"><span aria-hidden="true">|</span><code>positions</code></span></td><td class="helios-api-param-type"><code>Float32Array</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Pre-captured packed <code>x,y,z</code> positions to encode.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Serializable layout runtime snapshot.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Promise</code>&lt;<code>Object</code>&gt;</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.snapshotLayoutRuntimeStateAsync({
  enabled: true,
});
</code></pre>
</div>

<a id="method-restorelayoutruntimestate" class="helios-api-member-anchor"></a>

### `restoreLayoutRuntimeState(state = {}, options = {})` &rarr; &#123;boolean&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/Helios.js:8712</code></p>
<p>Restore scheduler, layout, and encoded position state from a previous snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>state</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Snapshot returned by <code>snapshotLayoutRuntimeState*</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Restore controls.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.reason"><span aria-hidden="true">|</span><code>reason</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Diagnostic reason passed to position delegates.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p><code>true</code> when any runtime state or positions were restored.</p><span class="helios-api-return-type"><strong>Type</strong> <code>boolean</code></span></div>
</div>


## Example

<div markdown="1" class="helios-api-template-section">

```js
const helios = new Helios(network, {
  container: document.querySelector('#app'),
  layout: { type: 'gpu-force', options: { mode: '2d' } },
  behaviors: { labels: { enabled: true, source: 'label' } },
});
await helios.ready;
```

</div>
