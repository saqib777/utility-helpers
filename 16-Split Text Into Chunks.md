## Utility 16: Split Text Into Chunks

### What It Does

This helper splits long text into fixed-size chunks. Useful for previewing long content, preparing data for APIs with size limits, pagination, or breaking text into manageable parts.

Example:

* Input text length: 120 characters
* Chunk size: 25
* Output: a list of strings, each up to 25 characters.

---

### Code Example

```python
def split_text_into_chunks(text, size):
    """
    Split text into fixed-size chunks.
    """
    return [text[i:i+size] for i in range(0, len(text), size)]

sample = "Python utilities make development easier and cleaner."
print(split_text_into_chunks(sample, 10))
```

---

### Advanced Version (Word-Safe)

```python
def split_chunks_wordsafe(text, size):
    """
    Split text into chunks without breaking words.
    """
    words = text.split()
    chunks = []
    current = ""

    for word in words:
        if len(current) + len(word) + 1 <= size:
            current += (" " + word if current else word)
        else:
            chunks.append(current)
            current = word

    if current:
        chunks.append(current)
    return chunks
```

---

### Summary

* Basic version splits strictly by character count.
* Word-safe version avoids splitting inside words.
* Useful for messaging systems, previews, and pagination.

---

### Next Step

Next utility: detect_language(text).
