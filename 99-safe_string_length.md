
---

### 📄 `utility_99_safe_string_length.md`

```md
## Utility 99: Safe String Length

Returns the length of a string safely.
Non-string inputs return zero instead of throwing errors.

### Use cases
- Defensive checks
- Validating input length
- Avoiding runtime exceptions

### Code

```python
def safe_string_length(text):
    """
    Returns length of string safely.
    """
    if not isinstance(text, str):
        return 0

    return len(text)
