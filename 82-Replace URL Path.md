## Utility 82: Replace URL Path

### What It Does

Replaces the entire path of a URL while keeping:

* scheme (http/https)
* host
* query string
* fragment

Useful for routing, rewriting endpoints, or redirect logic.

---

### Code Example

```python
from urllib.parse import urlparse, urlunparse

def replace_url_path(url, new_path):
    parsed = urlparse(url)
    updated = parsed._replace(path=new_path)
    return urlunparse(updated)

# Example
url = "https://example.com/api/v1/users?page=2"
print(replace_url_path(url, "/api/v2/products"))
# https://example.com/api/v2/products?page=2
```

---

### Notes

* Leaves query and fragment untouched.
* Ensures clean path replacement.

---

### Next Step

Utility 83 will follow automatically.
