
---

### 📄 `utility_111_create_directory_if_missing.md`

```md
## Utility 111: Create Directory if Missing

Creates a directory only if it does not already exist.
Avoids unnecessary errors during setup.

### Use cases
- Test artifact storage
- Log directories
- Report generation folders

### Code

```python
import os

def create_directory_if_missing(directory_path):
    """
    Creates directory if it does not exist.
    """
    if not isinstance(directory_path, str):
        return False

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    return True
