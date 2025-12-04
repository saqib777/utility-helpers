## Utility 79: Extract URL Path Segments

### What It Does

Breaks a URL's path into clean, individual segments. Helpful for routing, debugging, breadcrumb generation, and URL analysis.

---

### Code Example

```python
from urllib.parse import urlparse

def extract_path_segments(url):
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    return path.split('/') if path else []

# Example
url = "https://example.com/api/v1/users/123/profile"
print(extract_path_segments(url))
# ['api', 'v1', 'users', '123', 'profile']
```

---

### Notes

* Removes leading/trailing slashes.
* Returns an empty list if path is empty.

---

### Next Step

Utility 80 will follow next automatically.
