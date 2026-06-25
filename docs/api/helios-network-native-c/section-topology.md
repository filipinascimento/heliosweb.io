
# Topology

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

Node, edge, neighbor, compaction, and topology mutation APIs.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXNetworkAddEdges/">
<span>function</span>
<strong>CXNetworkAddEdges</strong>
<em>Inserts the provided edges, writing the new indices to `outIndices` when supplied. Edges are expressed as contiguous (from,to) pairs.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkAddNodes/">
<span>function</span>
<strong>CXNetworkAddNodes</strong>
<em>Appends `count` new nodes to the network. When `outIndices` is non-null it receives the indices assigned to the created nodes.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkCollectNeighbors/">
<span>function</span>
<strong>CXNetworkCollectNeighbors</strong>
<em>Collects unique one-hop neighbors for one or more source nodes. - `sourceNodes` can contain any node ids; inactive/out-of-range entries are ignored. - `direction` controls traversal for directed graphs (`out`, `in`, `both`). - `includeSourceNodes` controls whether source nodes can appear in `outNodeSelector`. - `outEdgeSelector` is optional; pass NULL to skip edge collection.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkCollectNeighborsAtLevel/">
<span>function</span>
<strong>CXNetworkCollectNeighborsAtLevel</strong>
<em>Collects neighbors at exactly the given concentric level (shortest-path hop distance). - `level == 0` refers to the source set itself. - `includeSourceNodes` only affects whether level-0 source nodes are included. - `outEdgeSelector` is optional; pass NULL to skip edge collection.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkCollectNeighborsUpToLevel/">
<span>function</span>
<strong>CXNetworkCollectNeighborsUpToLevel</strong>
<em>Collects neighbors up to (and including) the given concentric level. - `maxLevel == 0` returns only the source set when `includeSourceNodes` is true. - `outEdgeSelector` is optional; pass NULL to skip edge collection.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkCompact/">
<span>function</span>
<strong>CXNetworkCompact</strong>
<em>Compacts the network so that node and edge indices become contiguous starting at zero and capacities shrink to match the number of active elements. When `nodeOriginalIndexAttr` or `edgeOriginalIndexAttr` are provided, the function records the previous indices in attributes of type `CXUnsignedIntegerAttributeType`. Returns CXFalse on allocation failure or when incompatible attributes are encountered.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgeCapacity/">
<span>function</span>
<strong>CXNetworkEdgeCapacity</strong>
<em>Returns the allocated edge capacity.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgeCount/">
<span>function</span>
<strong>CXNetworkEdgeCount</strong>
<em>Returns the number of active edges currently stored.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgeFreeListCapacity/">
<span>function</span>
<strong>CXNetworkEdgeFreeListCapacity</strong>
<em>Returns the allocated edge free-list capacity (reserved slots).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgeFreeListCount/">
<span>function</span>
<strong>CXNetworkEdgeFreeListCount</strong>
<em>Returns the current edge free-list size (recycled indices).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetEdgeValidRange/">
<span>function</span>
<strong>CXNetworkGetEdgeValidRange</strong>
<em>Returns the min/max active edge indices as [start,end).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetNodeValidRange/">
<span>function</span>
<strong>CXNetworkGetNodeValidRange</strong>
<em>Returns the min/max active node indices as [start,end).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkInNeighbors/">
<span>function</span>
<strong>CXNetworkInNeighbors</strong>
<em>Returns the inbound neighbor container for the given node.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNodeCapacity/">
<span>function</span>
<strong>CXNetworkNodeCapacity</strong>
<em>Returns the allocated node capacity (useful for buffer sizing).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNodeCount/">
<span>function</span>
<strong>CXNetworkNodeCount</strong>
<em>Returns the number of active nodes currently stored.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNodeFreeListCapacity/">
<span>function</span>
<strong>CXNetworkNodeFreeListCapacity</strong>
<em>Returns the allocated node free-list capacity (reserved slots).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNodeFreeListCount/">
<span>function</span>
<strong>CXNetworkNodeFreeListCount</strong>
<em>Returns the current node free-list size (recycled indices).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkOutNeighbors/">
<span>function</span>
<strong>CXNetworkOutNeighbors</strong>
<em>Returns the outbound neighbor container for the given node.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkRemoveEdges/">
<span>function</span>
<strong>CXNetworkRemoveEdges</strong>
<em>Removes the supplied edges from the network.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkRemoveNodes/">
<span>function</span>
<strong>CXNetworkRemoveNodes</strong>
<em>Removes the supplied nodes, reclaiming their indices for future use.</em>
</a>
</div>
