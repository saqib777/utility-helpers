##  Utility 4: Check if a String is a Palindrome

###  What It Does

This helper checks whether a given word or sentence reads the same forward and backward. For example:

* Input: `"madam"`
* Output: `True`

Palindromes are common in programming exercises, data validation, and even text analysis. This utility is simple but demonstrates string manipulation and logic.

---
###  Explanation

A **palindrome** is a word, phrase, or number that remains the same when reversed. Examples: `"racecar"`, `"level"`, `"noon"`. When checking, we usually:

1. Reverse the string.
2. Compare it to the original.

For better accuracy, we often ignore spaces, punctuation, and capitalization.

---

###  Code Examples

####  Method 1: Basic Check

```python
def is_palindrome(text):
    """
    Check if a string is a palindrome (case-sensitive).
    """
    return text == text[::-1]

# Live Example
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

This is the simplest version — clean and quick.

---

####  Method 2: Case-Insensitive Check

```python
def is_palindrome_case_insensitive(text):
    """
    Check palindrome ignoring case sensitivity.
    """
    text = text.lower()
    return text == text[::-1]

# Live Example
print(is_palindrome_case_insensitive("Madam"))  # Output: True
```

This version handles mixed-case inputs like `"Madam"` or `"RaceCar"`.

---

####  Method 3: Ignore Spaces and Punctuation

```python
import re

def is_palindrome_cleaned(text):
    """
    Check palindrome by removing all non-alphanumeric characters and ignoring case.
    Useful for sentences or formatted text.
    """
    cleaned = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

# Live Example
print(is_palindrome_cleaned("A man, a plan, a canal: Panama"))  # Output: True
```

This one’s practical for real-world strings where punctuation or spaces exist.

---

###  Real-Life Use Case

You might use this in a **text-based testing utility** or **data validation tool** to detect symmetric strings or patterns. For example:

```python
inputs = ["madam", "No lemon, no melon", "hello"]
for word in inputs:
    print(f"{word} -> {is_palindrome_cleaned(word)}")
```

Output:

```
madam -> True
No lemon, no melon -> True
hello -> False
```

---

###  Summary

| Method           | Technique               | Pros                    | Best For                  |
| ---------------- | ----------------------- | ----------------------- | ------------------------- |
| Basic            | Compare reversed string | Fast, simple            | Single words              |
| Case-insensitive | Lowercase comparison    | Handles capital letters | User input                |
| Cleaned          | Regex filter            | Works for sentences     | Complex or formatted text |

---

### Next Step

Next, we can create **Utility 5: count_vowels(text)** — a small but useful helper that counts how many vowels appear in a given string.
