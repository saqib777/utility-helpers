# Utility Helpers

A growing collection of **simple, reusable Python utility functions** designed to make everyday coding cleaner and faster. Each utility is explained in plain English, with real examples, use cases, and beginner-friendly explanations.

---

## Overview

This repository is meant for anyone learning Python or building automation/testing tools. It includes well-documented helper functions across categories like:

* **String Helpers** → text cleanup, formatting, and manipulation.
* **Math Helpers** → number logic, calculations, and small formulas.
* **File Helpers** → reading, writing, and organizing data.

Each helper is intentionally small and readable — built to teach good programming habits while being practical enough to reuse in projects.

---

## Folder Structure

```
utility-helpers/
│
├── string_helpers/
│   ├── reverse_string.py
│   ├── capitalize_words.py
│   ├── remove_whitespace.py
│   ├── is_palindrome.py
│   ├── count_vowels.py
│
├── math_helpers/
│   ├── factorial.py
│   ├── is_prime.py
│
├── file_helpers/
│   ├── read_file.py
│   ├── write_file.py
│
└── README.md
```

---

## Getting Started

Clone the repository:

```bash
git clone https://github.com/yourusername/utility-helpers.git
cd utility-helpers
```

Each helper can be imported directly into your Python scripts.

Example usage:

```python
from string_helpers.reverse_string import reverse_string
print(reverse_string("Hello World"))  # Output: dlroW olleH
```

---

## Included Utilitie

### String Helpers

| Utility                      | Description                           | Example                       |
| ---------------------------- | ------------------------------------- | ----------------------------- |
| `reverse_string(text)`       | Reverses a given string               | `Hello → olleH`               |
| `capitalize_each_word(text)` | Capitalizes first letter of each word | `hello world → Hello World`   |
| `remove_whitespace(text)`    | Cleans up extra spaces/tabs/newlines  | `Hello   World → Hello World` |
| `is_palindrome(text)`        | Checks if text reads same backward    | `madam → True`                |
| `count_vowels(text)`         | Counts number of vowels in a string   | `Saqib → 2`                   |

---

### Math Helpers

| Utility        | Description                      |
| -------------- | -------------------------------- |
| `factorial(n)` | Calculates factorial of a number |
| `is_prime(n)`  | Checks if a number is prime      |

---

### File Helpers

| Utility                      | Description               |
| ---------------------------- | ------------------------- |
| `read_file(filepath)`        | Reads file content safely |
| `write_file(filepath, data)` | Writes data into a file   |

---

## hy This Repo Exists

This project was created to:

* Build a habit of writing **modular, well-documented code**
* Serve as a go-to **learning reference** for Python basics
* Offer a library of **reusable helpers** for testing, scripting, or quick automation

Every file is written with clarity, real examples, and comments that explain *why* things are done a certain way — not just *how*.

---

## Future Additions

* More math and file operations
* Date/time utilities
* Data validation helpers
* JSON, CSV, and logging helpers

---

## Contributing

If you’d like to contribute, feel free to fork the repo and submit a pull request with your own helper! Just make sure to:

* Keep it **simple and readable**
* Add **docstrings and examples**
* Follow the folder naming convention

---

**Created and maintained by [Mohammed Saqib](https://github.com/saqib777)**
*"Keep learning. Keep building small, clean things — they add up."*
