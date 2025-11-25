## Utility 54: Deep Clone JSON

### What It Does

Creates a **full, independent copy** of a JSON/dict object. Changes to the clone do not affect the original.

### Code Example

```python
import copy

def deep_clone_json(data):
    return copy.deepcopy(data)

sample = {"user": {"profile": {"name": "Saqib", "skills": ["python", "testing"]}}}
cloned = deep_clone_json(sample)

cloned["user"]["profile"]["name"] = "Changed"
print(sample["user"]["profile"]["name"])  # Saqib
```

### Notes

* Uses Python’s `deepcopy` for full isolation.
* Works with lists, dicts, and nested structures.

---

### Next Step

Utility 55: Deep compare JSON (strict equivalence check).
