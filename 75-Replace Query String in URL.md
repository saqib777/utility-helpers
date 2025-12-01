## Utility 75: Replace Query String in URL

### What It Does

Replaces the entire query string of a URL while keeping:

* Scheme (http/https)
* Domain
* Path

Useful for:

* Resetting filters
* Applying new parameters
* Sanitizing URLs

---

### Code Example

```python
from urllib.parse import urlparse, urlunparse

def replace_querystring(url, new_qs):
    parts = list(urlparse(url))
    parts[4] = new_qs  # Query component
    return urlunparse(parts)

# Example
url = "https://example.com/products?page=1&sort=asc"
new_qs = "page=2&filter=active"

print(replace_querystring(url, new_qs))
# https://example.com/products?page=2&filter=active
```

---

### Notes

* Does not modify path or hostname.
* Use with `json_to_querystring`, `merge_querystrings`, etc.

---

### Next Step

Ready for **Utility 76** whenever you are.
