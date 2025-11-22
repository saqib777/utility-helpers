## Utility 37: Strip ANSI Escape Codes

### What It Does

Removes ANSI escape codes from text. These codes are commonly used for terminal colors, formatting, and cursor controls. Removing them is useful when storing logs, cleaning console output, or processing colored text.

Example of text with ANSI codes:

```[31mError:[0m Something went wrong!
```

After stripping:

```
Error: Something went wrong!
```

---

### Code Example

```python
import re

def strip_ansi_codes(text):
    """
    Remove ANSI color/formatting escape sequences from text.
    """
    ansi_pattern = r"\x1B\[[0-?]*[ -/]*[@-~]"
    return re.sub(ansi_pattern, "", text)

sample = "\u001b[32mSuccess:\u001b[0m Operation completed."
print(strip_ansi_codes(sample))
# Output: Success: Operation completed.
```

---

### Explanation

ANSI escape codes begin with ESC (`\x1B`) followed by `[` and formatting instructions.
This regex catches:

* Color codes (e.g., `\x1b[31m` for red)
* Reset codes (`\x1b[0m`)
* Cursor control sequences

---

### Real-Life Use Case

Cleaning logs coming from colorized CLI tools:

```python
log = "\u001b[33mWARNING:\u001b[0m Disk almost full"
print(strip_ansi_codes(log))
# WARNING: Disk almost full
```

---

### Summary

* Removes terminal formatting characters.
* Useful for logs, exports, and debugging.

---

### Next Step

Utility 38: Generate secure random string.
