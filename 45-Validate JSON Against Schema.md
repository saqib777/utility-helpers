## Utility 45: Validate JSON Against Schema

### What It Does

Validates any JSON object against a predefined JSON Schema using the `jsonschema` library.

JSON Schema validation helps ensure that incoming data (API payloads, config files, user input, etc.) is structured correctly before your application processes it.

---

### Requirements

Install the `jsonschema` package:

```bash
pip install jsonschema
```

---

### Basic Example

```python
from jsonschema import validate, ValidationError

# Example schema
todo_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "completed": {"type": "boolean"},
        "priority": {"type": "integer"}
    },
    "required": ["title", "completed"],
    "additionalProperties": False
}

# Example JSON object
data = {
    "title": "Buy groceries",
    "completed": False,
    "priority": 1
}

try:
    validate(instance=data, schema=todo_schema)
    print("Valid JSON!")
except ValidationError as e:
    print("Invalid JSON:", e.message)
```

---

### Explanation

* **`type`** defines what kind of structure the value must have.
* **`properties`** defines each allowed field.
* **`required`** lists fields that must be present.
* **`additionalProperties: False`** disallows extra unexpected fields.

If any rule is violated, `ValidationError` is raised.

---

### Real-Life Use Case

Validate incoming API payloads:

```python
def validate_user(data):
    schema = {
        "type": "object",
        "properties": {
            "username": {"type": "string", "minLength": 3},
            "email": {"type": "string"},
            "age": {"type": "integer", "minimum": 18}
        },
        "required": ["username", "email"]
    }

    try:
        validate(data, schema)
        return True
    except ValidationError as e:
        return False, e.message
```

---

### Summary

* Ensures JSON structure matches rules.
* Prevents malformed data from entering systems.
* Great for APIs, configuration validation, and automated testing.

---

### Next Step

Utility 46: Pretty-print JSON (indentation + sorting).
