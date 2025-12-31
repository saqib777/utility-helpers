
---

### 📄 `utility_112_read_text_file_safely.md`

```md
## Utility 112: Read a Text File Safely

Reads the contents of a text file safely.
Returns an empty string if the file cannot be read.

### Use cases
- Reading config files
- Loading test data
- Avoiding runtime crashes

### Code

```python
def read_text_file_safely(file_path, encoding="utf-8"):
    """
    Reads a text file safely and returns its content.
    """
    try:
        with open(file_path, "r", encoding=encoding) as file:
            return file.read()
    except Exception:
        return ""
