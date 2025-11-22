## Utility 35: Decode HTML Entities

### What It Does

Decodes HTML entities (like `&amp;`, `&lt;`, `&gt;`, `&quot;`) into their normal readable characters. Useful when cleaning data scraped from webpages or sanitizing text pulled from APIs.

### Code Example

```python
import html

def decode_html_entities(text):
    """
    Convert HTML entities back into normal characters.
    """
    return html.unescape(text)

sample = "Tom &amp; Jerry &lt;Cartoon&gt;"
print(decode_html_entities(sample))
# Output: Tom & Jerry <Cartoon>
```

### Notes

* Uses Python’s built‑in `html` module.
* Handles named, numeric, and hex entities.

---

### Real-Life Use Case

Cleaning text copied from HTML sources:

```python
raw = "Price: 50 &euro;"
print(decode_html_entities(raw))  # Price: 50 €
```

---

### Summary

* Converts encoded HTML characters into readable text.
* Helpful for web scraping, email parsing, and document cleaning.

---

### Next Step

Utility 36: Encode HTML entities.
