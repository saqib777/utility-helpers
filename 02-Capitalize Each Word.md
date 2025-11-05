Utility 2: Capitalize Each Word

### What It Does

This helper converts every word’s first letter to uppercase and the rest to lowercase. For example, `"hello world"` becomes `"Hello World"`. This is useful in formatting names, titles, or sentences for display.

---

### Explanation

Capitalize means changing only the **first letter** of each word to uppercase and keeping others lowercase. Python offers multiple ways to do this:

1. Using the built-in `.title()` method
2. Using string manipulation (split, capitalize, join)
3. Using list comprehensions for more control

---

###  Code Examples

####  Method 1: Using `.title()`

```python
def capitalize_each_word(text):
    """
    Capitalize the first letter of every word using str.title().
    """
    return text.title()

# Live Example
print(capitalize_each_word("hello world"))  # Output: "Hello World"
```

This is the **quickest** and most direct method.

---

####  Method 2: Using Split and Capitalize

```python
def capitalize_each_word_manual(text):
    """
    Capitalize each word manually using split() and capitalize().
    """
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Live Example
print(capitalize_each_word_manual("python utility helpers"))  # Output: "Python Utility Helpers"
```

This gives more control if you need to add extra logic later.

---

#### Method 3: Handling Edge Cases

```python
def smart_capitalize(text):
    """
    Capitalize each word but ignore small connector words like 'and', 'or', 'the' (except first word).
    Useful for title formatting.
    """
    exceptions = {"and", "or", "the", "of", "in"}
    words = text.split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or word.lower() not in exceptions:
            result.append(word.capitalize())
        else:
            result.append(word.lower())

    return ' '.join(result)

# Live Example
print(smart_capitalize("the lord of the rings"))  # Output: "The Lord of the Rings"
```

This mimics how titles are formatted in English writing.

---

###  Real-Life Use Case

You can use this helper to clean up inconsistent user input:

```python
user_input = "mOhammeD sAqiB"
print(capitalize_each_word_manual(user_input))  # Output: "Mohammed Saqib"
```

Perfect for formatting names or converting messy text into neat, display-friendly output.

---

###  Summary

| Method     | Technique          | Pros             | Best For              |
| ---------- | ------------------ | ---------------- | --------------------- |
| `.title()` | Built-in           | Simple, quick    | Normal text           |
| Manual     | split + capitalize | Customizable     | Complex inputs        |
| Smart      | Ignores connectors | Title formatting | Blog posts, headlines |

---

### Next Step

Next, we can add **remove_whitespace(text)** — a small helper that trims extra spaces, tabs, or newlines from text for clean processing.
