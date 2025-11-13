## Utility 20: Extract Emails

### What It Does

This helper extracts email addresses from any given text. Useful for form processing, data extraction, and validation.

### Code Example

```python
import re

def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}"
    return re.findall(pattern, text)

print(extract_emails("Contact us at support@example.com or admin@mail.io"))
# Output: ['support@example.com', 'admin@mail.io']
```

### Summary

* Uses regex to find valid email patterns.
* Works for simple and typical email formats.
* Good for scraping, validation, and cleaning data.

---

### Next Step

More utilities can be added such as extracting phone numbers, validating URLs, or formatting text.
