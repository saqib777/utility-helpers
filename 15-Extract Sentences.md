## Utility 15: Extract Sentences

### What It Does

This helper extracts individual sentences from a block of text. It splits text based on punctuation like periods, question marks, and exclamation marks.

Example:

* Input: "Python is great. It is easy to learn! Do you agree?"
* Output: ["Python is great", "It is easy to learn", "Do you agree"]

---

### Code Example

```python
import re

def extract_sentences(text):
    pattern = r"[^.!?]+"
    sentences = re.findall(pattern, text)
    cleaned = [s.strip() for s in sentences if s.strip()]
    return cleaned

print(extract_sentences("Python is great. It is easy to learn! Do you agree?"))
```

---

### Summary

* Uses regex to capture sentence blocks.
* Removes extra spaces.
* Useful for NLP, summarization, and text analysis.

---

### Next Step

Next utility: split_text_into_chunks(text, size).
