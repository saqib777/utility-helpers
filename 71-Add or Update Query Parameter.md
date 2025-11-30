## Utility 71: Add or Update Query Parameter

### What It Does

Adds a new parameter to a query string or updates it if it already exists.

Useful for:

* Modifying URLs dynamically
* Adding filters or pagination
* Updating API request parameters

---

### Code Example

```python
from urllib.parse import parse_qs, urlencode

def add_or_update_query_param(qs, key, value):
    parsed = parse_qs(qs)

    # Update or insert
    parsed[key] = [value]

    return urlencode(parsed, doseq=True)

# Example
qs = "page=1&sort=asc"
print(add_or_update_query_param(qs, "sort", "desc"))
# page=1&sort=desc

print(add_or_update_query_param(qs, "filter", "active"))
# page=1&sort=asc&filter=active
```

---

### Notes

* Automatically normalizes single values into lists for URL encoding.
* Supports overwriting or adding parameters.

---

### Next Step

Utility 72: Remove a query parameter from a query string.
