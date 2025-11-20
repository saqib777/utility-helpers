## Utility 30: Convert camelCase to snake_case

### What It Does

Converts camelCase or PascalCase strings into snake_case.

### Code Example

```python
import re

def camel_to_snake(text):
    text = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', text)
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)
    return text.lower()

print(camel_to_snake("totalUserCount"))
# total_user_count
```
