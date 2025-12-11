## Utility 86: Components to URL (Rebuild URL From Parts)

### What It Does

Reconstructs a full URL from individual components:

* scheme
* host
* port (optional)
* path
* query
* fragment

Useful for:

* Rewriting URLs
* Modifying specific parts before reassembly
* Proxy routing
* API client utilities

---

### Code Example

```python
from urllib.parse import urlunparse

def components_to_url(components):
    scheme = components.get("scheme", "")
    host = components.get("host", "")
    port = components.get("port")
    path = components.get("path", "")
    query = components.get("query", "")
    fragment = components.get("fragment", "")

    # Build netloc (host[:port])
    if port:
        netloc = f"{host}:{port}"
    else:
        netloc = host

    return urlunparse((scheme, netloc, path, "", query, fragment))

# Example
components = {
    "scheme": "https",
    "host": "example.com",
    "port": 8080,
    "path": "/api/v2/items",
    "query": "page=10",
    "fragment": "details"
}

print(components_to_url(components))
# https://example.com:8080/api/v2/items?page=10#details
```

---

### Notes

* Complements Utility 85 (URL → Components).
* Ensures clean and valid URL reconstruction.

---

### Next Step

Utility 87 is ready whenever you want to continue.
