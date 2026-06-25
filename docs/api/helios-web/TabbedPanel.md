# TabbedPanel

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/ui/panels/TabbedPanel.js:24</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Small tabbed panel primitive used by the optional Helios UI.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class TabbedPanel {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Tab panel options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.tabs"><span aria-hidden="true">|</span><code>tabs</code></span></td><td class="helios-api-param-type"><code>Array</code>.&lt;<code>Object</code>&gt;</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Initial tabs.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.activeId"><span aria-hidden="true">|</span><code>activeId</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Initially active tab id.</td></tr>
</tbody>
</table>
</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-destroy" class="helios-api-member-anchor"></a>

### `destroy()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/panels/TabbedPanel.js:100</code></p>
<p>Manages destroy for the current instance.</p>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setactive" class="helios-api-member-anchor"></a>

### `setActive(id)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/panels/TabbedPanel.js:79</code></p>
<p>Set the active setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setActive</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-addtab" class="helios-api-member-anchor"></a>

### `addTab(tab)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/panels/TabbedPanel.js:57</code></p>
<p>Manages tab for the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>tab</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>addTab</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-activeid" class="helios-api-member-anchor"></a>

### `activeId()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/panels/TabbedPanel.js:96</code></p>
<p>Configures or reads active id.</p>
</div>
