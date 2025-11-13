## Utility 19: Sanitize Text

### What It Does

This helper cleans and normalizes text by applying multiple steps: trimming spaces, lowering case, removing punctuation, and normalizing spacing. It prepares text for consistent processing.

### Code Example

```python
import re

def sanitize_text(text):
    text = text.lower()                     # lowercase
    text = re.sub(r"[^a-z0-9\s]", "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip() # normalize spaces
    return text

print(sanitize_text("  Hello!!! This  is Python, 2025.  "))
# Output: "hello this is python 2025"
```

### Summary

* Ideal for NLP preprocessing.
* Ensures consistent formatting for further analysis.

---

### Next Step

Utility 20: Extract emails from text.
