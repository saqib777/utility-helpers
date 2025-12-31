
---

### 📄 `utility_104_is_palindrome_string.md`

```md
## Utility 104: Check if a String is a Palindrome

Checks whether a string reads the same forwards and backwards.
Ignores case and surrounding spaces.

### Use cases
- Logical validations
- Interview-style test utilities
- Demonstrating clean checks

### Code

```python
def is_palindrome_string(text):
    """
    Returns True if the string is a palindrome.
    """
    if not isinstance(text, str):
        return False

    cleaned = text.strip().lower()
    return cleaned == cleaned[::-1]
