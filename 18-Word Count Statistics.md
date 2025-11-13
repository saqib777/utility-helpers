## Utility 18: Word Count Statistics

### What It Does

This helper generates basic text statistics including total words, unique words, average word length, and the most common word.

### Code Example

```python
from collections import Counter
import re

def word_count_stats(text):
    words = re.findall(r"[A-Za-z]+", text.lower())
    total = len(words)
    unique = len(set(words))
    avg_len = sum(len(w) for w in words) / total if total else 0
    common = Counter(words).most_common(1)[0][0] if total else None

    return {
        'total_words': total,
        'unique_words': unique,
        'average_word_length': avg_len,
        'most_common_word': common
    }

print(word_count_stats("Python is fun and Python is powerful"))
```

### Summary

* Provides quick insights about text.
* Useful for analytics, preprocessing, and reports.

---

### Next Step

Utility 19: Sanitize text (clean and normalize).
