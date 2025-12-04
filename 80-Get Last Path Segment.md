## Utility 80: Get Last Path Segment (Basename)

### What It Does

Extracts the final path segment from a URL.
Equivalent to `basename` for filesystem paths.

Useful for:

* Extracting resource IDs
* Parsing endpoints
* Building breadcrumbs

---

### Code Example

```python
from urllib.parse import urlparse

def get_last_path_segment(url):
    parsed = urlparse(url)
    path = parsed.path.rstrip('/')

    if not path:
        return ''

    return path.split('/')[-1]

# Example
url = "https://example.com/api/v1/users/123/profile"
print(get_last_path_segment(url))
# profile
```

---

### Notes

* Safe for trailing slashes.
* Returns empty string if no path exists.

---

### Next Step

Utility 81 will follow automatically.
