
---

### 📄 `utility_114_write_text_file_safely.md`

```md
## Utility 114: Write Text to a File Safely

Writes text to a file safely.
Creates the file if it does not exist.

### Use cases
- Writing logs
- Saving reports
- Storing test outputs

### Code

```python
def write_text_file_safely(file_path, content, encoding="utf-8"):
    """
    Writes content to a text file safely.
    """
    try:
        with open(file_path, "w", encoding=encoding) as file:
            file.write(str(content))
        return True
    except Exception:
        return False
