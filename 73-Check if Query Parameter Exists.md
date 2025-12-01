## Utility 73: Check if Query Parameter Exists

### What It Does

Checks whether a query string contains a given key.

Useful when conditionally modifying URLs or validating API requests.

---

### Code Example

```python
from urllib.parse import parse_qs

def query_param_exists(qs, key):
    parsed = parse_qs(qs)
    return key in parsed

# Example
qs = "page=1&sort=asc"
print(query_param_exists(qs, "sort"))   # True
print(query_param_exists(qs, "filter")) # False
```

---

### Notes

* Clean boolean response.
* Works for all valid query strings.

---

### Next Step

Utility 74: Get value of a query parameter.
