## Utility 25: Extract Domain from URL

### What It Does

Extracts the domain name from a full URL.

### Code Example

```python
from urllib.parse import urlparse

def extract_domain(url):
    parsed = urlparse(url)
    return parsed.netloc

print(extract_domain("https://docs.python.org/3/tutorial/"))
# Output: docs.python.org
```

### Notes

* Uses Python's built-in `urlparse` for reliability.
* Handles subdomains, ports, and paths correctly.

---

### Next Step

Utility 26: Normalize URL.
