## Utility 36: Encode HTML Entities

### What It Does

Encodes special characters in a string into their HTML-safe entity forms. This is important when rendering user-generated content on webpages or storing text safely.

### Code Example

```python
import html

def encode_html_entities(text):
    """
    Convert characters like <, >, &, " into their HTML-safe versions.
    """
    return html.escape(text)

sample = "Tom & Jerry <Cartoon>"
print(encode_html_entities(sample))
# Output: Tom &amp; Jerry &lt;Cartoon&gt;
```

### Notes

* Helps prevent HTML injection.
* Uses Python's built-in `html` library.

---

### Real-Life Use Case

```python
user_input = '<script>alert("Hi")</script>'
safe = encode_html_entities(user_input)
print(safe)
# &lt;script&gt;alert(&quot;Hi&quot;)&lt;/script&gt;
```

This ensures the string is displayed literally and not executed.

---

### Summary

* Encodes HTML-sensitive characters.
* Useful for sanitizing and safely storing content.

---

### Next Step

Utility 37: Strip ANSI escape codes (terminal color codes).
