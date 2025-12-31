
---

### 📄 `utility_96_compare_strings_ignore_case.md`

```md
## Utility 96: Compare Strings Ignoring Case

Compares two strings while ignoring case differences.
Handles non-string inputs safely.

### Use cases
- Case-insensitive assertions
- Comparing user input
- Validation logic in tests

### Code

```python
def compare_strings_ignore_case(str1, str2):
    """
    Returns True if both strings are equal ignoring case.
    """
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False

    return str1.lower() == str2.lower()
