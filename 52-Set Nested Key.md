## Utility 52: Set Nested Key (Create Path If Missing)

### What It Does

Allows you to set a value deep inside a nested dictionary using a dot-notation path. If nested dictionaries do not exist, they are automatically created.

### Code Example

```python
def set_nested(data, path, value):
    parts = path.split('.')
    current = data

    for part in parts[:-1]:
        if part not in current or not isinstance(current[part], dict):
            current[part] = {}
        current = current[part]

    current[parts[-1]] = value
    return data

sample = {}
set_nested(sample, "user.profile.city", "Bangalore")
print(sample)
# {'user': {'profile': {'city': 'Bangalore'}}}
```

### Notes

* Path is created if missing.
* Supports unlimited depth.

---

### Next Step

Utility 53: Delete nested key safely.
