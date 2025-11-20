## Utility 34: Remove HTML Tags

### What It Does

Removes all HTML tags from a string, leaving only plain text.

### Code Example

```python
import re

def remove_html_tags(text):
    return re.sub(r'<[^>]*>', '', text)

sample = "<h1>Hello</h1> <p>World</p>"
print(remove_html_tags(sample))
# Hello World
```

### Notes

* Useful for cleaning scraped data or sanitizing input.
