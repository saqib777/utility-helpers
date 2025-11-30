## Utility 64: Remove Null Values (Deep Clean)

### What It Does

Removes all `None` or `null` values from a nested JSON/dict. This is useful for cleaning API payloads, storage objects, and preprocessing.

### Code Example

```python
def remove_nulls(data):
    if isinstance(data, dict):
        cleaned = {}
        for k, v in data.items():
            if v is None:
                continue
            cleaned_value = remove_nulls(v)
            if cleaned_value is not None:
                cleaned[k] = cleaned_value
        return cleaned

    if isinstance(data, list):
        result = []
        for item in data:
            cleaned_item = remove_nulls(item)
            if cleaned_item is not None:
                result.append(cleaned_item)
        return result

    # Primitive value
    return None if data is None else data

sample = {
    "user": {
        "name": "Saqib",
        "age": None,
        "meta": {"city": None, "country": "India"}
    },
    "logs": [None, {"status": None, "id": 1}]
}

print(remove_nulls(sample))
```

---

### Notes

* Removes `None` deeply inside dicts and lists.
* Preserves structure while removing empty nodes.

---

### Next Step

Utility 65: Freeze JSON (make a hashable, immutable version).
