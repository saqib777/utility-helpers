## Utility 77: Append Path Segments to a URL

### What It Does

Safely appends one or more path segments to a base URL without breaking slashes or structure.

Useful for:

* Building REST API endpoints
* Constructing dynamic microservice routes
* Ensuring clean paths without double slashes

---

### Code Example

```python
from urllib.parse import urlparse, urlunparse

def append_url_path(url, *segments):
    parsed = urlparse(url)

    # Clean and join segments
    clean_segments = [s.strip('/') for s in segments]
    new_path = '/'.join([parsed.path.rstrip('/')] + clean_segments)

    updated = parsed._replace(path=new_path)
    return urlunparse(updated)

# Example
base = "https://api.example.com/v1"
print(append_url_path(base, "users", "123", "orders"))
# https://api.example.com/v1/users/123/orders
```

---

### Notes

* Removes accidental double slashes.
* Preserves query string and fragment if present.

---

### Next Step

Utility 78: Remove last path segment from a URL.
