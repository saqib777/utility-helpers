
---

### 📄 `utility_97_is_numeric_string.md`

```md
## Utility 97: Check if a String is Numeric

Checks whether a string contains only numeric characters.

### Use cases
- Validating IDs
- Input validation
- Pre-checks before conversion

### Code

```python
def is_numeric_string(text):
    """
    Returns True if the string contains only numbers.
    """
    if not isinstance(text, str):
        return False

    return text.isdigit()
