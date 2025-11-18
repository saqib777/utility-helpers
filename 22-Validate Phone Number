## Utility 22: Validate Phone Number

### What It Does

This helper validates whether a given string is a properly formatted phone number. It supports common formats like:

* 1234567890
* 123-456-7890
* (123) 456-7890
* +1 123 456 7890

Validation is useful for forms, user inputs, and API data cleaning.

---

### Code Example

```python
import re

def validate_phone_number(number):
    """
    Validate if the given string matches a typical phone number pattern.
    """
    pattern = r"^(\+?\d{1,3}[\s-]?)?(\(\d{3}\)|\d{3})[\s-]?\d{3}[\s-]?\d{4}$"
    return bool(re.match(pattern, number))

print(validate_phone_number("987-654-3210"))        # True
print(validate_phone_number("+1 222 333 4444"))      # True
print(validate_phone_number("12345"))                # False
```

---

### Explanation

The validation checks for:

* Optional country code
* A valid 3-digit area code
* Properly formatted number blocks
* Optional parentheses and separators

---

### Real-Life Use Case

```python
numbers = ["(800) 123-4567", "98765", "123-456-7890"]
valid = [n for n in numbers if validate_phone_number(n)]
print(valid)
# Output: ['(800) 123-4567', '123-456-7890']
```

---

### Summary

* Ensures number structure is valid.
* Works for multiple formats.
* Useful for form validation and preprocessing.

---

### Next Step

Next utility: extract_urls(text).
