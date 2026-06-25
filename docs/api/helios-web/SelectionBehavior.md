# SelectionBehavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/SelectionBehavior.js:108</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in behavior for node and edge selection state.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class SelectionBehavior extends Behavior {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Selection options such as <code>nodeClick</code>, <code>edgeClick</code>, <code>selectedConnectedEdges</code>, saved-selection attribute names, and inactive-item styling.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Behavior that can be attached through <code>helios.useBehavior(&#x27;selection&#x27;, options)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <code>SelectionBehavior</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Selection state is serializable. The behavior also synchronizes
picking, labels, and optional connected-edge highlighting.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:109</code></p>
<p>Id exposed by the class.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-getpublicstate" class="helios-api-member-anchor"></a>

### `getPublicState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:375</code></p>
<p>Returns the current public state value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getPublicState();
</code></pre>
</div>

<a id="method-ensurestatestyledefaults" class="helios-api-member-anchor"></a>

### `ensureStateStyleDefaults()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:383</code></p>
<p>Configures or reads ensure state style defaults.</p>
</div>

<a id="method-applyotherelementsstate" class="helios-api-member-anchor"></a>

### `applyOtherElementsState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:387</code></p>
<p>Updates the other elements state state on the current instance.</p>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-attach" class="helios-api-member-anchor"></a>

### `attach(context)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:136</code></p>
<p>Configures or reads attach.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>attach</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-serialize" class="helios-api-member-anchor"></a>

### `serialize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:196</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:357</code></p>
<p>Updates the restore state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>restore</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-centerselectednodesornetwork" class="helios-api-member-anchor"></a>

### `centerSelectedNodesOrNetwork(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:623</code></p>
<p>Read or set the center selected nodes or network setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current center selected nodes or network value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.centerSelectedNodesOrNetwork({
  enabled: true,
});
</code></pre>
</div>

<a id="method-saveselectiontoattribute" class="helios-api-member-anchor"></a>

### `saveSelectionToAttribute(name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:682</code></p>
<p>Handles selection to attribute for the current graph or visualization state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-restoreselectionfromattribute" class="helios-api-member-anchor"></a>

### `restoreSelectionFromAttribute(name)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:732</code></p>
<p>Updates the selection from attribute state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-attachnetworkattributelisteners" class="helios-api-member-anchor"></a>

### `attachNetworkAttributeListeners()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:743</code></p>
<p>Configures or reads attach network attribute listeners.</p>
</div>

<a id="method-handlenetworkreplaced" class="helios-api-member-anchor"></a>

### `handleNetworkReplaced()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:795</code></p>
<p>Configures or reads handle network replaced.</p>
</div>

## Appearance { #api-appearance .helios-api-section-title }

<p class="helios-api-section-description">Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.</p>

<a id="method-applyselectionlabeldefaults" class="helios-api-member-anchor"></a>

### `applySelectionLabelDefaults()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:416</code></p>
<p>Updates the selection label defaults state on the current instance.</p>
</div>

## Rendering And Picking { #api-rendering-and-picking .helios-api-section-title }

<p class="helios-api-section-description">Render requests, picking, framebuffer inspection, and attribute tracking. <a href="HoverBehavior.md">HoverBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> use these lower-level hooks.</p>

<a id="method-syncpicking" class="helios-api-member-anchor"></a>

### `syncPicking()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:395</code></p>
<p>Configures or reads sync picking.</p>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setselectionbinding" class="helios-api-member-anchor"></a>

### `setSelectionBinding(value = CURRENT_SELECTION_VALUE)` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:399</code></p>
<p>Read or set the set selection binding setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>CURRENT_SELECTION_VALUE</code></td><td class="helios-api-param-description">New set selection binding value. Omit this argument to read the current value.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current set selection binding value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.setSelectionBinding(1);
</code></pre>
</div>

<a id="method-setselectorrules" class="helios-api-member-anchor"></a>

### `setSelectorRules(rules = [], options = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:407</code></p>
<p>Set the selector rules setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>rules</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>[]</code></td><td class="helios-api-param-description">Value passed to <code>setSelectorRules</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-setnodeselected" class="helios-api-member-anchor"></a>

### `setNodeSelected(index, selected, options = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:431</code></p>
<p>Set the node selected setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node, edge, or attribute index.</td></tr>
<tr><td class="helios-api-param-name"><code>selected</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setNodeSelected</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-setedgeselected" class="helios-api-member-anchor"></a>

### `setEdgeSelected(index, selected, options = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:453</code></p>
<p>Set the edge selected setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node, edge, or attribute index.</td></tr>
<tr><td class="helios-api-param-name"><code>selected</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setEdgeSelected</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-clearselection" class="helios-api-member-anchor"></a>

### `clearSelection(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:472</code></p>
<p>Read or set the clear selection setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current clear selection value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.clearSelection({
  enabled: true,
});
</code></pre>
</div>

<a id="method-toggleselection" class="helios-api-member-anchor"></a>

### `toggleSelection(kind, index, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:507</code></p>
<p>Updates the selection state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>kind</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>toggleSelection</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node, edge, or attribute index.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-detach" class="helios-api-member-anchor"></a>

### `detach()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:153</code></p>
<p>Manages detach for the current instance.</p>
</div>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:163</code></p>
<p>Read or set the update setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current update value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.update({
  enabled: true,
});
</code></pre>
</div>

<a id="method-stateentries" class="helios-api-member-anchor"></a>

### `stateEntries()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:215</code></p>
<p>Configures or reads state entries.</p>
</div>

<a id="method-emitchange" class="helios-api-member-anchor"></a>

### `emitChange(reason, detail = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:371</code></p>
<p>Configures or reads emit change.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>detail</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Event payload passed to listeners.</td></tr>
</tbody>
</table>
</div>

<a id="method-applyselectedconnectededges" class="helios-api-member-anchor"></a>

### `applySelectedConnectedEdges()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:391</code></p>
<p>Updates the selected connected edges state on the current instance.</p>
</div>

<a id="method-selectonly" class="helios-api-member-anchor"></a>

### `selectOnly(kind, index, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:494</code></p>
<p>Configures or reads select only.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>kind</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>selectOnly</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>index</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node, edge, or attribute index.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-applynodeselectionset" class="helios-api-member-anchor"></a>

### `applyNodeSelectionSet(indices, mode = 'add', options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:512</code></p>
<p>Updates the node selection set state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node or edge indices used by the operation.</td></tr>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;add&#x27;</code></td><td class="helios-api-param-description">Mode for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.applyNodeSelectionSet([0, 1, 2]);
</code></pre>
</div>

<a id="method-applyedgeselectionset" class="helios-api-member-anchor"></a>

### `applyEdgeSelectionSet(indices, mode = 'add', options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:550</code></p>
<p>Updates the edge selection set state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node or edge indices used by the operation.</td></tr>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;add&#x27;</code></td><td class="helios-api-param-description">Mode for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.applyEdgeSelectionSet([0, 1, 2]);
</code></pre>
</div>

<a id="method-selectnodes" class="helios-api-member-anchor"></a>

### `selectNodes(indices, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:588</code></p>
<p>Configures or reads select nodes.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node or edge indices used by the operation.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.selectNodes([0, 1, 2]);
</code></pre>
</div>

<a id="method-selectedges" class="helios-api-member-anchor"></a>

### `selectEdges(indices, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:592</code></p>
<p>Configures or reads select edges.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>indices</code></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Node or edge indices used by the operation.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.selectEdges([0, 1, 2]);
</code></pre>
</div>

<a id="method-buildnodeselectionquery" class="helios-api-member-anchor"></a>

### `buildNodeSelectionQuery(rules = [])`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:596</code></p>
<p>Configures or reads build node selection query.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>rules</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>[]</code></td><td class="helios-api-param-description">Value passed to <code>buildNodeSelectionQuery</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-applynodeselectionquery" class="helios-api-member-anchor"></a>

### `applyNodeSelectionQuery(rules, mode = 'add')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:605</code></p>
<p>Updates the node selection query state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>rules</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>applyNodeSelectionQuery</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>mode</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;add&#x27;</code></td><td class="helios-api-param-description">Mode for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-expandselectiontoneighbors" class="helios-api-member-anchor"></a>

### `expandSelectionToNeighbors()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:613</code></p>
<p>Configures or reads expand selection to neighbors.</p>
</div>

<a id="method-collectsavedselectionattributes" class="helios-api-member-anchor"></a>

### `collectSavedSelectionAttributes()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:646</code></p>
<p>Configures or reads collect saved selection attributes.</p>
</div>

<a id="method-ensurebooleanselectionattribute" class="helios-api-member-anchor"></a>

### `ensureBooleanSelectionAttribute(network, scope, name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:662</code></p>
<p>Configures or reads ensure boolean selection attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Network instance to read from or mutate.</td></tr>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute scope: node, edge, or network.</td></tr>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-collectselectionattributeindices" class="helios-api-member-anchor"></a>

### `collectSelectionAttributeIndices(scope, name)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:705</code></p>
<p>Configures or reads collect selection attribute indices.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>scope</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute scope: node, edge, or network.</td></tr>
<tr><td class="helios-api-param-name"><code>name</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute or API identifier.</td></tr>
</tbody>
</table>
</div>

<a id="method-handlegraphclick" class="helios-api-member-anchor"></a>

### `handleGraphClick(event)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:759</code></p>
<p>Configures or reads handle graph click.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>event</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>handleGraphClick</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-handlegraphdoubleclick" class="helios-api-member-anchor"></a>

### `handleGraphDoubleClick(event)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:780</code></p>
<p>Configures or reads handle graph double click.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>event</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>handleGraphDoubleClick</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-handleuibindingchange" class="helios-api-member-anchor"></a>

### `handleUiBindingChange(event)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/SelectionBehavior.js:808</code></p>
<p>Configures or reads handle ui binding change.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>event</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>handleUiBindingChange</code>.</td></tr>
</tbody>
</table>
</div>


## Example

<div markdown="1" class="helios-api-template-section">

```js
helios.behavior.selection.selectNodes([0, 2, 4], { mode: 'replace' });
```

</div>
