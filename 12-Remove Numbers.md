## Utility 12: Remove Numbers

###  What It Does

This helper removes numeric digits from a given string. It’s especially useful when cleaning text data before analysis, ensuring that numbers (like years, IDs, or phone numbers) don’t interfere with word-based computations.

Example:

* Input: `"Python 3 is awesome in 2025!"`
* Output: `"Python  is awesome in !"`

---

###  Explanation

Numbers often appear in text where they’re not needed for analysis — like product codes, dates, or references. Removing them simplifies data and ensures cleaner results for algorithms or statistics.

We can do this using multiple approaches:

1. Regular expressions (`re.sub`) — the simplest and most flexible way.
2. String translation.
3. List comprehension filtering.

---

### Code Examples

####  Method 1: Using Regular Expressions

```python
import re

def remove_numbers(text):
    """
    Remove all numeric digits from a string using regex.
    """
    return re.sub(r'\d+', '', text)

# Live Example
print(remove_numbers("Python 3 is awesome in 2025!"))
# Output: "Python  is awesome in !"
```

This method is clean and highly efficient for most text-processing tasks.

---

#### Method 2: Using String Translation

```python

def remove_numbers_translate(text):
    """
    Remove digits using str.translate() and maketrans().
    """
    return text.translate(str.maketrans('', '', '0123456789'))

# Live Example
print(remove_numbers_translate("Version 2.0 released in 2024!"))
# Output: "Version . released in !"
```

Great for quick number removal without regex.

---

#### Method 3: Using List Comprehension

```python
def remove_numbers_list(text):
    """
    Remove digits manually using list comprehension.
    """
    return ''.join([char for char in text if not char.isdigit()])

# Live Example
print(remove_numbers_list("Room 101 is ready!"))
# Output: "Room  is ready!"
```

A straightforward way that’s easy to understand and modify.

---

### Real-Life Use Case

You can use this helper to clean raw user input, logs, or scraped data where numbers are irrelevant. For example:

```python
def clean_text_for_analysis(text):
    cleaned = remove_numbers(text)
    return ' '.join(cleaned.split())

print(clean_text_for_analysis("Report 2025: 99% success achieved!"))
# Output: "Report % success achieved!"
```

This makes the text consistent before applying NLP or keyword analysis.

---

### Summary

| Method             | Technique                  | Pros               | Best For             |
| ------------------ | -------------------------- | ------------------ | -------------------- |
| Regex              | `re.sub(r'\d+', '', text)` | Flexible, fast     | Data cleaning        |
| Translate          | `str.translate()`          | No imports, simple | Lightweight scripts  |
| List comprehension | Manual                     | Easy to customize  | Learning and control |

---

### Next Step

Next, we can add **Utility 13: extract_numbers(text)** — the opposite of this helper, which extracts only the digits or numbers from a given string.
