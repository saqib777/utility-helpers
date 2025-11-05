## 🧰 Utility 3: Remove Whitespace

### 🧠 What It Does

This helper cleans up unnecessary whitespace (spaces, tabs, or newlines) from text. For example:

* Input: `"   Hello   World   "`
* Output: `"Hello World"`

It’s very useful when processing user input, reading data from files, or cleaning text for APIs or databases.

---

### 💬 Explanation

Whitespace can appear in different forms — spaces, tabs (`\t`), or newlines (`\n`). Inconsistent spacing can cause validation errors or make data look messy. Python offers several ways to handle it:

1. Using `.strip()` to remove leading and trailing spaces
2. Using `.split()` and `' '.join()` to remove extra spaces between words
3. Using regex (`re.sub`) for complete whitespace normalization

---

### 🧑‍💻 Code Examples

#### ✅ Method 1: Using `.strip()`

```python
def remove_whitespace_basic(text):
    """
    Remove leading and trailing whitespace from the text.
    """
    return text.strip()

# Live Example
print(remove_whitespace_basic("   Hello World   "))  # Output: "Hello World"
```

This only trims the edges — good for simple cleanup.

---

#### ✅ Method 2: Using `.split()` and `' '.join()`

```python
def remove_extra_spaces(text):
    """
    Remove extra spaces between words.
    Splits text into words and rejoins them with a single space.
    """
    return ' '.join(text.split())

# Live Example
print(remove_extra_spaces("   Python     Utility   Helpers   "))  # Output: "Python Utility Helpers"
```

This is the most common and effective way to normalize spaces.

---

#### ✅ Method 3: Using Regex (for full control)

```python
import re

def normalize_whitespace(text):
    """
    Replace all types of whitespace (spaces, tabs, newlines) with a single space.
    Useful for cleaning large or formatted text.
    """
    return re.sub(r'\s+', ' ', text).strip()

# Live Example
messy_text = "Hello\tWorld\n\nThis   is\tPython"
print(normalize_whitespace(messy_text))  # Output: "Hello World This is Python"
```

This approach handles any kind of whitespace pattern — ideal for data parsing or log cleaning.

---

### 💡 Real-Life Use Case

You can use this helper when cleaning text input from users or files:

```python
user_input = "   Mohammed    Saqib   \n   "
cleaned = normalize_whitespace(user_input)
print(cleaned)  # Output: "Mohammed Saqib"
```

This ensures consistency when comparing or saving strings.

---

### 🪄 Summary

| Method       | Technique          | Pros                   | Best For            |
| ------------ | ------------------ | ---------------------- | ------------------- |
| `.strip()`   | Built-in           | Simple trimming        | Removing edges only |
| Split & Join | Word-level cleanup | Clean, efficient       | Normal text input   |
| Regex        | Advanced           | Handles all whitespace | Large or messy data |

---

### Next Step

Next, we can create **Utility 4: is_palindrome(text)** — building on the earlier reverse helper to detect words that read the same backward.
