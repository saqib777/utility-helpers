## Utility 5: Count Vowels in a String

###  What It Does

This helper counts how many vowels (`a, e, i, o, u`) appear in a given string. For example:

* Input: `"Mohammed Saqib"`
* Output: `6`

This is often used in text analysis, word statistics, or when validating or filtering text data.

---

### 💬 Explanation

Vowels are the letters that produce open sounds in English (`a, e, i, o, u`). To count them, we loop through the text and check how many characters belong to that set. We usually handle both lowercase and uppercase cases.

There are multiple ways to do this:

1. Using a simple loop
2. Using list comprehension
3. Using regular expressions

---

###  Code Examples

####  Method 1: Using a Loop

```python
def count_vowels(text):
    """
    Count the number of vowels in a string using a loop.
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Live Example
print(count_vowels("Mohammed Saqib"))  # Output: 6
```

Simple and clear — easy to understand for beginners.

---

####  Method 2: Using List Comprehension

```python
def count_vowels_comprehension(text):
    """
    Count vowels using list comprehension.
    """
    return sum([1 for char in text.lower() if char in 'aeiou'])

# Live Example
print(count_vowels_comprehension("HELLO WORLD"))  # Output: 3
```

This method is concise and Pythonic.

---

#### Method 3: Using Regular Expressions

```python
import re

def count_vowels_regex(text):
    """
    Count vowels using regex pattern matching.
    """
    return len(re.findall(r'[aeiouAEIOU]', text))

# Live Example
print(count_vowels_regex("Utility Helpers"))  # Output: 5
```

Regex helps when you want to quickly match patterns in large text.

---

###  Real-Life Use Case

This helper is great for analyzing strings — for example, counting vowels in user-generated names or titles:

```python
names = ["Saqib", "Aarav", "Krishna", "Steve"]
for name in names:
    print(f"{name} -> {count_vowels(name)} vowels")
```

Output:

```
Saqib -> 2 vowels
Aarav -> 3 vowels
Krishna -> 2 vowels
Steve -> 2 vowels
```

---

###  Summary

| Method        | Technique        | Pros                 | Best For       |
| ------------- | ---------------- | -------------------- | -------------- |
| Loop          | Manual iteration | Simple, clear        | Beginners      |
| Comprehension | Pythonic         | Compact, readable    | Quick use      |
| Regex         | Pattern search   | Great for large text | Text analytics |

---

### Next Step

Next, we can add **Utility 6: count_words(text)** — a small but practical helper that counts how many words appear in a given string.
