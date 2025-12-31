## Utility 100: Check if a String is Blank

This utility checks whether a string is `None`, empty, or contains
only whitespace characters.

### Use cases
- Validating mandatory fields
- Cleaning user input
- Preventing false positives in tests

### Code

```python
def is_blank_string(value):
    """
    Returns True if the value is None, empty, or only whitespace.
    """
    if value is None:
        return True

    if not isinstance(value, str):
        return False

    return value.strip() == ""
