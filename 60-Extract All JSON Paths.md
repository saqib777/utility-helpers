## Utility 60: Extract All JSON Paths

### What It Does

Collects **all possible paths** inside a nested JSON/dict structure.
This is useful for:

* Debugging complex JSON
* Understanding large API responses
* Generating auto-documentation
* Creating dynamic forms or validators

Each path represents the location of a value inside the JSON.

Example:

```
{"a": {"b": 1}, "c": [10, 20]}
→ ['a.b', 'c[0]', 'c[1]']
```

---

### Code Example

```python
def extract_all_paths(data, path=""):
    paths = []

    # Handle dictionaries
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            paths.append(new_path)
            paths.extend(extract_all_paths(value, new_path))

    # Handle lists
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{path}[{index}]"
            paths.append(new_path)
            paths.extend(extract_all_paths(item, new_path))

    return paths

sample = {
    "user": {"profile": {"name": "Saqib", "skills": ["python", "testing"]}},
    "active": True
}

print(extract_all_paths(sample))
```

---

### Output Example

```
[
  'user',
  'user.profile',
  'user.profile.name',
  'user.profile.skills',
  'user.profile.skills[0]',
  'user.profile.skills[1]',
  'active'
]
```

---

### Notes

* Handles nested dicts and lists
* Returns every node path in the structure
* Useful for mapping, flattening, search, and documentation

---

### Next Step

Utility 61: Extract all values from JSON (flat list of every value).
