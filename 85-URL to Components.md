## Utility 85: URL to Components (Break URL Into Parts)

### What It Does

Parses a URL and returns a clean dictionary containing:

* scheme
* host
* port (if present)
* path
* query string
* fragment

Useful for:

* URL inspection
* Debugging
* Proxy/middleware logic
* Request rewriting

---

### Code Example

```python
from urllib.parse import urlparse

def url_to_components(url):
    parsed = urlparse(url)
    return {
        "scheme": parsed.scheme,
        "host": parsed.hostname,
        "port": parsed.port,
        "path": parsed.path,
        "query": parsed.query,
        "fragment": parsed.fragment
    }

# Example
url = "https://example.com:8080/api/v1/users?page=5#info"
print(url_to_components(url))
```

---

### Example Output

```
{
  'scheme': 'https',
  'host': 'example.com',
  'port': 8080,
  'path': '/api/v1/users',
  'query': 'page=5',
  'fragment': 'info'
}
```

---

### Notes

* Works with and without a port.
* Does not modify or normalize any part.

---

### Next Step

Utili
