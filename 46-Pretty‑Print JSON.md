## Utility 46: Pretty‑Print JSON

### What It Does

Formats JSON objects into readable, indented, optionally sorted text. Useful for logs, debugging, documentation, or displaying API responses.

---

### Code Example

```python
import json

def pretty_print_json(data, indent=4, sort_keys=False):
    return json.dumps(data, indent=indent, sort_keys=sort_keys)

sample = {"name": "Saqib", "age": 25, "skills": ["python", "testing", "automation"]}
print(pretty_print_json(sample, indent=2, sort_keys=True))
```

---

### Notes

* `indent` controls spacing.
* `sort_keys=True` alphabetically orders keys.
* Accepts any JSON‑serializable object.

---

### Next Step

Utility 47: Flatten nested JSON (convert nested dict to dot‑notation).
