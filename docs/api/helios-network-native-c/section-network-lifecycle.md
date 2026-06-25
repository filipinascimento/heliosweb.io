
# Network Lifecycle

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

Allocation, destruction, version, and graph-wide metadata helpers.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXFreeNetwork/">
<span>function</span>
<strong>CXFreeNetwork</strong>
<em>Releases all resources owned by a network.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkBuildFilteredSubgraph/">
<span>function</span>
<strong>CXNetworkBuildFilteredSubgraph</strong>
<em>Builds an induced filtered subgraph from optional node/edge filters. - `nodeFilter` / `edgeFilter` may be NULL to indicate &quot;all active&quot;. - Node output is always active-only. - Edge output is always active-only and induced by the resulting node set (edges with at least one endpoint outside `outNodeSelector` are removed). - Output order follows native active index order.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGenerateBarabasiAlbert/">
<span>function</span>
<strong>CXNetworkGenerateBarabasiAlbert</strong>
<em>Creates a Barabasi-Albert preferential-attachment graph.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGenerateConfigurationModel/">
<span>function</span>
<strong>CXNetworkGenerateConfigurationModel</strong>
<em>Creates a graph with the requested degree sequence using the configuration model.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGenerateLattice2D/">
<span>function</span>
<strong>CXNetworkGenerateLattice2D</strong>
<em>Creates a two-dimensional lattice graph.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGenerateRandomGeometric/">
<span>function</span>
<strong>CXNetworkGenerateRandomGeometric</strong>
<em>Creates a random geometric graph using random 2D positions and a radius cutoff.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGenerateStochasticBlockModel/">
<span>function</span>
<strong>CXNetworkGenerateStochasticBlockModel</strong>
<em>Creates a stochastic block model graph from block sizes and a flattened block-to-block probability matrix.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGenerateWattsStrogatz/">
<span>function</span>
<strong>CXNetworkGenerateWattsStrogatz</strong>
<em>Creates a Watts-Strogatz small-world graph.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGenerateWaxman/">
<span>function</span>
<strong>CXNetworkGenerateWaxman</strong>
<em>Creates a Waxman random graph using distance-weighted edge probabilities.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkIsDirected/">
<span>function</span>
<strong>CXNetworkIsDirected</strong>
<em>Returns CXTrue when the network treats edges as directed.</em>
</a>
<a class="helios-api-directory-item" href="../CXNewNetwork/">
<span>function</span>
<strong>CXNewNetwork</strong>
<em>Allocates a new network with default capacities.</em>
</a>
<a class="helios-api-directory-item" href="../CXNewNetworkWithCapacity/">
<span>function</span>
<strong>CXNewNetworkWithCapacity</strong>
<em>Allocates a new network with explicit node/edge capacities.</em>
</a>
</div>
