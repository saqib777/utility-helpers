## Utility 63: Find Duplicate Keys in JSON

### What It Does

Scans a nested JSON/dict structure and identifies keys that appear more than once, along with their occurrence count.

### Code Example

```python
def find_duplicate_keys(data):
    counts = {}

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                counts[k] = counts.get(k, 0) + 1
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(data)
    return {k: c for k, c in counts.items() if c > 1}

sample = {
    "user": {"name": "Saqib", "meta": {"name": "Alias"}},
    "logs": [{"name": "event1"}, {"name": "event2"}]
}

print(find_duplicate_keys(sample))
# {'name': 4}
```

---

### Notes

* Counts ALL key occurrences across entire JSON.
* Useful for detecting inconsistent schemas.

---

### Next Step

Utility 64: Remove null/None values deeply.
