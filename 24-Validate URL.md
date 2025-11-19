## Utility 24: Validate URL

### What It Does

Checks whether a given string is a valid URL using a flexible regular expression.

### Code Example

```python
import re

def validate_url(url):
    pattern = r"^(https?://)[\w.-]+(/[\w./%-]*)?$"
    return bool(re.match(pattern, url))

print(validate_url("https://example.com"))      # True
print(validate_url("http:/wrong.com"))          # False
```

### Notes

* Supports HTTP and HTTPS.
* Checks domain + optional path.

---

### Next Step

Utility 25: Extract domain from URL.
