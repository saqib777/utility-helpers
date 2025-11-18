## Utility 21: Extract Phone Numbers

### What It Does

This helper extracts phone numbers from text. It supports common formats such as:

* 1234567890
* 123-456-7890
* (123) 456-7890
* +1 123 456 7890

Useful for cleaning form data, scraping details, and validating user input.

---

### Code Example

```python
import re

def extract_phone_numbers(text):
    """
    Extract phone numbers from text using flexible regex patterns.
    """
    pattern = r"(?:\+?\d{1,3}[\s-]?)?(?:\(\d{3}\)|\d{3})[\s-]?\d{3}[\s-]?\d{4}"
    return re.findall(pattern, text)

print(extract_phone_numbers("Call me at 987-654-3210 or +1 222 333 4444."))
# Output: ['987-654-3210', '+1 222 333 4444']
```

---

### Explanation

The regex is designed to detect:

* Optional country code
* Area code with or without parentheses
* Spacing or hyphens

This makes it robust for most international and domestic phone formats.

---

### Real-Life Use Case

Extract all phone numbers from a paragraph:

```python
text = "Support: (800) 123-4567, Sales: +91 98765 43210"
print(extract_phone_numbers(text))
```

---

### Summary

| Method | Technique     | Pros           | Best For             |
| ------ | ------------- | -------------- | -------------------- |
| Regex  | Pattern-based | Flexible, fast | User input, scraping |

---

### Next Step

Next utility: validate_phone_number(number).
