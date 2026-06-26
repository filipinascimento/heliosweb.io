# HeliosUI

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/ui/HeliosUI.js:341</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Optional built-in control surface for a Helios visualization.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class HeliosUI {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">UI construction options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.helios"><span aria-hidden="true">|</span><code>helios</code></span></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Helios instance to inspect and control.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.container"><span aria-hidden="true">|</span><code>container</code></span></td><td class="helios-api-param-type"><code>HTMLElement</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Existing UI container. When omitted the UI creates or reuses a layer on the Helios root.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.layerName"><span aria-hidden="true">|</span><code>layerName</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;ui&#x27;</code></td><td class="helios-api-param-description">Layer name used when the UI attaches to the Helios layer manager.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.theme"><span aria-hidden="true">|</span><code>theme</code></span></td><td class="helios-api-param-type">&#x27;<code>dark</code>&#x27;|&#x27;<code>light</code>&#x27;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Initial UI theme.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.styles"><span aria-hidden="true">|</span><code>styles</code></span></td><td class="helios-api-param-type">&#x27;<code>default</code>&#x27;|<code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;default&#x27;</code></td><td class="helios-api-param-description">Built-in style preset or external style mode.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.document"><span aria-hidden="true">|</span><code>document</code></span></td><td class="helios-api-param-type"><code>Document</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Document used for custom elements and style installation.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.allowDrag"><span aria-hidden="true">|</span><code>allowDrag</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Enable dragging floating panels.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.labelColumn"><span aria-hidden="true">|</span><code>labelColumn</code></span></td><td class="helios-api-param-type"><code>number</code>|<code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional fixed label-column sizing for generated controls.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.persistenceIndicators"><span aria-hidden="true">|</span><code>persistenceIndicators</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Show dirty/default markers when persistent storage supports them.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.interface"><span aria-hidden="true">|</span><code>interface</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Interface behavior options passed to <code>helios.useBehavior(&#x27;interface&#x27;, ...)</code>.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.behaviors"><span aria-hidden="true">|</span><code>behaviors</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Behavior option bag used by built-in UI behaviors.</td></tr>
</tbody>
</table>
</div>

## User Interface { #api-user-interface .helios-api-section-title }

<a id="method-registerstatecontrol" class="helios-api-member-anchor"></a>

### `registerStateControl(path, options = {})` &rarr; &#123;Function|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:482</code></p>
<p>Register a UI-owned value with the Helios state manager.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>path</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Persistent state path.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">State metadata and UI-control hints.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Cleanup function returned by the state manager, or <code>null</code> when state tracking is unavailable.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Function</code>|<code>null</code></span></div>
</div>

<a id="method-writestatecontrol" class="helios-api-member-anchor"></a>

### `writeStateControl(path, value, options = {})` &rarr; &#123;*|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:525</code></p>
<p>Write a UI control value through the Helios state manager.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>path</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Persistent state path.</td></tr>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type">*</td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value to store.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Persistence, debounce, source, and override-tracking options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>State-manager write result, or <code>null</code> when state tracking is unavailable.</p><span class="helios-api-return-type"><strong>Type</strong> *|<code>null</code></span></div>
</div>

<a id="method-createstateindicator" class="helios-api-member-anchor"></a>

### `createStateIndicator(path = '', scope = null, options = {})` &rarr; &#123;HTMLElement|null&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:563</code></p>
<p>Create a dirty/default indicator for a state path or state scope.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>path</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;&#x27;</code></td><td class="helios-api-param-description">State path to observe.</td></tr>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type"><code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Indicator scope override.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Registration and tooltip options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Indicator element, or <code>null</code> when indicators are disabled.</p><span class="helios-api-return-type"><strong>Type</strong> <code>HTMLElement</code>|<code>null</code></span></div>
</div>

<a id="method-settheme" class="helios-api-member-anchor"></a>

### `setTheme(theme, options = {})` &rarr; &#123;void&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:621</code></p>
<p>Apply a UI theme.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>theme</code></td><td class="helios-api-param-type">&#x27;<code>dark</code>&#x27;|&#x27;<code>light</code>&#x27;|<code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Theme name stored on the UI container.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> <code>void</code></span></div>
</div>

<a id="method-toggletheme" class="helios-api-member-anchor"></a>

### `toggleTheme(options = {})` &rarr; &#123;void&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:635</code></p>
<p>Toggle between the built-in dark and light themes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> <code>void</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.toggleTheme({
  enabled: true,
});
</code></pre>
</div>

<a id="method-serializestate" class="helios-api-member-anchor"></a>

### `serializeState()` &rarr; &#123;Object&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:650</code></p>
<p>Serialize UI panel, dock, theme, and responsive-interface state.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Serializable UI state snapshot.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

<a id="method-restorestate" class="helios-api-member-anchor"></a>

### `restoreState(state = {})` &rarr; &#123;HeliosUI&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:669</code></p>
<p>Restore a UI state snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>state</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Snapshot returned by <code>serializeState()</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This UI instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>HeliosUI</code></span></div>
</div>

<a id="method-getviewportwidth" class="helios-api-member-anchor"></a>

### `getViewportWidth()` &rarr; &#123;number&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:687</code></p>
<p>Resolve the best available viewport width for responsive UI behavior.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>Width in CSS pixels, or zero when unavailable.</p><span class="helios-api-return-type"><strong>Type</strong> <code>number</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getViewportWidth();
</code></pre>
</div>

<a id="method-applyinterfacebehaviorstate" class="helios-api-member-anchor"></a>

### `applyInterfaceBehaviorState(state = {})` &rarr; &#123;HeliosUI&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:711</code></p>
<p>Apply responsive interface state to the UI container and panel manager.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>state</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Interface behavior snapshot.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This UI instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>HeliosUI</code></span></div>
</div>

<a id="method-bindheliosaccessor" class="helios-api-member-anchor"></a>

### `bindHeliosAccessor(accessorName, options = {})` &rarr; &#123;UIAttribute&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:1350</code></p>
<p>Bind a Helios accessor method to a UIAttribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>accessorName</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Name of the Helios getter/setter method.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute metadata, range, persistence, and labeling options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Attribute wrapper suitable for controls and panels.</p><span class="helios-api-return-type"><strong>Type</strong> <code>UIAttribute</code></span></div>
</div>

<a id="method-bindbehavioraccessor" class="helios-api-member-anchor"></a>

### `bindBehaviorAccessor(behavior, accessorName, options = {})` &rarr; &#123;UIAttribute&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:1419</code></p>
<p>Bind a behavior accessor method to a UIAttribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>behavior</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/Behavior/"><code>Behavior</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Behavior instance that owns the accessor.</td></tr>
<tr><td class="helios-api-param-name"><code>accessorName</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Name of the behavior getter/setter method.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute metadata, range, persistence, and labeling options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Attribute wrapper suitable for controls and panels.</p><span class="helios-api-return-type"><strong>Type</strong> <code>UIAttribute</code></span></div>
</div>

<a id="method-createpanel" class="helios-api-member-anchor"></a>

### `createPanel(options)` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:1542</code></p>
<p>Create a standard Helios UI panel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel id, title, placement, content, schema, and persistence options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Panel instance returned by the panel manager.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createtabbedpanel" class="helios-api-member-anchor"></a>

### `createTabbedPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:1579</code></p>
<p>Create a panel whose content is managed by a tabbed panel primitive.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel and tab options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createTabbedPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createdemopanel" class="helios-api-member-anchor"></a>

### `createDemoPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:1607</code></p>
<p>Create the default scene/demo controls panel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement and title options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createDemoPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createfilterpanel" class="helios-api-member-anchor"></a>

### `createFilterPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:4352</code></p>
<p>Create the graph filtering panel with node and edge rule editors.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement, throttling, width, and initial filter options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createFilterPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createmetricspanel" class="helios-api-member-anchor"></a>

### `createMetricsPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:4616</code></p>
<p>Create a metrics panel for basic graph and renderer counters.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement and collapsed-state options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createMetricsPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createdebugpanel" class="helios-api-member-anchor"></a>

### `createDebugPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:7104</code></p>
<p>Create a debug panel for persistence and state-manager counters.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement and refresh-window options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createDebugPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-destroy" class="helios-api-member-anchor"></a>

### `destroy()` &rarr; &#123;void&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:7181</code></p>
<p>Dispose all UI controls, panels, listeners, timers, and container resources.</p>
<h4>Returns</h4>
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> <code>void</code></span></div>
</div>

<a id="method-createmapperspanel" class="helios-api-member-anchor"></a>

### `createMappersPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:7206</code></p>
<p>Create the visual mapper configuration panel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement and mapper panel options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createMappersPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createlayoutpanel" class="helios-api-member-anchor"></a>

### `createLayoutPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:9223</code></p>
<p>Create the layout controls panel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement and layout panel options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createLayoutPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createlegendspanel" class="helios-api-member-anchor"></a>

### `createLegendsPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:9235</code></p>
<p>Create the legends controls panel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement and legend panel options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createLegendsPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createcamerapanel" class="helios-api-member-anchor"></a>

### `createCameraPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:9247</code></p>
<p>Create the camera controls panel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement and camera panel options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createCameraPanel({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createselectionpanel" class="helios-api-member-anchor"></a>

### `createSelectionPanel(options = {})` &rarr; &#123;Panel&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/HeliosUI.js:9259</code></p>
<p>Create the selection and hover controls panel.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Panel placement and selection panel options.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Created panel instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Panel</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createSelectionPanel({
  enabled: true,
});
</code></pre>
</div>


## Example

<div markdown="1" class="helios-api-template-section">

```js
const ui = new HeliosUI({ helios, theme: 'dark' });
```

</div>
