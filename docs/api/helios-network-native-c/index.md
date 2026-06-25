
# Helios Network Native C API

<p class="helios-api-version">Native core reference</p>

The C API is the native surface behind the WASM and Python bindings. Functions are grouped by lifecycle, topology, attributes, selectors, serialization, and measurements.

## Network Lifecycle

<p class="helios-api-group-description">Allocation, destruction, version, and graph-wide metadata helpers.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXFreeNetwork/">
<span>function</span>
<strong>CXFreeNetwork</strong>
<em>Releases all resources owned by a network.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkBuildFilteredSubgraph/">
<span>function</span>
<strong>CXNetworkBuildFilteredSubgraph</strong>
<em>Builds an induced filtered subgraph from optional node/edge filters. - `nodeFilter` / `edgeFilter` may be NULL to indicate &quot;all active&quot;. - Node output is always active-only. - Edge output is always active-only and induced by the resulting node set (edges with at least one endpoint outside `outNodeSelector` are removed). - Output order follows native active index order.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGenerateBarabasiAlbert/">
<span>function</span>
<strong>CXNetworkGenerateBarabasiAlbert</strong>
<em>Creates a Barabasi-Albert preferential-attachment graph.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGenerateConfigurationModel/">
<span>function</span>
<strong>CXNetworkGenerateConfigurationModel</strong>
<em>Creates a graph with the requested degree sequence using the configuration model.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGenerateLattice2D/">
<span>function</span>
<strong>CXNetworkGenerateLattice2D</strong>
<em>Creates a two-dimensional lattice graph.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGenerateRandomGeometric/">
<span>function</span>
<strong>CXNetworkGenerateRandomGeometric</strong>
<em>Creates a random geometric graph using random 2D positions and a radius cutoff.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGenerateStochasticBlockModel/">
<span>function</span>
<strong>CXNetworkGenerateStochasticBlockModel</strong>
<em>Creates a stochastic block model graph from block sizes and a flattened block-to-block probability matrix.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGenerateWattsStrogatz/">
<span>function</span>
<strong>CXNetworkGenerateWattsStrogatz</strong>
<em>Creates a Watts-Strogatz small-world graph.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGenerateWaxman/">
<span>function</span>
<strong>CXNetworkGenerateWaxman</strong>
<em>Creates a Waxman random graph using distance-weighted edge probabilities.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkIsDirected/">
<span>function</span>
<strong>CXNetworkIsDirected</strong>
<em>Returns CXTrue when the network treats edges as directed.</em>
</a>
<a class="helios-api-directory-item" href="CXNewNetwork/">
<span>function</span>
<strong>CXNewNetwork</strong>
<em>Allocates a new network with default capacities.</em>
</a>
<a class="helios-api-directory-item" href="CXNewNetworkWithCapacity/">
<span>function</span>
<strong>CXNewNetworkWithCapacity</strong>
<em>Allocates a new network with explicit node/edge capacities.</em>
</a>
</div>


## Topology

<p class="helios-api-group-description">Node, edge, neighbor, compaction, and topology mutation APIs.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXNetworkAddEdges/">
<span>function</span>
<strong>CXNetworkAddEdges</strong>
<em>Inserts the provided edges, writing the new indices to `outIndices` when supplied. Edges are expressed as contiguous (from,to) pairs.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkAddNodes/">
<span>function</span>
<strong>CXNetworkAddNodes</strong>
<em>Appends `count` new nodes to the network. When `outIndices` is non-null it receives the indices assigned to the created nodes.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkCollectNeighbors/">
<span>function</span>
<strong>CXNetworkCollectNeighbors</strong>
<em>Collects unique one-hop neighbors for one or more source nodes. - `sourceNodes` can contain any node ids; inactive/out-of-range entries are ignored. - `direction` controls traversal for directed graphs (`out`, `in`, `both`). - `includeSourceNodes` controls whether source nodes can appear in `outNodeSelector`. - `outEdgeSelector` is optional; pass NULL to skip edge collection.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkCollectNeighborsAtLevel/">
<span>function</span>
<strong>CXNetworkCollectNeighborsAtLevel</strong>
<em>Collects neighbors at exactly the given concentric level (shortest-path hop distance). - `level == 0` refers to the source set itself. - `includeSourceNodes` only affects whether level-0 source nodes are included. - `outEdgeSelector` is optional; pass NULL to skip edge collection.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkCollectNeighborsUpToLevel/">
<span>function</span>
<strong>CXNetworkCollectNeighborsUpToLevel</strong>
<em>Collects neighbors up to (and including) the given concentric level. - `maxLevel == 0` returns only the source set when `includeSourceNodes` is true. - `outEdgeSelector` is optional; pass NULL to skip edge collection.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkCompact/">
<span>function</span>
<strong>CXNetworkCompact</strong>
<em>Compacts the network so that node and edge indices become contiguous starting at zero and capacities shrink to match the number of active elements. When `nodeOriginalIndexAttr` or `edgeOriginalIndexAttr` are provided, the function records the previous indices in attributes of type `CXUnsignedIntegerAttributeType`. Returns CXFalse on allocation failure or when incompatible attributes are encountered.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgeCapacity/">
<span>function</span>
<strong>CXNetworkEdgeCapacity</strong>
<em>Returns the allocated edge capacity.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgeCount/">
<span>function</span>
<strong>CXNetworkEdgeCount</strong>
<em>Returns the number of active edges currently stored.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgeFreeListCapacity/">
<span>function</span>
<strong>CXNetworkEdgeFreeListCapacity</strong>
<em>Returns the allocated edge free-list capacity (reserved slots).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgeFreeListCount/">
<span>function</span>
<strong>CXNetworkEdgeFreeListCount</strong>
<em>Returns the current edge free-list size (recycled indices).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetEdgeValidRange/">
<span>function</span>
<strong>CXNetworkGetEdgeValidRange</strong>
<em>Returns the min/max active edge indices as [start,end).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetNodeValidRange/">
<span>function</span>
<strong>CXNetworkGetNodeValidRange</strong>
<em>Returns the min/max active node indices as [start,end).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkInNeighbors/">
<span>function</span>
<strong>CXNetworkInNeighbors</strong>
<em>Returns the inbound neighbor container for the given node.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNodeCapacity/">
<span>function</span>
<strong>CXNetworkNodeCapacity</strong>
<em>Returns the allocated node capacity (useful for buffer sizing).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNodeCount/">
<span>function</span>
<strong>CXNetworkNodeCount</strong>
<em>Returns the number of active nodes currently stored.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNodeFreeListCapacity/">
<span>function</span>
<strong>CXNetworkNodeFreeListCapacity</strong>
<em>Returns the allocated node free-list capacity (reserved slots).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNodeFreeListCount/">
<span>function</span>
<strong>CXNetworkNodeFreeListCount</strong>
<em>Returns the current node free-list size (recycled indices).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkOutNeighbors/">
<span>function</span>
<strong>CXNetworkOutNeighbors</strong>
<em>Returns the outbound neighbor container for the given node.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkRemoveEdges/">
<span>function</span>
<strong>CXNetworkRemoveEdges</strong>
<em>Removes the supplied edges from the network.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkRemoveNodes/">
<span>function</span>
<strong>CXNetworkRemoveNodes</strong>
<em>Removes the supplied nodes, reclaiming their indices for future use.</em>
</a>
</div>


## Attributes

<p class="helios-api-group-description">Attribute definition, lookup, categorization, and multi-category APIs.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXAttributeData/">
<span>function</span>
<strong>CXAttributeData</strong>
<em>Returns a pointer to the raw backing buffer for an attribute (or NULL when missing).</em>
</a>
<a class="helios-api-directory-item" href="CXAttributeInterpolateFloatBuffer/">
<span>function</span>
<strong>CXAttributeInterpolateFloatBuffer</strong>
<em>Interpolates a float attribute buffer toward target values and bumps the attribute version. Returns CXTrue when further interpolation steps are recommended based on minDisplacementRatio.</em>
</a>
<a class="helios-api-directory-item" href="CXAttributeStride/">
<span>function</span>
<strong>CXAttributeStride</strong>
<em>Returns the byte stride between consecutive entries of an attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXAttributeVersion/">
<span>function</span>
<strong>CXAttributeVersion</strong>
<em>Returns the version counter for an attribute descriptor.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkBumpEdgeAttributeVersion/">
<span>function</span>
<strong>CXNetworkBumpEdgeAttributeVersion</strong>
<em>Manually bumps an edge attribute version and returns the new value.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkBumpNetworkAttributeVersion/">
<span>function</span>
<strong>CXNetworkBumpNetworkAttributeVersion</strong>
<em>Manually bumps a network attribute version and returns the new value.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkBumpNodeAttributeVersion/">
<span>function</span>
<strong>CXNetworkBumpNodeAttributeVersion</strong>
<em>Manually bumps a node attribute version and returns the new value.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkCategorizeAttribute/">
<span>function</span>
<strong>CXNetworkCategorizeAttribute</strong>
<em>Converts a string attribute into category ids using the requested sort policy.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkClearMultiCategoryEntry/">
<span>function</span>
<strong>CXNetworkClearMultiCategoryEntry</strong>
<em>Clears all category ids and weights for one multi-category entry.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkCopyNodeAttributesToEdgeAttributes/">
<span>function</span>
<strong>CXNetworkCopyNodeAttributesToEdgeAttributes</strong>
<em>Copies node attributes into an edge attribute buffer using the network&#x27;s topology. `endpointMode` controls which endpoint is copied: -1 = both, 0 = source only, 1 = destination only. When copying a single endpoint and `duplicateSingleEndpoint` is true, the chosen endpoint is written twice sequentially (for double-width edge attributes).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkDecategorizeAttribute/">
<span>function</span>
<strong>CXNetworkDecategorizeAttribute</strong>
<em>Converts category ids back to string labels for the named attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkDefineEdgeAttribute/">
<span>function</span>
<strong>CXNetworkDefineEdgeAttribute</strong>
<em>Declares an edge attribute backing buffer.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkDefineMultiCategoryAttribute/">
<span>function</span>
<strong>CXNetworkDefineMultiCategoryAttribute</strong>
<em>Defines a multi-category attribute with optional per-entry weights.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkDefineNetworkAttribute/">
<span>function</span>
<strong>CXNetworkDefineNetworkAttribute</strong>
<em>Declares a network-level attribute backing buffer.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkDefineNodeAttribute/">
<span>function</span>
<strong>CXNetworkDefineNodeAttribute</strong>
<em>Declares a node attribute backing buffer. Dimension defaults to 1.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgeAttributeCount/">
<span>function</span>
<strong>CXNetworkEdgeAttributeCount</strong>
<em>Returns the number of edge attributes currently defined on the network.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgeAttributeNameAt/">
<span>function</span>
<strong>CXNetworkEdgeAttributeNameAt</strong>
<em>Returns the edge attribute name at `index`, or NULL when out of range.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetAttributeCategoryDictionary/">
<span>function</span>
<strong>CXNetworkGetAttributeCategoryDictionary</strong>
<em>Returns the category dictionary for a categorical attribute, or NULL when unavailable.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetAttributeCategoryDictionaryCount/">
<span>function</span>
<strong>CXNetworkGetAttributeCategoryDictionaryCount</strong>
<em>Returns how many category entries are defined for a categorical attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetAttributeCategoryDictionaryEntries/">
<span>function</span>
<strong>CXNetworkGetAttributeCategoryDictionaryEntries</strong>
<em>Copies category ids and labels into caller-provided arrays.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetEdgeAttribute/">
<span>function</span>
<strong>CXNetworkGetEdgeAttribute</strong>
<em>Fetches an edge attribute descriptor by name.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetEdgeAttributeBuffer/">
<span>function</span>
<strong>CXNetworkGetEdgeAttributeBuffer</strong>
<em>Returns a pointer to the raw edge attribute buffer for the named attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetMultiCategoryEntryCount/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryEntryCount</strong>
<em>Returns the number of category entries stored for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetMultiCategoryEntryRange/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryEntryRange</strong>
<em>Returns the [start,end) range for one entry inside the packed multi-category buffers.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetMultiCategoryIds/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryIds</strong>
<em>Returns the packed category id buffer for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetMultiCategoryOffsetCount/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryOffsetCount</strong>
<em>Returns the number of offsets stored for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetMultiCategoryOffsets/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryOffsets</strong>
<em>Returns the packed offsets buffer for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetMultiCategoryWeights/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryWeights</strong>
<em>Returns the packed weight buffer, or NULL when the attribute is unweighted.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetNetworkAttribute/">
<span>function</span>
<strong>CXNetworkGetNetworkAttribute</strong>
<em>Fetches a network attribute descriptor by name.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetNetworkAttributeBuffer/">
<span>function</span>
<strong>CXNetworkGetNetworkAttributeBuffer</strong>
<em>Returns a pointer to the raw network attribute buffer for the named attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetNodeAttribute/">
<span>function</span>
<strong>CXNetworkGetNodeAttribute</strong>
<em>Fetches a node attribute descriptor by name.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkGetNodeAttributeBuffer/">
<span>function</span>
<strong>CXNetworkGetNodeAttributeBuffer</strong>
<em>Returns a pointer to the raw node attribute buffer for the named attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMultiCategoryHasWeights/">
<span>function</span>
<strong>CXNetworkMultiCategoryHasWeights</strong>
<em>Returns CXTrue when the multi-category attribute stores per-entry weights.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNetworkAttributeCount/">
<span>function</span>
<strong>CXNetworkNetworkAttributeCount</strong>
<em>Returns the number of network attributes currently defined on the network.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNetworkAttributeNameAt/">
<span>function</span>
<strong>CXNetworkNetworkAttributeNameAt</strong>
<em>Returns the network attribute name at `index`, or NULL when out of range.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNodeAttributeCount/">
<span>function</span>
<strong>CXNetworkNodeAttributeCount</strong>
<em>Returns the number of node attributes currently defined on the network.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNodeAttributeNameAt/">
<span>function</span>
<strong>CXNetworkNodeAttributeNameAt</strong>
<em>Returns the node attribute name at `index` in the internal dictionary iteration order, or NULL when out of range.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkRemoveEdgeAttribute/">
<span>function</span>
<strong>CXNetworkRemoveEdgeAttribute</strong>
<em>Removes a sparse edge attribute and its storage.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkRemoveNetworkAttribute/">
<span>function</span>
<strong>CXNetworkRemoveNetworkAttribute</strong>
<em>Removes a sparse network attribute and its storage.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkRemoveNodeAttribute/">
<span>function</span>
<strong>CXNetworkRemoveNodeAttribute</strong>
<em>Removes a sparse node attribute and its storage.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSetAttributeCategoryDictionary/">
<span>function</span>
<strong>CXNetworkSetAttributeCategoryDictionary</strong>
<em>Replaces or remaps the category dictionary for a categorical attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSetMultiCategoryBuffers/">
<span>function</span>
<strong>CXNetworkSetMultiCategoryBuffers</strong>
<em>Replaces the packed offset/id/weight buffers for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSetMultiCategoryEntry/">
<span>function</span>
<strong>CXNetworkSetMultiCategoryEntry</strong>
<em>Writes one entry of a multi-category attribute using category ids.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSetMultiCategoryEntryByLabels/">
<span>function</span>
<strong>CXNetworkSetMultiCategoryEntryByLabels</strong>
<em>Writes one entry of a multi-category attribute using category labels.</em>
</a>
</div>


## Buffers And Versions

<p class="helios-api-group-description">Direct buffer access and version counters used by high-performance integrations.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXNetworkActiveEdgeIndexCount/">
<span>function</span>
<strong>CXNetworkActiveEdgeIndexCount</strong>
<em>Returns the number of entries in the stable active edge index buffer.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkActiveEdgeIndices/">
<span>function</span>
<strong>CXNetworkActiveEdgeIndices</strong>
<em>Returns a stable buffer of active edge indices in native active order.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkActiveNodeIndexCount/">
<span>function</span>
<strong>CXNetworkActiveNodeIndexCount</strong>
<em>Returns the number of entries in the stable active node index buffer.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkActiveNodeIndices/">
<span>function</span>
<strong>CXNetworkActiveNodeIndices</strong>
<em>Returns a stable buffer of active node indices in native active order.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgeActivityBuffer/">
<span>function</span>
<strong>CXNetworkEdgeActivityBuffer</strong>
<em>Provides a pointer to the edge activity bitmap.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgesBuffer/">
<span>function</span>
<strong>CXNetworkEdgesBuffer</strong>
<em>Returns a pointer to the flattened edge buffer `[from, to, ...]`.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkEdgeTopologyVersion/">
<span>function</span>
<strong>CXNetworkEdgeTopologyVersion</strong>
<em>Returns the edge topology version.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkIsEdgeActive/">
<span>function</span>
<strong>CXNetworkIsEdgeActive</strong>
<em>Returns CXTrue if the edge index is active.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkIsNodeActive/">
<span>function</span>
<strong>CXNetworkIsNodeActive</strong>
<em>Returns CXTrue if the given node index is currently active.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNodeActivityBuffer/">
<span>function</span>
<strong>CXNetworkNodeActivityBuffer</strong>
<em>Provides a pointer to the node activity bitmap in linear memory.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkNodeTopologyVersion/">
<span>function</span>
<strong>CXNetworkNodeTopologyVersion</strong>
<em>Returns the node topology version (increments on topology edits and repacks).</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkPromoteActiveEdgesForNodesToRenderEnd/">
<span>function</span>
<strong>CXNetworkPromoteActiveEdgesForNodesToRenderEnd</strong>
<em>Moves active edges incident to the supplied active nodes to the end of the native active edge order.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkPromoteActiveEdgesToRenderEnd/">
<span>function</span>
<strong>CXNetworkPromoteActiveEdgesToRenderEnd</strong>
<em>Moves active edge indices to the end of the native active order, preserving batch order.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkPromoteActiveNodesToRenderEnd/">
<span>function</span>
<strong>CXNetworkPromoteActiveNodesToRenderEnd</strong>
<em>Moves active node indices to the end of the native active order, preserving batch order.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkVersionString/">
<span>function</span>
<strong>CXNetworkVersionString</strong>
<em>Returns the semantic version string for the compiled library (e.g. &quot;1.2.3&quot;).</em>
</a>
</div>


## Selectors

<p class="helios-api-group-description">Node and edge selector containers used for filtering and set operations.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXEdgeSelectorClear/">
<span>function</span>
<strong>CXEdgeSelectorClear</strong>
<em>Clears all indices from an edge selector without releasing its capacity.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorCount/">
<span>function</span>
<strong>CXEdgeSelectorCount</strong>
<em>Returns how many indices are currently stored in the selector.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorCreate/">
<span>function</span>
<strong>CXEdgeSelectorCreate</strong>
<em>Creates a selector object for edges.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorData/">
<span>function</span>
<strong>CXEdgeSelectorData</strong>
<em>Returns a pointer to the selector&#x27;s index data.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorDestroy/">
<span>function</span>
<strong>CXEdgeSelectorDestroy</strong>
<em>Releases all heap memory associated with an edge selector.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorFillAll/">
<span>function</span>
<strong>CXEdgeSelectorFillAll</strong>
<em>Populates the selector with every active edge.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorFillFromArray/">
<span>function</span>
<strong>CXEdgeSelectorFillFromArray</strong>
<em>Fills the selector with the provided edge indices.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorFilterActive/">
<span>function</span>
<strong>CXEdgeSelectorFilterActive</strong>
<em>Removes invalid/inactive indices in-place from an edge selector.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorFilterByNodes/">
<span>function</span>
<strong>CXEdgeSelectorFilterByNodes</strong>
<em>Keeps only active edges whose endpoints are both present in `nodeSelector`.</em>
</a>
<a class="helios-api-directory-item" href="CXEdgeSelectorIntersect/">
<span>function</span>
<strong>CXEdgeSelectorIntersect</strong>
<em>Intersects an edge selector in-place with another selector (active indices only).</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorClear/">
<span>function</span>
<strong>CXNodeSelectorClear</strong>
<em>Clears all indices from a node selector without releasing its capacity.</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorCount/">
<span>function</span>
<strong>CXNodeSelectorCount</strong>
<em>Returns how many indices are currently stored in the selector.</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorCreate/">
<span>function</span>
<strong>CXNodeSelectorCreate</strong>
<em>Creates a selector object for nodes with an optional initial capacity.</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorData/">
<span>function</span>
<strong>CXNodeSelectorData</strong>
<em>Returns a pointer to the selector&#x27;s contiguous index data.</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorDestroy/">
<span>function</span>
<strong>CXNodeSelectorDestroy</strong>
<em>Releases all heap memory associated with a node selector.</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorFillAll/">
<span>function</span>
<strong>CXNodeSelectorFillAll</strong>
<em>Populates the selector with every active node.</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorFillFromArray/">
<span>function</span>
<strong>CXNodeSelectorFillFromArray</strong>
<em>Fills the selector with the provided node indices.</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorFilterActive/">
<span>function</span>
<strong>CXNodeSelectorFilterActive</strong>
<em>Removes invalid/inactive indices in-place from a node selector.</em>
</a>
<a class="helios-api-directory-item" href="CXNodeSelectorIntersect/">
<span>function</span>
<strong>CXNodeSelectorIntersect</strong>
<em>Intersects a node selector in-place with another selector (active indices only).</em>
</a>
</div>


## Queries

<p class="helios-api-group-description">Query parser and selector APIs.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXNetworkQueryLastErrorMessage/">
<span>function</span>
<strong>CXNetworkQueryLastErrorMessage</strong>
<em>Returns the most recent query parser/evaluator error message for this thread.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkQueryLastErrorOffset/">
<span>function</span>
<strong>CXNetworkQueryLastErrorOffset</strong>
<em>Returns the byte offset for the most recent query parser/evaluator error.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSelectEdgesByQuery/">
<span>function</span>
<strong>CXNetworkSelectEdgesByQuery</strong>
<em>Evaluates a query string against edges, populating the provided edge selector.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSelectNodesByQuery/">
<span>function</span>
<strong>CXNetworkSelectNodesByQuery</strong>
<em>Evaluates a query string against the network, populating the provided selector. Returns CXFalse on parse or evaluation errors. Use CXNetworkQueryLastError* to retrieve details about the last failure.</em>
</a>
</div>


## Serialization

<p class="helios-api-group-description">Readers and writers for BXNet, ZXNet, XNet, GML, and node-link JSON.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXNetworkReadBXNet/">
<span>function</span>
<strong>CXNetworkReadBXNet</strong>
<em>Reads an uncompressed BXNet file from disk.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkReadGML/">
<span>function</span>
<strong>CXNetworkReadGML</strong>
<em>Reads a graph from a GML file. Accepts standard GML and a looser dialect that tolerates quoted keys and unquoted scalar strings. @param path Path to the `.gml` file on disk. @return Newly allocated network when successful, otherwise NULL.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkReadGT/">
<span>function</span>
<strong>CXNetworkReadGT</strong>
<em>Reads a graph-tool `.gt` binary graph file. Supports the v1 graph-tool wire format, including endian-aware topology loading and the scalar/vector property-map types that map cleanly to Helios attributes. Unsupported or lossy property maps are skipped and reported via `CXNetworkSerializationLastWarningMessage()`. @param path Path to the `.gt` file on disk. @return Newly allocated network when successful, otherwise NULL.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkReadXNet/">
<span>function</span>
<strong>CXNetworkReadXNet</strong>
<em>Reads a graph from an `.xnet` (XNET 1.0.0 or legacy) container. @param path Path to the XNET file on disk. @return Newly allocated network when successful, otherwise NULL.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkReadZXNet/">
<span>function</span>
<strong>CXNetworkReadZXNet</strong>
<em>Reads a BGZF-compressed ZXNet file from disk.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSerializationLastWarningMessage/">
<span>function</span>
<strong>CXNetworkSerializationLastWarningMessage</strong>
<em>Returns the last non-fatal serialization warning emitted by a save/load helper.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSerializationWarningAppend/">
<span>function</span>
<strong>CXNetworkSerializationWarningAppend</strong>
<em>Appends a formatted message to the shared serialization warning buffer.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkSerializationWarningClear/">
<span>function</span>
<strong>CXNetworkSerializationWarningClear</strong>
<em>Clears the shared serialization warning buffer.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteActiveEdgeNodeAttributes/">
<span>function</span>
<strong>CXNetworkWriteActiveEdgeNodeAttributes</strong>
<em>Writes `componentsPerNode` values for each endpoint of active edges from the provided node attribute buffer into a caller-managed destination. Values are copied verbatim; the caller controls element width (`componentSizeBytes`) and must ensure the typed views line up with the provided byte offsets. Returns the number of edges that would be written; when `dstCapacityEdges` is too small, the required count is returned and no writes occur.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteActiveEdges/">
<span>function</span>
<strong>CXNetworkWriteActiveEdges</strong>
<em>Writes active edge indices into caller-provided storage. When `capacity` is insufficient the required size is returned and no writes occur.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteActiveEdgeSegments/">
<span>function</span>
<strong>CXNetworkWriteActiveEdgeSegments</strong>
<em>Writes two position vectors per active edge directly into the provided buffer. `componentsPerNode` describes how many floats to copy per endpoint (commonly 4 for vec4 data). Returns the number of edges that would be written; when `dstCapacityEdges` is too small, the required count is returned and no writes occur.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteActiveNodes/">
<span>function</span>
<strong>CXNetworkWriteActiveNodes</strong>
<em>Writes active node indices into caller-provided storage. When `capacity` is insufficient the required size is returned and no writes occur.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteBXNet/">
<span>function</span>
<strong>CXNetworkWriteBXNet</strong>
<em>Writes an uncompressed binary BXNet file to disk.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteBXNetFiltered/">
<span>function</span>
<strong>CXNetworkWriteBXNetFiltered</strong>
<em>Writes a BXNet file while allowing or ignoring selected attributes by scope.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteGML/">
<span>function</span>
<strong>CXNetworkWriteGML</strong>
<em>Serializes a network as GML. Lossy cases (for example unsupported attribute payloads or renamed keys) are reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.gml` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteGT/">
<span>function</span>
<strong>CXNetworkWriteGT</strong>
<em>Serializes a network as a graph-tool `.gt` binary graph file. `.gt` is an interoperability format. Helios-specific state and unsupported attributes may be skipped or converted, with warnings reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.gt` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteNodeLinkJSON/">
<span>function</span>
<strong>CXNetworkWriteNodeLinkJSON</strong>
<em>Serializes a network as node-link JSON compatible with common D3/NetworkX style payloads. Lossy cases are reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.json` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteXNet/">
<span>function</span>
<strong>CXNetworkWriteXNet</strong>
<em>Serializes a network using the XNET 1.0.0 human-readable container. Performs compaction to ensure contiguous node and edge indices before writing. Adds the `_original_ids_` vertex attribute to preserve the original node identifiers. @param network Network to serialize. @param path Output path for the `.xnet` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteXNetFiltered/">
<span>function</span>
<strong>CXNetworkWriteXNetFiltered</strong>
<em>Serializes an XNET file while allowing or ignoring selected attributes. Attribute filters are split by node, edge, and graph/network scope. @param network Network to serialize. @param path Output path for the `.xnet` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteZXNet/">
<span>function</span>
<strong>CXNetworkWriteZXNet</strong>
<em>Writes a BGZF-compressed ZXNet file to disk.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkWriteZXNetFiltered/">
<span>function</span>
<strong>CXNetworkWriteZXNetFiltered</strong>
<em>Writes a ZXNet file while allowing or ignoring selected attributes by scope.</em>
</a>
</div>


## Measurements

<p class="helios-api-group-description">One-shot graph measurements such as degree, strength, clustering, dimension, and centrality.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXNetworkLeidenModularity/">
<span>function</span>
<strong>CXNetworkLeidenModularity</strong>
<em>Runs Leiden community detection optimizing (weighted) modularity. - For undirected graphs, uses the standard modularity objective. - For directed graphs, uses the directed modularity formulation. - `resolution` corresponds to the modularity resolution parameter (gamma). - When `edgeWeightAttribute` is NULL/empty, every edge has weight 1. Writes the resulting community id into a node attribute (created when missing) of type `CXUnsignedIntegerAttributeType` and dimension 1. Returns the number of detected communities, or 0 on failure.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureBetweennessCentrality/">
<span>function</span>
<strong>CXNetworkMeasureBetweennessCentrality</strong>
<em>Runs Brandes betweenness centrality (weighted when an edge weight attribute is provided, unweighted otherwise). - `sourceNodes` can restrict the set of source nodes used by the algorithm. When NULL/empty, all active nodes are used. - Set `accumulate` to CXTrue to add into `inOutNodeBetweenness` instead of clearing it first (useful for chunked stepping). - Output buffer length must be at least `CXNetworkNodeCapacity(network)`. Returns the number of source nodes actually processed.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureConnectedComponents/">
<span>function</span>
<strong>CXNetworkMeasureConnectedComponents</strong>
<em>Measures connected components. - Weak mode treats directed edges as undirected (weakly-connected components). - Strong mode computes strongly-connected components on directed graphs. Undirected graphs behave like weak mode. Component ids are written into `outNodeComponent` (length must be at least `CXNetworkNodeCapacity(network)`). Inactive nodes receive id `0`. Returns the number of detected components.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureCoreness/">
<span>function</span>
<strong>CXNetworkMeasureCoreness</strong>
<em>Measures node coreness (k-core index) for all node capacity indices. - Uses iterative peeling over the chosen degree policy (`direction`). - For directed graphs: - `Out` uses outgoing degree. - `In` uses incoming degree. - `Both` uses incoming + outgoing degree. - For undirected graphs, direction is normalized to undirected degree. Output buffer length must be at least `CXNetworkNodeCapacity(network)`. Inactive nodes receive coreness 0.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureDegree/">
<span>function</span>
<strong>CXNetworkMeasureDegree</strong>
<em>Measures node degree for every node index (inactive nodes receive 0). Output buffer length must be at least `CXNetworkNodeCapacity(network)`.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureDimension/">
<span>function</span>
<strong>CXNetworkMeasureDimension</strong>
<em>Computes global multiscale dimension statistics over a node set. - If `nodes` is NULL or `nodeCount` is 0, all active nodes are used. - Invalid/inactive node ids in `nodes` are ignored. - Output buffers, when non-null, must each have length `maxLevel + 1`. Returns the number of nodes actually measured.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureEigenvectorCentrality/">
<span>function</span>
<strong>CXNetworkMeasureEigenvectorCentrality</strong>
<em>Runs power-iteration eigenvector centrality. - `initialNodeCentrality`, when non-null, must have one value per node capacity index and is used as the initial vector. - `outNodeCentrality` must have one value per node capacity index. - `executionMode` allows callers to force single-thread or parallel mode.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureLocalClusteringCoefficient/">
<span>function</span>
<strong>CXNetworkMeasureLocalClusteringCoefficient</strong>
<em>Measures local clustering coefficients for all node indices. - `variant` selects the unweighted or weighted formulation. - Weighted variants read `edgeWeightAttribute` (unit weights when omitted). Output buffer length must be at least `CXNetworkNodeCapacity(network)`.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureNodeDimension/">
<span>function</span>
<strong>CXNetworkMeasureNodeDimension</strong>
<em>Computes local multiscale capacity and dimension for a single node. - `maxLevel` controls the largest geodesic radius r evaluated. - `method` and `order` select the derivative estimator (FW/BK/CE/LS). - `outCapacity` and `outDimension`, when non-null, must point to buffers of length `maxLevel + 1`. Returns CXFalse when the node is invalid/inactive or on allocation failure.</em>
</a>
<a class="helios-api-directory-item" href="CXNetworkMeasureStrength/">
<span>function</span>
<strong>CXNetworkMeasureStrength</strong>
<em>Measures node strength from an edge weight attribute (or unit weights when `edgeWeightAttribute` is NULL/empty). Output buffer length must be at least `CXNetworkNodeCapacity(network)`.</em>
</a>
</div>


## Measurement Sessions

<p class="helios-api-group-description">Steppable native measurement sessions for long-running algorithms.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="CXConnectedComponentsSessionCreate/">
<span>function</span>
<strong>CXConnectedComponentsSessionCreate</strong>
<em>Creates a steppable connected-components session.</em>
</a>
<a class="helios-api-directory-item" href="CXConnectedComponentsSessionDestroy/">
<span>function</span>
<strong>CXConnectedComponentsSessionDestroy</strong>
<em>Releases all resources held by a connected-components session.</em>
</a>
<a class="helios-api-directory-item" href="CXConnectedComponentsSessionFinalize/">
<span>function</span>
<strong>CXConnectedComponentsSessionFinalize</strong>
<em>Finalizes a completed session, copying per-node component ids into `outNodeComponent` (length &gt;= nodeCapacity).</em>
</a>
<a class="helios-api-directory-item" href="CXConnectedComponentsSessionGetProgress/">
<span>function</span>
<strong>CXConnectedComponentsSessionGetProgress</strong>
<em>Returns current progress metrics. Any output pointer may be NULL.</em>
</a>
<a class="helios-api-directory-item" href="CXConnectedComponentsSessionStep/">
<span>function</span>
<strong>CXConnectedComponentsSessionStep</strong>
<em>Advances the session by at most `budget` node-visits (best effort).</em>
</a>
<a class="helios-api-directory-item" href="CXCorenessSessionCreate/">
<span>function</span>
<strong>CXCorenessSessionCreate</strong>
<em>Creates a steppable coreness session.</em>
</a>
<a class="helios-api-directory-item" href="CXCorenessSessionDestroy/">
<span>function</span>
<strong>CXCorenessSessionDestroy</strong>
<em>Releases all resources held by a coreness session.</em>
</a>
<a class="helios-api-directory-item" href="CXCorenessSessionFinalize/">
<span>function</span>
<strong>CXCorenessSessionFinalize</strong>
<em>Finalizes a completed session, copying per-node coreness values into `outNodeCoreness` (length &gt;= nodeCapacity).</em>
</a>
<a class="helios-api-directory-item" href="CXCorenessSessionGetProgress/">
<span>function</span>
<strong>CXCorenessSessionGetProgress</strong>
<em>Returns current progress metrics. Any output pointer may be NULL.</em>
</a>
<a class="helios-api-directory-item" href="CXCorenessSessionStep/">
<span>function</span>
<strong>CXCorenessSessionStep</strong>
<em>Advances the session by at most `budget` peeled nodes (best effort).</em>
</a>
<a class="helios-api-directory-item" href="CXLeidenSessionCreate/">
<span>function</span>
<strong>CXLeidenSessionCreate</strong>
<em>Creates a steppable Leiden session. The network topology and relevant edge weight attribute must not change while the session is active. Returns NULL on failure.</em>
</a>
<a class="helios-api-directory-item" href="CXLeidenSessionDestroy/">
<span>function</span>
<strong>CXLeidenSessionDestroy</strong>
<em>Releases all resources held by a Leiden session.</em>
</a>
<a class="helios-api-directory-item" href="CXLeidenSessionFinalize/">
<span>function</span>
<strong>CXLeidenSessionFinalize</strong>
<em>Finalizes a completed session, writing the resulting community ids into a node attribute of type `CXUnsignedIntegerAttributeType` (dimension 1). Returns CXFalse if the session has not completed or on failure.</em>
</a>
<a class="helios-api-directory-item" href="CXLeidenSessionGetProgress/">
<span>function</span>
<strong>CXLeidenSessionGetProgress</strong>
<em>Returns current progress metrics. Any output pointer may be NULL. `outProgressCurrent` and `outProgressTotal` are best-effort and may change as the algorithm advances (i.e. the total may be revised).</em>
</a>
<a class="helios-api-directory-item" href="CXLeidenSessionStep/">
<span>function</span>
<strong>CXLeidenSessionStep</strong>
<em>Advances the session by at most `budget` node-visits (best effort). Returns the current phase after stepping.</em>
</a>
</div>



## Coverage Notes

The extractor reads `CX_EXTERN` declarations and the nearest preceding Doxygen-style block comment. Internal bundled headers and uthash/utarray compatibility headers are intentionally excluded. For more precise grouping later, add a section annotation to the Doxygen block and wire it into `scripts/generate_api_reference.py`.

- No missing C comment summaries detected for extracted declarations.
