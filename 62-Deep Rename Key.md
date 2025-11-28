## Utility 62: Deep Rename Key

### What It Does

Renames a key anywhere in a nested JSON/dict. If multiple keys match, all are renamed.

### Code Example

```python
def deep_rename_key(data, old_key, new_key):
    if isinstance(data, dict):
        new_dict = {}
        for k, v in data.items():
            key_name = new_key if k == old_key else k
            new_dict[key_name] = deep_rename_key(v, old_key, new_key)
        return new_dict

    if isinstance(data, list):
        return [deep_rename_key(item, old_key, new_key) for item in data]

    return data

sample = {"user": {"name": "Saqib", "meta": {"name": "Alias"}}}
print(deep_rename_key(sample, "name", "full_name"))
```

---

### Notes

* Renames deeply across dicts and lists.
* Returns transformed structure.

---

### Next Step

Utility 63: Find all duplicate keys in JSON.
