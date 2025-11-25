## Utility 51: Safe Get (Nested Key Lookup)

### What It Does

Safely retrieves a nested key from a JSON/dict structure without raising errors if a key is missing. Returns a default value instead.

### Code Example

```python
def safe_get(data, path, default=None):
    parts = path.split('.')
    current = data
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        else:
            return default
    return current

sample = {"user": {"profile": {"name": "Saqib", "city": "Bangalore"}}}

print(safe_get(sample, "user.profile.name"))       # Saqib
print(safe_get(sample, "user.profile.age", "N/A"))  # N/A
```

### Notes

* Avoids `KeyError` exceptions.
* Supports dot-notation paths.

---

### Next Step

Utility 52: Set nested key (create path if missing).
