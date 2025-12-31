## Utility 95: Extract Letters from a String

This utility extracts only alphabetic characters from a string.
Numbers, spaces, and special characters are ignored.

### Use cases
- Cleaning names or text fields
- Normalizing mixed input
- Preparing data for comparisons

### Code

```python
import re

def extract_letters_from_string(text):
    """
    Extracts and returns only alphabetic characters from a string.
    """
    if not isinstance(text, str):
        return ""

    return "".join(re.findall(r"[a-zA-Z]+", text))
