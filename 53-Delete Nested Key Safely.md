## Utility 53: Delete Nested Key Safely

### What It Does

Deletes a nested key from a dictionary using dot‑notation. If the path does not exist, it silently does nothing.

### Code Example

```python
def delete_nested(data, path):
    parts = path.split('.')
    current = data

    for part in parts[:-1]:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return data  # Path doesn't exist

    # Delete final key if exists
    if isinstance(current, dict) and parts[-1] in current:
        del current[parts[-1]]

    return data

sample = {"user": {"profile": {"name": "Saqib", "city": "Bangalore"}}}
delete_nested(sample, "user.profile.city")
print(sample)
# {'user': {'profile': {'name': 'Saqib'}}}
```

### Notes

* Safe: no errors on missing paths.
* Works with any nesting depth.

---

### Next Step

Utility 54: Deep clone JSON (full dictionary copy).
