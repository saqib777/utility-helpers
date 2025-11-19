## Utility 26: Normalize URL

### What It Does

Normalizes a URL into a consistent format by:

* Lowercasing the scheme and domain
* Removing trailing slashes
* Ensuring path formatting is clean

### Code Example

```python
from urllib.parse import urlparse, urlunparse

def normalize_url(url):
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    netloc = parsed.netloc.lower()
    path = parsed.path.rstrip('/')
    return urlunparse((scheme, netloc, path, '', '', ''))

print(normalize_url("HTTPS://Example.COM/docs/") )
# Output: https://example.com/docs
```

### Notes

* Helpful for comparing or storing URLs consistently.
* Removes unnecessary trailing slashes.

---

### Next Step

Utility 27: Extract file extension from filename or URL.
