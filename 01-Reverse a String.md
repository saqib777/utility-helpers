## Utility Helpers Repository

---

## 🧰 Utility 1: Reverse a String

### 🧠 What It Does

This helper reverses any given string. For example, `"Saqib"` becomes `"biqaS"`. It’s simple but handy when handling text operations, especially for testing, string validation, or algorithms.

---

### 💬 Explanation

Reversing a string means flipping the order of characters — so `"abc"` becomes `"cba"`. There are several ways to do this in Python:

1. Using slicing (`[::-1]`)
2. Using a loop
3. Using the built-in `reversed()` function

---

### 🧑‍💻 Code Examples

#### ✅ Method 1: Using Slicing

```python
def reverse_string(text):
    """
    Reverse a given string using slicing.

    Args:
        text (str): The input string.

    Returns:
        str: The reversed string.
    """
    return text[::-1]

# Live Example
example = "Hello World"
print(reverse_string(example))  # Output: "dlroW olleH"
```

This is the **most Pythonic** way — short, efficient, and easy to read.

---

#### ✅ Method 2: Using a Loop

```python
def reverse_string_loop(text):
    """
    Reverse a string manually using a loop.
    """
    reversed_text = ''
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# Live Example
print(reverse_string_loop("Saqib"))  # Output: "biqaS"
```

This version helps beginners understand what happens under the hood.

---

#### ✅ Method 3: Using `reversed()` Built-in

```python
def reverse_string_builtin(text):
    """
    Reverse a string using the reversed() built-in function.
    """
    return ''.join(reversed(text))

# Live Example
print(reverse_string_builtin("Utility"))  # Output: "ytilitU"
```

This is readable and efficient for larger strings.

---

### 💡 Real-Life Use Case

You can use this helper to check for **palindromes** (words that read the same backward):

```python
def is_palindrome(word):
    return word == reverse_string(word)

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
```

---

### 🪄 Summary

| Method   | Technique    | Pros                | Best For     |
| -------- | ------------ | ------------------- | ------------ |
| Slicing  | `[::-1]`     | Fast, clean         | Most cases   |
| Loop     | Manual       | Great for learning  | Beginners    |
| Built-in | `reversed()` | Readable, efficient | Long strings |

---

### Next Step

The next helper can be **capitalize_each_word(text)**, which converts `"hello world"` → `"Hello World"`, or something like **remove_whitespace(text)** for cleaning input.

---

**Goal:** Keep each helper well-documented, simple, and easy to reuse across any project.
