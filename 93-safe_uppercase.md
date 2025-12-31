
---

### 📄 `utility_93_safe_uppercase.md`

```md
## Utility 93: Safe Uppercase Conversion

This utility converts a string to uppercase
and safely ignores non-string inputs.

### Use cases
- Normalizing headers
- Case-insensitive validations
- Test data standardization

### Code

```python
def safe_uppercase(text):
    """
    Converts text to uppercase safely.
    """
    if not isinstance(text, str):
        return text

    return text.upper()
