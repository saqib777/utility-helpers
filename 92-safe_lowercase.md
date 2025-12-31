
---

### 📄 `utility_92_safe_lowercase.md`

```md
## Utility 92: Safe Lowercase Conversion

Converts text to lowercase without throwing errors
when the input is not a string.

### Use cases
- Case-insensitive comparisons
- Normalizing test input
- Defensive programming in utilities

### Code

```python
def safe_lowercase(text):
    """
    Converts text to lowercase safely.
    """
    if not isinstance(text, str):
        return text

    return text.lower()
