
---

### 📄 `utility_98_mask_sensitive_string.md`

```md
## Utility 98: Mask Sensitive Part of a String

Masks part of a string to hide sensitive information.
Only the last few characters remain visible.

### Use cases
- Masking account numbers
- Hiding phone numbers
- Logging sensitive data safely

### Code

```python
def mask_sensitive_string(text, visible_chars=4):
    """
    Masks all but the last 'visible_chars' characters of a string.
    """
    if not isinstance(text, str):
        return text

    if len(text) <= visible_chars:
        return "*" * len(text)

    return "*" * (len(text) - visible_chars) + text[-visible_chars:]
