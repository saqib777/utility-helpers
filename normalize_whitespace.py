Cleans up extra spaces inside a string and converts multiple spaces into a single space.

```
def normalize_whitespace(text):
    """
    Normalizes whitespace by removing extra spaces and trimming the string.
    """
    if not isinstance(text, str):
        return text

    return " ".join(text.split())
```
