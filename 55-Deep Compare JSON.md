## Utility 55: Deep Compare JSON (Strict Structural + Value Equality)

### What It Does

Compares two JSON/dict objects **deeply** to check if they are exactly the same — including:

* Same keys
* Same value types
* Same nested structure
* Same list order

Useful for testing, API response validation, and config verification.

---

### Code Example

```python
import json

def deep_compare_json(a, b):
    """
    Strict deep comparison of two JSON-like objects.
    Returns True if identical, else False.
    """
    # Convert both to canonical JSON strings
    # Ensures ordering consistency for dictionaries
    a_norm = json.dumps(a, sort_keys=True)
    b_norm = json.dumps(b, sort_keys=True)
    return a_norm == b_norm

# Example
obj1 = {"user": {"name": "Saqib", "skills": ["python", "testing"]}}
obj2 = {"user": {"name": "Saqib", "skills": ["python", "testing"]}}
obj3 = {"user": {"name": "Saqib", "skills": ["testing", "python"]}}

print(deep_compare_json(obj1, obj2))  # True
print(deep_compare_json(obj1, obj3))  # False (list order differs)
```

---

### Explanation

Why JSON string normalization?

* Dictionaries are unordered by default.
* `json.dumps(..., sort_keys=True)` alphabetically sorts keys.
* Both structures are serialized identically when truly equal.

The comparison becomes a clean string equality test.

---

### Notes

* List order matters.
* Supports nested dicts and lists.
* Fails fast if types/structure differ.

---

### Real-Life Use Case

```python
expected_response = {"status": "ok", "details": {"id": 1, "active": True}}
actual_response   = {"details": {"id": 1, "active": True}, "status": "ok"}

print(deep_compare_json(expected_response, actual_response))  # True
```

---

### Summary

* Simple, strict deep equality.
* Perfect for snapshot testing.
* Guarantees identical structure + values.

---
