## Utility 28: Generate URL Slug

### What It Does

Creates a clean, readable URL slug from any given text. Slugs are commonly used in blogs, documentation tools, and web apps.

Example:

* Input: "Python Utilities for Text Processing"
* Output: "python-utilities-for-text-processing"

---

### Code Example

```python
import re

def generate_slug(text):
    # Lowercase
    text = text.lower()
    # Replace non‑alphanumeric characters with spaces
    text = re.sub(r"[^a-z0-9]+", " ", text)
    # Remove extra spaces
    text = text.strip()
    # Replace spaces with hyphens
    return text.replace(" ", "-")

print(generate_slug("Python Utilities for Text Processing"))
# Output: python-utilities-for-text-processing
```

---

### Explanation

This utility performs:

1. Lowercasing for consistency.
2. Removal of symbols and punctuation.
3. Normalization of spacing.
4. Conversion of spaces to hyphens.

The result is a clean, SEO‑friendly slug.

---

### Real-Life Use Case

```python
title = "Learn Python in 2025: Complete Roadmap!"
print(generate_slug(title))
# Output: learn-python-in-2025-complete-roadmap
```

Useful for generating blog URLs, file names, or identifiers.

---

### Summary

* Simple text‑to‑slug utility.
* Ensures lowercase, readable, hyphenated output.
* Ideal for websites, blogs, and documentation.

---

### Next Step

Utility 29: Convert snake_case to camelCase.
