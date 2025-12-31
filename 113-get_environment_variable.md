
---

### 📄 `utility_113_get_environment_variable.md`

```md
## Utility 113: Get Environment Variable with Default

Fetches an environment variable safely.
Returns a default value if not found.

### Use cases
- Environment-based configs
- CI/CD pipelines
- Local vs prod execution

### Code

```python
import os

def get_environment_variable(key, default=None):
    """
    Returns environment variable value or default.
    """
    if not isinstance(key, str):
        return default

    return os.getenv(key, default)
