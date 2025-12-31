
---

### 📄 `utility_106_generate_uuid.md`

```md
## Utility 106: Generate a UUID

Generates a universally unique identifier (UUID).
Useful when uniqueness matters across systems.

### Use cases
- Correlation IDs
- Unique test records
- Tracking execution runs

### Code

```python
import uuid

def generate_uuid():
    """
    Generates and returns a UUID string.
    """
    return str(uuid.uuid4())
