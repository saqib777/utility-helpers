## Utility 14: Extract Words

### What It Does

This helper extracts all alphabetic words from a given string. It removes numbers, punctuation, and symbols, returning only clean, readable words. This is especially useful for text preprocessing, NLP tasks, or when preparing content for analysis.

Example:

* Input: "Python 3.10 is awesome, fast, and powerful!"
* Output: ["Python", "is", "awesome", "fast", "and", "powerful"]

---

### Explanation

Real-world text often contains punctuation, digits, mixed symbols, or formatting noise. Extracting only the words makes it easier to process the text for:

* Word frequency analysis
* Sentiment analysis
* Keyword extraction
* Document cleaning

We’ll use:

1. Regular expressions
2. `.isalpha()` filtering
3. Simple tokenization techniques

---

### Code Examples

#### Method 1: Using Regular Expressions

```python
import re

def extract_words(text):
    """
    Extract alphabetic words from text.
    Returns a list of clean words.
    """
    return re.findall(r"[A-Za-z]+", text)

# Example
print(extract_words("Python 3.10 is awesome, fast, and powerful!"))
# Output: ['Python', 'is', 'awesome', 'fast', 'and', 'powerful']
```

This is the cleanest and most reliable approach.

---

#### Method 2: Lowercase Normalized Words

```python
import re

def extract_words_lower(text):
    """
    Extract words and convert them to lowercase.
    Useful for word frequency calculations.
    """
    return [word.lower() for word in re.findall(r"[A-Za-z]+", text)]

# Example
print(extract_words_lower("Hello WORLD 2025!"))
# Output: ['hello', 'world']
```

This helps when matching or counting words consistently.

---

#### Method 3: Using Split and isalpha

```python
def extract_words_manual(text):
    """
    Extract alphabetic words using split and isalpha().
    Good for simple text.
    """
    return [word for word in text.split() if word.isalpha()]

# Example
print(extract_words_manual("Clean code 101 is important"))
# Output: ['Clean', 'code', 'is', 'important']
```

Works well on clean text but not ideal for punctuation-heavy input.

---

### Real-Life Use Case

Cleaning text before building a word frequency model or performing sentiment analysis:

```python
def preprocess_for_analysis(text):
    words = extract_words_lower(text)
    return [w for w in words if len(w) > 2]  # remove very short words

print(preprocess_for_analysis("AI in 2025 is the future of tech!"))
# Output: ['future', 'tech']
```

This type of preprocessing is essential in NLP pipelines.

---

### Summary

| Method            | Technique         | Pros                | Best For              |
| ----------------- | ----------------- | ------------------- | --------------------- |
| Regex `[A-Za-z]+` | Pattern matching  | Accurate, clean     | Most real-world text  |
| Lowercase words   | Regex + normalize | Great for analytics | Word frequency models |
| isalpha() split   | Manual filtering  | Simple logic        | Controlled input      |

---

### Next Step

Next, we can create Utility 15: extract_sentences(text), which extracts individual sentences from a block of text for analysis or processing.
