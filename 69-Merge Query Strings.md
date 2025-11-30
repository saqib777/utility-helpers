## Utility 69: Merge Query Strings

### What It Does

Combines two URL query strings into one. If keys overlap, the second query string overrides the first.

Useful for:

* Merging pagination params
* Adding filters dynamically
* Updating existing URLs safely

---

### Code Example

```python
from urllib.parse import parse_qs, urlencode

def merge_querystrings(qs1, qs2):
    # Parse both query strings
    d1 = parse_qs(qs1)
    d2 = parse_qs(qs2)

    # Merge with override
    merged = {**d1, **d2}

    # Convert parsed lists back to simpler values whenever possible
    normalized = {
        k: v[0] if len(v) == 1 else v
        for k, v in merged.items()
    }

    return urlencode(normalized, doseq=True)

# Example
q1 = "page=1&sort=asc"
q2 = "sort=desc&filter=active"
print(merge_querystrings(q1, q2))
# page=1&sort=desc&filter=active
```

---

### Notes

* Keys in `qs2` override keys from `qs1`.
* Supports multi-value parameters.
* Output is normalized to a clean query string.

---

### Next Step

Utility 70: Normalize query string (sort keys alphabetically).
