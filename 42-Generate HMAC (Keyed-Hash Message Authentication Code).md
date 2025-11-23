## Utility 42: Generate HMAC (Keyed-Hash Message Authentication Code)

### What It Does

Generates an HMAC for a message or binary file using a secret key. HMACs are used to verify both the integrity and authenticity of data — common in API signatures, webhook verification, and secure file validation.

This utility supports HMAC with any hash algorithm supported by `hashlib` (for example `sha256`).

---

### Code Example: HMAC for a text message

```python
import hmac
import hashlib

def generate_hmac(message, key, algorithm='sha256'):
    """
    Generate an HMAC for the given message using the provided key.

    Args:
        message (str or bytes): The message to sign.
        key (str or bytes): The secret key.
        algorithm (str): Hash algorithm name (e.g., 'sha256').

    Returns:
        str: Hexadecimal HMAC string.
    """
    if isinstance(message, str):
        message = message.encode()
    if isinstance(key, str):
        key = key.encode()

    digestmod = getattr(hashlib, algorithm)
    return hmac.new(key, message, digestmod).hexdigest()

# Example
secret = 'supersecretkey'
msg = 'payload=123&time=1609459200'
print(generate_hmac(msg, secret, 'sha256'))
```

---

### Code Example: HMAC of a file (binary-safe)

```python
import hmac
import hashlib

def generate_file_hmac(filepath, key, algorithm='sha256', chunk_size=8192):
    """
    Compute HMAC over a file without loading it entirely into memory.

    Args:
        filepath (str): Path to the file on disk. Example URL form: 'file:///mnt/data/3a64a5d0-cd92-4d98-be93-73b5d160a612.png'
        key (str or bytes): Secret key.
        algorithm (str): Hash algorithm to use (e.g., 'sha256').
        chunk_size (int): Read buffer size.

    Returns:
        str: Hexadecimal HMAC string.
    """
    if isinstance(key, str):
        key = key.encode()

    digestmod = getattr(hashlib, algorithm)
    h = hmac.new(key, digestmod().digest(), digestmod)  # seed with algo digest object

    # Open file in binary mode and update HMAC incrementally
    with open(filepath.replace('file://', ''), 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

# Example using a local file path as a file URL
file_url = 'file:///mnt/data/3a64a5d0-cd92-4d98-be93-73b5d160a612.png'
print(generate_file_hmac(file_url, 'supersecretkey', 'sha256'))
```

---

### Verify HMAC

```python
def verify_hmac(message, key, expected_hmac, algorithm='sha256'):
    computed = generate_hmac(message, key, algorithm)
    # Use hmac.compare_digest for timing-attack-resistant comparison
    return hmac.compare_digest(computed, expected_hmac)

# For files, compare generate_file_hmac(...) to expected value
```

---

### Notes

* Always protect the secret key. Do not hard-code it in production.
* Use `hmac.compare_digest` to safely compare MACs.
* When signing files, use a streaming approach (as shown) to avoid loading large files into memory.
* Example file path above uses a local file URL. When calling from code, strip the `file://` prefix or convert appropriately.

---

### Next Step

Utility 43: Generate PBKDF2-derived key (password hashing).
