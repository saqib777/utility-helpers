## Utility 23: Extract URLs

### What It Does

This utility extracts all URLs from a given block of text. It supports common patterns including HTTP, HTTPS, and basic domain formats.

Example:

* Input: "Visit [https://example.com](https://example.com) or [http://test.org](http://test.org) for details."
* Output: ["[https://example.com](https://example.com)", "[http://test.org](http://test.org)"]

---

### Code Example

```python
import re

def extract_urls(text):
    """
    Extract all URLs from the text using regex.
    """
    pattern = r"https?://[\w./%-]+"
    return re.findall(pattern, text)

sample = "Docs: https://docs.python.org, site: http://example.com/page"
print(extract_urls(sample))
```

---

### Explanation

The regex captures:

* `http` or `https`
* `://`
* Allowed characters such as letters, digits, dots, slashes, hyphens, and percent-encoded values

This makes the function suitable for most web URL extraction tasks.

---

### Real-Life Use Case

```python
text = "Resources: https://github.com, https://pypi.org/project/regex/"
print(extract_urls(text))
```

---

### Summary

* Simple URL extraction using regex.
* Great for scraping, preprocessing, and link collection.

---

### Next Step

Next utility: validate_url(url).
