## Utility 65: Freeze JSON (Immutable + Hashable)

### What It Does

Converts a JSON/dict structure into an immutable, hashable form (tuples, frozensets). Useful for:

* Using JSON objects as dictionary keys
* Caching
* Deduplication tasks

### Code Example

```python
def freeze_json(data):
    if isinstance(data, dict):
        return frozenset((k, freeze_json(v)) for k, v in data.items())
    if isinstance(data, list):
        return tuple(freeze_json(i) for i in data)
    return data

sample = {"a": 1, "b": {"c": 2}}
print(freeze_json(sample))
```
