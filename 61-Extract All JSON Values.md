## Utility 61: Extract All JSON Values

### What It Does

Returns every value found inside a nested JSON/dict structure, regardless of depth.

### Code Example

```python
def extract_all_values(data):
    values = []

    if isinstance(data, dict):
        for value in data.values():
            values.append(value)
            values.extend(extract_all_values(value))

    elif isinstance(data, list):
        for item in data:
            values.append(item)
            values.extend(extract_all_values(item))

    return values

sample = {"user": {"name": "Saqib", "skills": ["python", "testing"]}, "active": True}
print(extract_all_values(sample))
```

---

### Notes

* Useful for scanning all content in JSON.
* Includes primitives, lists, dicts.

---

### Next Step

Utility 62: Rename a key deeply inside JSON.
