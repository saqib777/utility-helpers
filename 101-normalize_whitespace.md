
---

### 📄 `utility_101_normalize_whitespace.md`

```md
## Utility 101: Normalize Whitespace in a String

This utility removes extra spaces and normalizes
multiple spaces into a single space.

### Use cases
- Cleaning UI text
- Normalizing API responses
- Reliable string comparisons

### Code

```python
def normalize_whitespace(text):
    """
    Normalizes whitespace by trimming and collapsing spaces.
    """
    if not isinstance(text, str):
        return text

    return " ".join(text.split())
