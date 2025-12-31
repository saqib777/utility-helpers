
---

### 📄 `utility_109_safe_type_cast.md`

```md
## Utility 109: Safe Type Casting

Safely casts a value to a given type.
Returns a default value instead of throwing errors.

### Use cases
- Parsing API responses
- Defensive programming
- Preventing runtime crashes

### Code

```python
def safe_type_cast(value, target_type, default=None):
    """
    Safely casts value to target_type.
    """
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default
