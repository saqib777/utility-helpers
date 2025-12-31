
---

### 📄 `utility_103_count_vowels_in_string.md`

```md
## Utility 103: Count Vowels in a String

Counts the number of vowels in a string.
Case-insensitive by default.

### Use cases
- Text analysis
- Validation rules
- Practice utilities used in tests

### Code

```python
def count_vowels_in_string(text):
    """
    Returns the count of vowels in the string.
    """
    if not isinstance(text, str):
        return 0

    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
