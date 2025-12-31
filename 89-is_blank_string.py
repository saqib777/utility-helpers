Safely checks whether a string is None, empty, or contains only whitespace.

```
def is_blank_string(value):
    """
    Returns True if the given value is None, empty, or contains only whitespace.
    """
    if value is None:
        return True

    if not isinstance(value, str):
        return False

    return value.strip() == ""
```
