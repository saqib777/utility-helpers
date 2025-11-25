## Utility 50: Deep Merge JSON Objects

### What It Does

Recursively merges two JSON/dict objects. Values from the second object override those from the first, and nested dictionaries are merged instead of replaced.

### Code Example

```python
def deep_merge_json(a, b):
    result = a.copy()
    for key, value in b.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_json(result[key], value)
        else:
            result[key] = value
    return result

obj1 = {"user": {"name": "Saqib", "role": "tester"}, "active": True}
obj2 = {"user": {"role": "admin"}, "active": False, "country": "India"}

print(deep_merge_json(obj1, obj2))
```

### Notes

* Recursively merges nested dictionaries.
* Second object always overrides.

---

### Next Step

Utility 51: Safe get (nested key lookup).
