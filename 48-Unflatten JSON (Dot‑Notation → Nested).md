## Utility 48: Unflatten JSON (Dot‑Notation → Nested)

### What It Does

Takes a flat dictionary with dot‑notation keys and reconstructs the original nested JSON structure.

Example:

```
{"a.b.c": 1}
→ {"a": {"b": {"c": 1}}}
```

---

### Code Example

```python
def unflatten_json(flat, sep="."):
    result = {}
    for key, value in flat.items():
        parts = key.split(sep)
        current = result
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = value
    return result

sample = {"user.profile.name": "Saqib", "user.profile.city": "Bangalore"}
print(unflatten_json(sample))
```

---

### Notes

* Works with any depth.
* Reconstructs nested dictionaries accurately.

---

### Next Step

Utility 49: Diff two JSON objects (show additions, removals, and changes).
