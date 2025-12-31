## Utility 110: Check if a File Exists Safely

Checks whether a file exists at the given path without throwing errors.

### Use cases
- Validating test resources
- Pre-checks before file operations
- Defensive automation scripts

### Code

```python
import os

def check_file_exists(file_path):
    """
    Returns True if the file exists, otherwise False.
    """
    if not isinstance(file_path, str):
        return False

    return os.path.isfile(file_path)
