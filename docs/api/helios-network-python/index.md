
# Helios Network Python API

<p class="helios-api-version">Version 0.10.2</p>

The Python API provides a convenient wrapper for the native graph core plus file readers and conversion utilities for common graph ecosystems.

## Network

<p class="helios-api-group-description">The main Python wrapper around the native graph core.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="Network/">
<span>class</span>
<strong>Network</strong>
<em>Python convenience wrapper around the Helios C core network.</em>
</a>
</div>


## Import And Conversion

<p class="helios-api-group-description">Readers and conversion helpers for BXNet, ZXNet, XNet, GML, node-link JSON, NetworkX, and igraph.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="from_igraph/">
<span>function</span>
<strong>from_igraph</strong>
<em>Create a Helios `Network` from an igraph `Graph`.</em>
</a>
<a class="helios-api-directory-item" href="from_networkx/">
<span>function</span>
<strong>from_networkx</strong>
<em>Create a Helios `Network` from a NetworkX `Graph` or `DiGraph`.</em>
</a>
<a class="helios-api-directory-item" href="read_bxnet/">
<span>function</span>
<strong>read_bxnet</strong>
<em>Read a binary `.bxnet` file into a `Network`.</em>
</a>
<a class="helios-api-directory-item" href="read_gml/">
<span>function</span>
<strong>read_gml</strong>
<em>Read a GML graph file into a `Network`.</em>
</a>
<a class="helios-api-directory-item" href="read_gt/">
<span>function</span>
<strong>read_gt</strong>
<em>Read a graph-tool `.gt` file into a `Network`.</em>
</a>
<a class="helios-api-directory-item" href="read_node_link_json/">
<span>function</span>
<strong>read_node_link_json</strong>
<em>Read a D3/NetworkX-style node-link JSON file into a `Network`.</em>
</a>
<a class="helios-api-directory-item" href="read_xnet/">
<span>function</span>
<strong>read_xnet</strong>
<em>Read a text `.xnet` file into a `Network`.</em>
</a>
<a class="helios-api-directory-item" href="read_zxnet/">
<span>function</span>
<strong>read_zxnet</strong>
<em>Read a compressed `.zxnet` file into a `Network`.</em>
</a>
<a class="helios-api-directory-item" href="to_igraph/">
<span>function</span>
<strong>to_igraph</strong>
<em>Convert a Helios `Network` to an igraph `Graph` with compatible attributes.</em>
</a>
<a class="helios-api-directory-item" href="to_networkx/">
<span>function</span>
<strong>to_networkx</strong>
<em>Convert a Helios `Network` to a NetworkX graph with compatible attributes.</em>
</a>
</div>


## UMAP

<p class="helios-api-group-description">UMAP integration helpers that export fuzzy and nearest-neighbor graphs as Helios networks.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="HeliosUMAP/">
<span>class</span>
<strong>HeliosUMAP</strong>
<em>Build UMAP embeddings with umap-learn while exporting the fuzzy graph and optional kNN graph as Helios networks.</em>
</a>
<a class="helios-api-directory-item" href="NetworkExportResult/">
<span>class</span>
<strong>NetworkExportResult</strong>
<em>Result record returned by UMAP graph export helpers.</em>
</a>
</div>


## Enums And Models

<p class="helios-api-group-description">Enums and small model classes shared with the native core.</p>
<div class="helios-api-directory">
<a class="helios-api-directory-item" href="AttributeScope/">
<span>class</span>
<strong>AttributeScope</strong>
<em>Scopes where attributes can be attached: nodes, edges, or graph-level metadata.</em>
</a>
<a class="helios-api-directory-item" href="AttributeType/">
<span>class</span>
<strong>AttributeType</strong>
<em>Attribute storage types supported by the Helios native core.</em>
</a>
<a class="helios-api-directory-item" href="CategorySortOrder/">
<span>class</span>
<strong>CategorySortOrder</strong>
<em>Ordering policies for category dictionaries derived from string attributes.</em>
</a>
<a class="helios-api-directory-item" href="ClusteringVariant/">
<span>class</span>
<strong>ClusteringVariant</strong>
<em>Formula selector for local clustering coefficient measurements.</em>
</a>
<a class="helios-api-directory-item" href="ConnectedComponentsMode/">
<span>class</span>
<strong>ConnectedComponentsMode</strong>
<em>Weak or strong connected-component mode.</em>
</a>
<a class="helios-api-directory-item" href="DimensionMethod/">
<span>class</span>
<strong>DimensionMethod</strong>
<em>Finite-difference method used by multiscale dimension measurements.</em>
</a>
<a class="helios-api-directory-item" href="encode_binary_batch/">
<span>function</span>
<strong>encode_binary_batch</strong>
<em>Encode mutation events into the Helios network binary batch protocol.</em>
</a>
<a class="helios-api-directory-item" href="generate_barabasi_albert/">
<span>function</span>
<strong>generate_barabasi_albert</strong>
<em>Generate a Barabasi-Albert preferential attachment network.</em>
</a>
<a class="helios-api-directory-item" href="generate_configuration_model/">
<span>function</span>
<strong>generate_configuration_model</strong>
<em>Generate a configuration model network from a degree sequence.</em>
</a>
<a class="helios-api-directory-item" href="generate_lattice_2d/">
<span>function</span>
<strong>generate_lattice_2d</strong>
<em>Generate a 2D lattice network.</em>
</a>
<a class="helios-api-directory-item" href="generate_random_geometric/">
<span>function</span>
<strong>generate_random_geometric</strong>
<em>Generate a random geometric unit-disk network.</em>
</a>
<a class="helios-api-directory-item" href="generate_small_world/">
<span>function</span>
<strong>generate_small_world</strong>
<em>Alias for `generate_watts_strogatz`.</em>
</a>
<a class="helios-api-directory-item" href="generate_stochastic_block_model/">
<span>function</span>
<strong>generate_stochastic_block_model</strong>
<em>Generate a stochastic block model network.</em>
</a>
<a class="helios-api-directory-item" href="generate_watts_strogatz/">
<span>function</span>
<strong>generate_watts_strogatz</strong>
<em>Generate a Watts-Strogatz small-world network.</em>
</a>
<a class="helios-api-directory-item" href="generate_waxman/">
<span>function</span>
<strong>generate_waxman</strong>
<em>Generate a Waxman geometric network.</em>
</a>
<a class="helios-api-directory-item" href="MeasurementExecutionMode/">
<span>class</span>
<strong>MeasurementExecutionMode</strong>
<em>Execution policy for native measurements that support serial or parallel kernels.</em>
</a>
<a class="helios-api-directory-item" href="mutation_events_to_text_batch/">
<span>function</span>
<strong>mutation_events_to_text_batch</strong>
<em>Convert mutation events to the text batch format understood by JS.</em>
</a>
<a class="helios-api-directory-item" href="NeighborDirection/">
<span>class</span>
<strong>NeighborDirection</strong>
<em>Traversal direction for neighbor queries and directed graph measurements.</em>
</a>
<a class="helios-api-directory-item" href="StrengthMeasure/">
<span>class</span>
<strong>StrengthMeasure</strong>
<em>Edge-weight aggregation used by strength measurements.</em>
</a>
</div>



## Coverage Notes

The structured reference is available at [`../reference.json`](../reference.json).

- No missing docstring summaries detected for extracted public Python symbols.
