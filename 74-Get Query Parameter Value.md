## Utility 74: Get Query Parameter Value

### What It Does

Retrieves the value of a key in a query string.
If the key appears multiple times, it returns a **list**.
If it appears once, it returns a **single value**.

---

### Code Example

```python
from urllib.parse import parse_qs

def get_query_param(qs, key, default=None):
    parsed = parse_qs(qs)

    if key not in parsed:
        return default

    values = parsed[key]

    # Convert single-value lists to a plain value
    return values[0] if len(values) == 1 else values

# Example
qs = "page=1&sort=asc&tag=python&tag=testing"
print(get_query_param(qs, "page"))   # '1'
print(get_query_param(qs, "tag"))    # ['python', 'testing']
print(get_query_param(qs, "filter", "none"))  # 'none'
```

---

### Notes

* Returns plain values whenever possible.
* Gracefully handles multi-value parameters.
* Provides an optional default.

---

### Next Step

Utility 75: Replace entire query string on a URL (preserve path + scheme).
