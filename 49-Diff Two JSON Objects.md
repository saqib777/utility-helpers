## Utility 49: Diff Two JSON Objects

### What It Does

Compares two JSON/dict objects and reports:

* Added keys
* Removed keys
* Modified values
* Unchanged values

Useful for config comparison, API response validation, and debugging.

---

### Code Example

```python
def json_diff(a, b, parent_key=""):
    diffs = {"added": {}, "removed": {}, "modified": {}, "same": {}}

    a_keys = set(a.keys())
    b_keys = set(b.keys())

    for key in a_keys - b_keys:
        diffs["removed"][key] = a[key]

    for key in b_keys - a_keys:
        diffs["added"][key] = b[key]

    for key in a_keys & b_keys:
        if isinstance(a[key], dict) and isinstance(b[key], dict):
            nested = json_diff(a[key], b[key], key)
            for k in diffs:
                diffs[k].update({f"{key}.{sub}": val for sub, val in nested[k].items()})
        elif a[key] != b[key]:
            diffs["modified"][key] = {"from": a[key], "to": b[key]}
        else:
            diffs["same"][key] = a[key]

    return diffs

# Example
old = {"name": "Saqib", "age": 24, "skills": {"python": "basic"}}
new = {"name": "Saqib", "age": 25, "skills": {"python": "advanced"}, "country": "India"}
print(json_diff(old, new))
```

---

### Notes

* Recursively compares nested dicts.
* Produces structured diff groups.
* Makes debugging changes easier.

---

### Next Step

Utility 50: Deep merge JSON objects (recursive merge).
