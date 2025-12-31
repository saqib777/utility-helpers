
---

### 📄 `utility_102_reverse_string.md`

```md
## Utility 102: Reverse a String Safely

Reverses a string while safely handling non-string inputs.

### Use cases
- String manipulation logic
- Small algorithm checks
- Utility transformations

### Code

```python
def reverse_string(text):
    """
    Reverses a string safely.
    """
    if not isinstance(text, str):
        return text

    return text[::-1]
