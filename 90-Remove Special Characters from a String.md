## Utility 90: Remove Special Characters from a String

This utility helps clean strings by removing special characters.
It keeps only alphabets, numbers, and spaces, which is useful for
test data cleanup, validations, and comparisons.

### Use cases
- Cleaning user input before validation
- Normalizing data for assertions
- Preparing text for comparisons

### Code

```python
import re

def remove_special_characters(text):
    """
    Removes special characters from a string.
    Keeps letters, numbers, and spaces.
    """
    if not isinstance(text, str):
        return text

    return re.sub(r"[^a-zA-Z0-9 ]", "", text)
