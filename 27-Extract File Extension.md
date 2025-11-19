## Utility 27: Extract File Extension

### What It Does

Extracts the file extension from a filename or URL. Useful when determining file types or validating allowed uploads.

### Code Example

```python
import os

def extract_extension(path):
    """
    Return the file extension without the dot.
    """
    return os.path.splitext(path)[1].lstrip('.')

print(extract_extension("report.pdf"))             # pdf
print(extract_extension("https://example.com/a/b/data.csv"))  # csv
```

### Notes

* Uses Python’s standard `os.path` library.
* Works with normal file paths and URLs.

---

### Next Step

Ready for the next utilities when you are.
