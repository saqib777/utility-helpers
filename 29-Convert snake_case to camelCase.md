## Utility 29: Convert snake_case to camelCase

### What It Does

This utility converts text written in `snake_case` into `camelCase`. This is commonly used when switching between Python-style variable naming and JavaScript-style naming.

Example:

* Input: "my_variable_name"
* Output: "myVariableName"

---

### Code Example

```python
def snake_to_camel(text):
    """
    Convert snake_case to camelCase.
    """
    parts = text.split('_')
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

print(snake_to_camel("my_variable_name"))  # myVariableName
print(snake_to_camel("python_utilities"))  # pythonUtilities
```

---

### Explanation

1. Split the string by underscores.
2. Keep the first word lowercase.
3. Capitalize each following word.
4. Join everything back together.

---

### Real-Life Use Case

Useful when converting API keys, JSON keys, or variable names between languages:

```python
python_key = "total_user_count"
js_key = snake_to_camel(python_key)
print(js_key)
# Output: totalUserCount
```

---

### Summary

* Converts snake_case to camelCase.
* Ensures compatibility between naming conventions.
* Helps when working across multiple languages.

---

### Next Step

Utility 30: Convert camelCase to snake_case.
