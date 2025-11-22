## Utility 40: Hash Text (SHA / MD5)

### What It Does

Generates cryptographic hash values for any given string. Hashing is essential for storing passwords, verifying file integrity, generating fingerprints, and securing data.

This utility supports:

* SHA-256
* SHA-1
* MD5

---

### Code Example (SHA-256)

```python
import hashlib

def hash_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

print(hash_sha256("hello"))
# Example: '2cf24dba5f...'
```

---

### SHA-1

```python
def hash_sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

print(hash_sha1("hello"))
```

---

### MD5

```python
def hash_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

print(hash_md5("hello"))
```

---

### Explanation

* Uses Python’s `hashlib` module.
* All outputs are hex strings.
* SHA-256 is the recommended algorithm for security.
* MD5 and SHA-1 are fast but not secure for critical systems.

---

### Real-Life Use Case

```python
payload = "user:1234"
fingerprint = hash_sha256(payload)
print(fingerprint)
```

Useful for API signatures and verification.

---

### Summary

* SHA-256: Secure, modern.
* SHA-1: Legacy support.
* MD5: Non-secure but useful for checksums.

---

### Next Step

Utility 41: Verify hash (compare plaintext with expected hash).
