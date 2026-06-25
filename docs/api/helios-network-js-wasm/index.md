
# Helios Network JS/WASM API

<p class="helios-api-version">Version 0.10.0</p>

The JavaScript/WASM package wraps the WebAssembly graph store with selectors, attribute APIs, serialization helpers, and direct typed-buffer access. Use the chainable attribute helpers for everyday code; the direct buffer methods remain documented as the low-level performance path when performance requires operating on WASM-backed views directly.

## Classes

<p class="helios-api-group-description">Network and selector classes exposed by the JavaScript/WASM package.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="EdgeSelector/">
<span>class</span>
<strong>EdgeSelector</strong>
<em>Selector specialized for edge indices.</em>
</a>
<a class="helios-api-directory-item" href="HeliosNetwork/">
<span>class</span>
<strong>HeliosNetwork</strong>
<em>High-level JavaScript wrapper around the Helios WASM network implementation. Manages lifetime, attribute registration, and buffer views.</em>
</a>
<a class="helios-api-directory-item" href="NodeSelector/">
<span>class</span>
<strong>NodeSelector</strong>
<em>Selector specialized for node indices.</em>
</a>
</div>


## Methods

<p class="helios-api-group-description">High-level chainable attribute helpers and low-level buffer access methods.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="defineEdgeAttribute/">
<span>method</span>
<strong>defineEdgeAttribute</strong>
<em>Defines an edge attribute backed by linear WASM memory.</em>
</a>
<a class="helios-api-directory-item" href="defineNetworkAttribute/">
<span>method</span>
<strong>defineNetworkAttribute</strong>
<em>Defines a network-level attribute backed by linear WASM memory.</em>
</a>
<a class="helios-api-directory-item" href="defineNodeAttribute/">
<span>method</span>
<strong>defineNodeAttribute</strong>
<em>Defines a node attribute backed by linear WASM memory.</em>
</a>
<a class="helios-api-directory-item" href="edgeAttribute/">
<span>method</span>
<strong>edgeAttribute</strong>
<em>Defines or updates one edge attribute and returns the network for chaining.</em>
</a>
<a class="helios-api-directory-item" href="edgeAttributes/">
<span>method</span>
<strong>edgeAttributes</strong>
<em>Defines or updates several edge attributes and returns the network for chaining.</em>
</a>
<a class="helios-api-directory-item" href="getEdgeAttributeBuffer/">
<span>method</span>
<strong>getEdgeAttributeBuffer</strong>
<em>Retrieves a wrapper around the edge attribute buffer.</em>
</a>
<a class="helios-api-directory-item" href="getNetworkAttributeBuffer/">
<span>method</span>
<strong>getNetworkAttributeBuffer</strong>
<em>Retrieves a wrapper around the network attribute buffer.</em>
</a>
<a class="helios-api-directory-item" href="getNodeAttributeBuffer/">
<span>method</span>
<strong>getNodeAttributeBuffer</strong>
<em>Retrieves a wrapper around the node attribute buffer.</em>
</a>
<a class="helios-api-directory-item" href="networkAttribute/">
<span>method</span>
<strong>networkAttribute</strong>
<em>Defines or updates one network-level attribute and returns the network for chaining. Network attributes store one graph-wide value at id/ordinal `0`. Missing attributes are defined from `options.type` / `options.dimension`, or inferred from the provided value or callback result.</em>
</a>
<a class="helios-api-directory-item" href="networkAttributes/">
<span>method</span>
<strong>networkAttributes</strong>
<em>Defines or updates several network-level attributes and returns the network for chaining. `valuesOrFn` may be an object keyed by attribute name, an array aligned with `names`, or a callback returning either an array aligned with `names` or an object keyed by attribute name.</em>
</a>
<a class="helios-api-directory-item" href="nodeAttribute/">
<span>method</span>
<strong>nodeAttribute</strong>
<em>Defines or updates one node attribute and returns the network for chaining. Missing attributes are defined from `options.type` / `options.dimension`, or inferred from the provided scalar, array-like value, or callback result. Array-like values are indexed by active ordinal by default; pass `{ indexBy: &#x27;id&#x27; }` to index them by node id instead.</em>
</a>
<a class="helios-api-directory-item" href="nodeAttributes/">
<span>method</span>
<strong>nodeAttributes</strong>
<em>Defines or updates several node attributes and returns the network for chaining. `valuesOrFn` may be an object keyed by attribute name, an array of per-attribute scalar values, or a callback returning either an array aligned with `names` or an object keyed by attribute name.</em>
</a>
<a class="helios-api-directory-item" href="withBufferAccess/">
<span>method</span>
<strong>withBufferAccess</strong>
<em>Runs a callback inside a buffer access session, ensuring cleanup even on throw.</em>
</a>
</div>


## Enums And Constants

<p class="helios-api-group-description">Constants mirrored from the WASM/native core for attributes, traversal, measurements, and execution modes.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="AttributeType/">
<span>symbol</span>
<strong>AttributeType</strong>
<em>Enumeration of attribute types supported by the WASM network core. Values align with the constants defined in the native implementation.</em>
</a>
<a class="helios-api-directory-item" href="CategorySortOrder/">
<span>symbol</span>
<strong>CategorySortOrder</strong>
<em>Ordering strategies used when converting string attributes to categories. Frequency ordering is useful for visualization legends; natural ordering keeps labels such as &quot;item2&quot; before &quot;item10&quot;.</em>
</a>
<a class="helios-api-directory-item" href="ClusteringCoefficientVariant/">
<span>symbol</span>
<strong>ClusteringCoefficientVariant</strong>
<em>Local clustering coefficient formula selector.</em>
</a>
<a class="helios-api-directory-item" href="ConnectedComponentsMode/">
<span>symbol</span>
<strong>ConnectedComponentsMode</strong>
<em>Connected-component mode selector for weak or strongly connected components.</em>
</a>
<a class="helios-api-directory-item" href="DimensionDifferenceMethod/">
<span>symbol</span>
<strong>DimensionDifferenceMethod</strong>
<em>Finite-difference estimators for local and global graph dimension measures.</em>
</a>
<a class="helios-api-directory-item" href="MeasurementExecutionMode/">
<span>symbol</span>
<strong>MeasurementExecutionMode</strong>
<em>Execution policy for native graph measurements that can run in serial or parallel.</em>
</a>
<a class="helios-api-directory-item" href="NeighborDirection/">
<span>symbol</span>
<strong>NeighborDirection</strong>
<em>Direction policy for neighbor traversal and degree-like measurements.</em>
</a>
<a class="helios-api-directory-item" href="StrengthMeasure/">
<span>symbol</span>
<strong>StrengthMeasure</strong>
<em>Aggregation policy for edge-weight based node strength.</em>
</a>
</div>



## Coverage Notes

The current JavaScript/WASM package does not publish TypeScript declarations. Until declarations are added, this extractor uses the public package entry plus implementation JSDoc and refuses to document deep modules. The structured reference is available at [`../reference.json`](../reference.json).
