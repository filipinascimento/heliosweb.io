# CXNetworkWriteXNetFiltered

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetworkXNet.h:54</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Serializes an XNET file while allowing or ignoring selected attributes. Attribute filters are split by node, edge, and graph/network scope. @param network Network to serialize. @param path Output path for the `.xnet` file. @return CXTrue on success, CXFalse on failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkWriteXNetFiltered(struct CXNetwork *network, const char *path, const char **nodeAllow, size_t nodeAllowCount, const char **nodeIgnore, size_t nodeIgnoreCount, const char **edgeAllow, size_t edgeAllowCount, const char **edgeIgnore, size_t edgeIgnoreCount, const char **graphAllow, size_t graphAllowCount, const char **graphIgnore, size_t graphIgnoreCount);
```

</div>
