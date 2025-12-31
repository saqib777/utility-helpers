## 87: Validate URL Format

### What It Does

Checks whether a given string is a syntactically valid URL.
This is useful for input validation, API gateway checks, crawler utilities, and security filtering.

---

### Code Example

```python
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        parsed = urlparse(url)
        # A valid URL must have scheme and netloc
        return bool(parsed.scheme and parsed.netloc)
    except Exception:
        return False

# Examples
print(is_valid_url("https://example.com/path"))        # True
print(is_valid_url("ftp://files.server.net/download"))  # True
print(is_valid_url("not_a_url"))                       # False
print(is_valid_url("http:/broken.com"))                # False
```

---

### Notes

* Only validates structure, not reachability.
* Accepts any scheme (http, https, ftp, etc.).
* Does not validate domain existence.

---

### Next Step

Utility 88 will follow automatically when you say next.
