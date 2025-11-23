## Utility 41: Verify Hash

### What It Does

Checks whether a given plaintext string matches a known hash. This is essential for password verification, integrity checks, and validating signatures.

It supports:

* SHA-256
* SHA-1
* MD5

---

### Code Example (General Verifier)

```python
import hashlib

def verify_hash(text, expected_hash, method="sha256"):
    """
    Verify a plaintext string against an expected hash.
    method: "sha256", "sha1", or "md5"
    """
    methods = {
        "sha256": hashlib.sha256,
        "sha1": hashlib.sha1,
        "md5": hashlib.md5
    }

    if method not in methods:
        raise ValueError("Unsupported hash method")

    computed = methods[method](text.encode()).hexdigest()
    return computed == expected_hash

# Example
original = "hello"
hashed = hashlib.sha256(original.encode()).hexdigest()
print(verify_hash("hello", hashed, method="sha256"))  # True
print(verify_hash("world", hashed, method="sha256"))  # False
```

---

### Explanation

This function:

1. Takes input plaintext.
2. Hashes it using the chosen algorithm.
3. Compares it to the known hash.
4. Returns True if they match.

Useful for authentication, API verification, or consistency checks.

---

### Practical Use Case

```python
stored_hash = "5d41402abc4b2a76b9719d911017c592"  # md5("hello")
print(verify_hash("hello", stored_hash, method="md5"))  # True
```

---

### Summary

* Confirms whether input text matches a stored hash.
* Supports SHA-256, SHA-1, and MD5.
* Ideal for authentication flows.

---

### Next Step

Utility 42: Generate HMAC (keyed hash).
