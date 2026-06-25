
# Methods

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

High-level chainable attribute helpers and low-level buffer access methods.

The JavaScript/WASM methods are split between ergonomic helpers and low-level
buffer access. Attribute helpers are the right default for application code.
Direct buffer methods are for performance-sensitive integrations that need to
operate on WASM-backed typed arrays.

When using direct buffers, allocate first and view second. Avoid holding a typed
array view across calls that can grow WASM memory; use `withBufferAccess(...)`
where available.

<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../defineEdgeAttribute/">
<span>method</span>
<strong>defineEdgeAttribute</strong>
<em>Defines an edge attribute backed by linear WASM memory.</em>
</a>
<a class="helios-api-directory-item" href="../defineNetworkAttribute/">
<span>method</span>
<strong>defineNetworkAttribute</strong>
<em>Defines a network-level attribute backed by linear WASM memory.</em>
</a>
<a class="helios-api-directory-item" href="../defineNodeAttribute/">
<span>method</span>
<strong>defineNodeAttribute</strong>
<em>Defines a node attribute backed by linear WASM memory.</em>
</a>
<a class="helios-api-directory-item" href="../edgeAttribute/">
<span>method</span>
<strong>edgeAttribute</strong>
<em>Defines or updates one edge attribute and returns the network for chaining.</em>
</a>
<a class="helios-api-directory-item" href="../edgeAttributes/">
<span>method</span>
<strong>edgeAttributes</strong>
<em>Defines or updates several edge attributes and returns the network for chaining.</em>
</a>
<a class="helios-api-directory-item" href="../getEdgeAttributeBuffer/">
<span>method</span>
<strong>getEdgeAttributeBuffer</strong>
<em>Retrieves a wrapper around the edge attribute buffer.</em>
</a>
<a class="helios-api-directory-item" href="../getNetworkAttributeBuffer/">
<span>method</span>
<strong>getNetworkAttributeBuffer</strong>
<em>Retrieves a wrapper around the network attribute buffer.</em>
</a>
<a class="helios-api-directory-item" href="../getNodeAttributeBuffer/">
<span>method</span>
<strong>getNodeAttributeBuffer</strong>
<em>Retrieves a wrapper around the node attribute buffer.</em>
</a>
<a class="helios-api-directory-item" href="../networkAttribute/">
<span>method</span>
<strong>networkAttribute</strong>
<em>Defines or updates one network-level attribute and returns the network for chaining. Network attributes store one graph-wide value at id/ordinal `0`. Missing attributes are defined from `options.type` / `options.dimension`, or inferred from the provided value or callback result.</em>
</a>
<a class="helios-api-directory-item" href="../networkAttributes/">
<span>method</span>
<strong>networkAttributes</strong>
<em>Defines or updates several network-level attributes and returns the network for chaining. `valuesOrFn` may be an object keyed by attribute name, an array aligned with `names`, or a callback returning either an array aligned with `names` or an object keyed by attribute name.</em>
</a>
<a class="helios-api-directory-item" href="../nodeAttribute/">
<span>method</span>
<strong>nodeAttribute</strong>
<em>Defines or updates one node attribute and returns the network for chaining. Missing attributes are defined from `options.type` / `options.dimension`, or inferred from the provided scalar, array-like value, or callback result. Array-like values are indexed by active ordinal by default; pass `{ indexBy: &#x27;id&#x27; }` to index them by node id instead.</em>
</a>
<a class="helios-api-directory-item" href="../nodeAttributes/">
<span>method</span>
<strong>nodeAttributes</strong>
<em>Defines or updates several node attributes and returns the network for chaining. `valuesOrFn` may be an object keyed by attribute name, an array of per-attribute scalar values, or a callback returning either an array aligned with `names` or an object keyed by attribute name.</em>
</a>
<a class="helios-api-directory-item" href="../withBufferAccess/">
<span>method</span>
<strong>withBufferAccess</strong>
<em>Runs a callback inside a buffer access session, ensuring cleanup even on throw.</em>
</a>
</div>
