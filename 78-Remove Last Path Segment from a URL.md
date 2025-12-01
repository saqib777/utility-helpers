## Utility 78: Remove Last Path Segment from a URL

### What It Does

Removes the final path segment from a URL while keeping:

* Scheme
* Host
* Query parameters
* Fragment (if any)

Useful for navigating up one level in REST endpoints, folder structures, or cleaning URLs.

---

### Code Example

```python
from urllib.parse import urlparse, urlunparse

def remove_last_path_segment(url):
    parsed = urlparse(url)
    path_parts = parsed.path.rstrip('/').split('/')

    # Remove last segment if it exists
    if len(path_parts) > 1:
        new_path = '/'.join(path_parts[:-1])
    else:
        new_path = ''

    updated = parsed._replace(path=new_path)
    return urlunparse(updated)

# Example
url = "https://example.com/api/v1/users/123"
print(remove_last_path_segment(url))
# https://example.com/api/v1/users
```

---

### Notes

* Does not touch query string or fragment.
* Safe for root paths.

---

### Next Step

Utility 79 will be generated next automatically.
