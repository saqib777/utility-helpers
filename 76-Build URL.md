## Utility 76: Build URL (Scheme + Host + Path + Query)

### What It Does

Constructs a complete URL from individual components:

* scheme (http/https)
* domain/host
* path
* query parameters (dict)

Useful for API clients, automated test scripts, dynamic URL generation, and microservices.

---

### Code Example

```python
from urllib.parse import urlencode, urlunparse

def build_url(scheme, host, path="", params=None):
    params = params or {}
    query = urlencode(params, doseq=True)
    return urlunparse((scheme, host, path, "", query, ""))

# Example
print(build_url(
    scheme="https",
    host="example.com",
    path="/products",
    params={"page": 2, "sort": "asc"}
))
# https://example.com/products?page=2&sort=asc
```

---

### Notes

* Automatically encodes parameters.
* Clean way to construct URLs programmatically.

---

### Next Step

Utility 77: Append path segments to a base URL.
