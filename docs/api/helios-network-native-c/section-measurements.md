
# Measurements

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

One-shot graph measurements such as degree, strength, clustering, dimension, and centrality.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXNetworkLeidenModularity/">
<span>function</span>
<strong>CXNetworkLeidenModularity</strong>
<em>Runs Leiden community detection optimizing (weighted) modularity. - For undirected graphs, uses the standard modularity objective. - For directed graphs, uses the directed modularity formulation. - `resolution` corresponds to the modularity resolution parameter (gamma). - When `edgeWeightAttribute` is NULL/empty, every edge has weight 1. Writes the resulting community id into a node attribute (created when missing) of type `CXUnsignedIntegerAttributeType` and dimension 1. Returns the number of detected communities, or 0 on failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureBetweennessCentrality/">
<span>function</span>
<strong>CXNetworkMeasureBetweennessCentrality</strong>
<em>Runs Brandes betweenness centrality (weighted when an edge weight attribute is provided, unweighted otherwise). - `sourceNodes` can restrict the set of source nodes used by the algorithm. When NULL/empty, all active nodes are used. - Set `accumulate` to CXTrue to add into `inOutNodeBetweenness` instead of clearing it first (useful for chunked stepping). - Output buffer length must be at least `CXNetworkNodeCapacity(network)`. Returns the number of source nodes actually processed.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureConnectedComponents/">
<span>function</span>
<strong>CXNetworkMeasureConnectedComponents</strong>
<em>Measures connected components. - Weak mode treats directed edges as undirected (weakly-connected components). - Strong mode computes strongly-connected components on directed graphs. Undirected graphs behave like weak mode. Component ids are written into `outNodeComponent` (length must be at least `CXNetworkNodeCapacity(network)`). Inactive nodes receive id `0`. Returns the number of detected components.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureCoreness/">
<span>function</span>
<strong>CXNetworkMeasureCoreness</strong>
<em>Measures node coreness (k-core index) for all node capacity indices. - Uses iterative peeling over the chosen degree policy (`direction`). - For directed graphs: - `Out` uses outgoing degree. - `In` uses incoming degree. - `Both` uses incoming + outgoing degree. - For undirected graphs, direction is normalized to undirected degree. Output buffer length must be at least `CXNetworkNodeCapacity(network)`. Inactive nodes receive coreness 0.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureDegree/">
<span>function</span>
<strong>CXNetworkMeasureDegree</strong>
<em>Measures node degree for every node index (inactive nodes receive 0). Output buffer length must be at least `CXNetworkNodeCapacity(network)`.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureDimension/">
<span>function</span>
<strong>CXNetworkMeasureDimension</strong>
<em>Computes global multiscale dimension statistics over a node set. - If `nodes` is NULL or `nodeCount` is 0, all active nodes are used. - Invalid/inactive node ids in `nodes` are ignored. - Output buffers, when non-null, must each have length `maxLevel + 1`. Returns the number of nodes actually measured.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureEigenvectorCentrality/">
<span>function</span>
<strong>CXNetworkMeasureEigenvectorCentrality</strong>
<em>Runs power-iteration eigenvector centrality. - `initialNodeCentrality`, when non-null, must have one value per node capacity index and is used as the initial vector. - `outNodeCentrality` must have one value per node capacity index. - `executionMode` allows callers to force single-thread or parallel mode.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureLocalClusteringCoefficient/">
<span>function</span>
<strong>CXNetworkMeasureLocalClusteringCoefficient</strong>
<em>Measures local clustering coefficients for all node indices. - `variant` selects the unweighted or weighted formulation. - Weighted variants read `edgeWeightAttribute` (unit weights when omitted). Output buffer length must be at least `CXNetworkNodeCapacity(network)`.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureNodeDimension/">
<span>function</span>
<strong>CXNetworkMeasureNodeDimension</strong>
<em>Computes local multiscale capacity and dimension for a single node. - `maxLevel` controls the largest geodesic radius r evaluated. - `method` and `order` select the derivative estimator (FW/BK/CE/LS). - `outCapacity` and `outDimension`, when non-null, must point to buffers of length `maxLevel + 1`. Returns CXFalse when the node is invalid/inactive or on allocation failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMeasureStrength/">
<span>function</span>
<strong>CXNetworkMeasureStrength</strong>
<em>Measures node strength from an edge weight attribute (or unit weights when `edgeWeightAttribute` is NULL/empty). Output buffer length must be at least `CXNetworkNodeCapacity(network)`.</em>
</a>
</div>
