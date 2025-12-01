## Utility 72: Remove Query Parameter

### What It Does

Removes a given key completely from a query string.

Useful for cleaning URLs, removing filters, or resetting parameters.

---

### Code Example

```python
from urllib.parse import parse_qs, urlencode

def remove_query_param(qs, key):
    parsed = parse_qs(qs)

    # Remove if exists
    if key in parsed:
        del parsed[key]

    return urlencode(parsed, doseq=True)

# Example
qs = "page=1&sort=asc&filter=active"
print(remove_query_param(qs, "filter"))
# page=1&sort=asc
```

---

### Notes

* Safe: does nothing if the key isn't present.
* Preserves all other parameters.

---

### Next Step

Utility 73: Check if a query parameter exists.
