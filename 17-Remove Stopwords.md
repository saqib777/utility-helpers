## Utility 17: Remove Stopwords

### What It Does

This helper removes common stopwords (like "the", "and", "is") from text. Stopwords are usually removed during NLP preprocessing to keep only meaningful words.

### Code Example

```python
STOPWORDS = {
    'the','and','is','in','on','at','a','an','to','for','of'
}

def remove_stopwords(text):
    words = text.split()
    return ' '.join([w for w in words if w.lower() not in STOPWORDS])

print(remove_stopwords("Python is great and useful in automation"))
```

### Summary

* Removes non-essential words.
* Helps in keyword extraction and NLP pipelines.

---

### Next Step

Utility 18: Generate word count statistics.
