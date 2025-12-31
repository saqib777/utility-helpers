
---

### 📄 `utility_91_truncate_string.md`

```md
## Utility 91: Truncate a String Safely

This utility trims a string to a given maximum length.
It avoids unexpected errors and keeps the logic explicit.

### Use cases
- Limiting UI text length
- Preparing logs or reports
- Handling long API responses

### Code

```python
def truncate_string(text, max_length):
    """
    Truncates a string to the specified max_length.
    """
    if not isinstance(text, str):
        return text

    if max_length < 0:
        raise ValueError("max_length must be non-negative")

    return text[:max_length]
