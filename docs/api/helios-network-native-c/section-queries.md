
# Queries

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

Query parser and selector APIs.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXNetworkQueryLastErrorMessage/">
<span>function</span>
<strong>CXNetworkQueryLastErrorMessage</strong>
<em>Returns the most recent query parser/evaluator error message for this thread.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkQueryLastErrorOffset/">
<span>function</span>
<strong>CXNetworkQueryLastErrorOffset</strong>
<em>Returns the byte offset for the most recent query parser/evaluator error.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSelectEdgesByQuery/">
<span>function</span>
<strong>CXNetworkSelectEdgesByQuery</strong>
<em>Evaluates a query string against edges, populating the provided edge selector.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSelectNodesByQuery/">
<span>function</span>
<strong>CXNetworkSelectNodesByQuery</strong>
<em>Evaluates a query string against the network, populating the provided selector. Returns CXFalse on parse or evaluation errors. Use CXNetworkQueryLastError* to retrieve details about the last failure.</em>
</a>
</div>
