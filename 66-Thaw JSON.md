## Utility 66: Thaw JSON (Immutable → Mutable)

### What It Does

Reverses the `freeze_json` transformation and converts:

* `frozenset` → `dict`
* `tuple` → `list`
* Primitives stay unchanged

### Code Example

```python
def thaw_json(data):
    if isinstance(data, frozenset):
        return {k: thaw_json(v) for k, v in data}
    if isinstance(data, tuple):
        return [thaw_json(i) for i in data]
    return data

frozen = frozenset({('a', 1), ('b', frozenset({('c', 2)}))})
print(thaw_json(frozen))
```
