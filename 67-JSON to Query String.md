## Utility 67: JSON to Query String

### What It Does

Converts a flat JSON/dict into a URL query-string format.

Example:

```
{"name":"Saqib", "city":"Bangalore"}
→ "name=Saqib&city=Bangalore"
```

### Code Example

```python
from urllib.parse import urlencode

def json_to_querystring(data):
    return urlencode(data)

sample = {"name": "Saqib", "role": "tester"}
print(json_to_querystring(sample))
```

### Notes

* Only supports flat dictionaries.
