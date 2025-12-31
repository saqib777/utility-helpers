
---

### 📄 `utility_116_extract_value_from_json.md`

```md
## Utility 116: Extract Value from JSON Safely

Safely extracts a value from a dictionary-based JSON response.
Returns None if the key does not exist.

### Use cases
- API response parsing
- Defensive JSON handling
- Avoiding KeyError in tests

### Code

```python
def extract_value_from_json(json_data, key):
    """
    Extracts value from JSON dictionary safely.
    """
    if not isinstance(json_data, dict):
        return None

    return json_data.get(key)
