## Utility 68: Query String to JSON

### What It Does

Parses a URL query string and converts it into a dictionary.

Example:

```
"name=Saqib&city=Bangalore"
→ {"name":"Saqib", "city":"Bangalore"}
```

### Code Example

```python
from urllib.parse import parse_qs

def querystring_to_json(qs):
    parsed = parse_qs(qs)
    # parse_qs returns lists for values, convert to single values when list size is 1
    return {k: v[0] if len(v) == 1 else v for k, v in parsed.items()}

print(querystring_to_json("name=Saqib&city=Bangalore"))
```

### Notes

* Supports multi-value keys.
