## Utility 83: Add or Replace URL Fragment

### What It Does

Sets or updates the fragment (the part after `#`) in a URL.
The scheme, host, path, and query stay the same.

Useful for:

* Navigation anchors
* Documentation URLs
* Hash‑based routing (common in SPAs)

---

### Code Example

```python
from urllib.parse import urlparse, urlunparse

def set_url_fragment(url, fragment):
    parsed = urlparse(url)
    updated = parsed._replace(fragment=fragment)
    return urlunparse(updated)

# Example
url = "https://example.com/products?page=3"
print(set_url_fragment(url, "details"))
# https://example.com/products?page=3#details
```

---

### Notes

* Replaces any existing fragment.
* Fragment is never URL‑encoded by default.

---

### Next Step

Utility 84 will follow automatically.
