## Utility 70: Normalize Query String (Sort Keys Alphabetically)

### What It Does

Reorders a URL query string so that its keys appear in alphabetical order. Useful for:

* Creating canonical URLs
* Cache key normalization
* Signature generation

---

### Code Example

```python
from urllib.parse import parse_qs, urlencode

def normalize_querystring(qs):
    parsed = parse_qs(qs)

    # Convert parsed lists back to simple values when possible
    cleaned = {k: v[0] if len(v) == 1 else v for k, v in parsed.items()}

    # Sort keys alphabetically
    sorted_items = dict(sorted(cleaned.items(), key=lambda x: x[0]))

    return urlencode(sorted_items, doseq=True)

# Example
qs = "sort=desc&page=2&filter=active"
print(normalize_querystring(qs))
# filter=active&page=2&sort=desc
```

---

### Notes

* Supports multi-value fields.
* Ensures consistent ordering for hashing and caching.

---

### Next Step

Utility 71: Add or update a parameter in a query string.
