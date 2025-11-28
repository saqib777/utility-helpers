## Utility 56: Deep Search Key

### What It Does

Searches for a given key anywhere in a nested JSON/dict and returns all its values.

### Code Example

```python
def deep_search_key(data, target_key):
    results = []

    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key:
                results.append(value)
            results.extend(deep_search_key(value, target_key))

    elif isinstance(data, list):
        for item in data:
            results.extend(deep_search_key(item, target_key))

    return results

sample = {
    "user": {"name": "Saqib", "meta": {"name": "Alias"}},
    "logs": [{"name": "event1"}, {"name": "event2"}]
}

print(deep_search_key(sample, "name"))
# ['Saqib', 'Alias', 'event1', 'event2']
```

### Notes

* Searches dictionaries and lists.
* Returns all matches.

---

