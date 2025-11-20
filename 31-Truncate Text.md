## Utility 31: Truncate Text

### What It Does

Truncates text to a given maximum length, optionally adding a suffix.

### Code Example

```python
def truncate_text(text, max_length, suffix="..."):
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

print(truncate_text("Python utilities are powerful", 15))
# Python util...
```
