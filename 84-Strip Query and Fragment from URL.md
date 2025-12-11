## Utility 84: Strip Query and Fragment from URL

### What It Does

Removes both the query string (`?param=value`) and the fragment (`#section`) from a URL.
The scheme, host, and path remain intact.

Useful for:

* Cleaning URLs
* Normalizing before caching
* Removing tracking parameters

---

### Code Example

```python
from urllib.parse import urlparse, urlunparse

def strip_query_and_fragment(url):
    parsed = urlparse(url)
    cleaned = parsed._replace(query="", fragment="")
    return urlunparse(cleaned)

# Example
url = "https://example.com/products?page=3#details"
print(strip_query_and_fragment(url))
# https://example.com/products
```

---

### Notes

* Does not touch the path.
* Ideal for canonical URL cleaning.

---

### Next Step

Utility 85 will follow automatically.
