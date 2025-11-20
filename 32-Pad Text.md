## Utility 32: Pad Text

### What It Does

Adds padding characters to the left, right, or both sides of a string until it reaches a desired length.

### Code Example

```python
def pad_left(text, length, char=' '):
    return text.rjust(length, char)

def pad_right(text, length, char=' '):
    return text.ljust(length, char)

def pad_center(text, length, char=' '):
    return text.center(length, char)

print(pad_left("42", 5, '0'))   # 00042
print(pad_right("hi", 6, '-'))  # hi----
print(pad_center("ok", 6, '*')) # **ok**
```
