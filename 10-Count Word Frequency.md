## Utility 10: Count Word Frequency

###  What It Does

This helper counts how many times each word appears in a given text and returns a frequency dictionary. It’s widely used in natural language processing (NLP), text analytics, and search engine algorithms.

Example:

* Input: `"Python is fun and Python is powerful"`
* Output: `{'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}`

---

###  Explanation

Counting word frequency helps understand the importance or repetition of certain words in text. The process involves:

1. Splitting text into words.
2. Normalizing the case (to avoid case-sensitive mismatches).
3. Counting each word's occurrences.

Python’s `collections.Counter` makes this extremely simple and efficient.

---

### Code Examples

#### Method 1: Using `collections.Counter`

```python
from collections import Counter

def count_word_frequency(text):
    """
    Count how many times each word appears in a string.
    Returns a dictionary-like object (Counter).
    """
    words = text.lower().split()
    return Counter(words)

# Live Example
print(count_word_frequency("Python is fun and Python is powerful"))
# Output: Counter({'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1})
```

This method is short, readable, and Pythonic — perfect for most use cases.

---

#### Method 2: Using Regular Expressions

```python
import re
from collections import Counter

def count_word_frequency_regex(text):
    """
    Count word frequency using regex for cleaner word extraction.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

# Live Example
print(count_word_frequency_regex("Hello, world! Hello Python."))
# Output: Counter({'hello': 2, 'world': 1, 'python': 1})
```

This version accurately handles punctuation and mixed symbols.

---

####  Method 3: Sorted Frequency Output

```python
from collections import Counter

def count_word_frequency_sorted(text):
    """
    Count and return words sorted by frequency (descending).
    """
    words = text.lower().split()
    counts = Counter(words)
    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

# Live Example
print(count_word_frequency_sorted("test test python code python python"))
# Output: {'python': 3, 'test': 2, 'code': 1}
```

This is helpful when you need to rank words by importance or popularity.

---

###  Real-Life Use Case

You can use this helper to generate a **word cloud** or analyze text patterns — for instance, finding the most common words in a paragraph or dataset.

```python
def most_common_words(text, top_n=3):
    from collections import Counter
    words = text.lower().split()
    return Counter(words).most_common(top_n)

print(most_common_words("data data data analysis is key to success", top_n=2))
# Output: [('data', 3), ('analysis', 1)]
```

---

### Summary

| Method          | Technique         | Pros                 | Best For           |
| --------------- | ----------------- | -------------------- | ------------------ |
| Counter         | Built-in          | Fast, easy           | Most cases         |
| Regex + Counter | Pattern filtering | Handles punctuation  | Clean text parsing |
| Sorted output   | Frequency ranking | Highlights top words | Data analysis      |

---

### Next Step

Next, we can add **Utility 11: remove_punctuation(text)** — a small helper to strip punctuation marks and clean up raw text for analysis.
