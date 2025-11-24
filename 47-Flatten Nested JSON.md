## Utility 47: Flatten Nested JSON

### What It Does

Converts a deeply nested JSON/dict structure into a flat dictionary using dot‑notation keys.

Example:

```
{"a": {"b": {"c": 1}}}
→ {"a.b.c": 1}
```

---

### Code Example

```python
def flatten_json(data, parent_key="", sep="."):
    items = {}
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_json(v, new_key, sep=sep))
        else:
            items[new_key] = v
    return items

sample = {"user": {"profile": {"name": "Saqib", "city": "Bangalore"}}}
print(flatten_json(sample))
```

---

### Notes

* Supports arbitrarily nested dictionaries.
* Key separator can be changed.
* Useful for logs, analytics, Elasticsearch indexing, etc.

---

### Next Step

Utility 48: Unflatten dot‑notation JSON back into nested structure.
