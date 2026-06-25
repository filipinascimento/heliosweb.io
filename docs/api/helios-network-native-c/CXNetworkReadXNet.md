# CXNetworkReadXNet

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetworkXNet.h:18</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Reads a graph from an `.xnet` (XNET 1.0.0 or legacy) container. @param path Path to the XNET file on disk. @return Newly allocated network when successful, otherwise NULL.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN struct CXNetwork* CXNetworkReadXNet(const char *path);
```

</div>
