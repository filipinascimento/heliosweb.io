# CXNetworkWriteBXNetFiltered

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetworkBXNet.h:93</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Writes a BXNet file while allowing or ignoring selected attributes by scope.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkWriteBXNetFiltered(struct CXNetwork *network, const char *path, const char **nodeAllow, size_t nodeAllowCount, const char **nodeIgnore, size_t nodeIgnoreCount, const char **edgeAllow, size_t edgeAllowCount, const char **edgeIgnore, size_t edgeIgnoreCount, const char **networkAllow, size_t networkAllowCount, const char **networkIgnore, size_t networkIgnoreCount);
```

</div>
