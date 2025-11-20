## Utility 33: Reverse Words Order

### What It Does

Reverses the order of words in a sentence.

### Code Example

```python
def reverse_words_order(text):
    words = text.split()
    return ' '.join(reversed(words))

print(reverse_words_order("Python utilities are helpful"))
# helpful are utilities Python
```
