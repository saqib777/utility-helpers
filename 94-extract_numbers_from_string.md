
---

### 📄 `utility_94_extract_numbers_from_string.md`

```md
## Utility 94: Extract Numbers from a String

Extracts all numeric characters from a given string
and returns them as a single string.

### Use cases
- Extracting IDs from mixed text
- Parsing phone numbers or codes
- Cleaning numeric input

### Code

```python
import re

def extract_numbers_from_string(text):
    """
    Extracts and returns only numbers from a string.
    """
    if not isinstance(text, str):
        return ""

    return "".join(re.findall(r"\d+", text))
