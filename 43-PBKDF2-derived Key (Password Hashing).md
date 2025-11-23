## Utility 43: PBKDF2-derived Key (Password Hashing)

### What It Does

Derives a secure key from a password using PBKDF2 (Password-Based Key Derivation Function 2). PBKDF2 is a standard method for hashing passwords: it applies a pseudorandom function (like HMAC-SHA256) many times with a salt to produce a derived key that is safe to store or use as a symmetric key.

This utility shows how to:

* Create a salted PBKDF2 hash for password storage.
* Verify a password against a stored hash.
* Derive a key usable for HMAC or encryption.

---

### Why Use PBKDF2

* Adds a salt to prevent rainbow-table attacks.
* Uses many iterations to slow down brute-force attempts.
* Widely supported and considered secure when parameters are chosen correctly.

---

### Code Examples

#### Generate a PBKDF2 hash (store salt + iterations + derived key)

```python
import os
import hashlib
import binascii

def pbkdf2_hash_password(password, iterations=100_000, dklen=32, algo='sha256'):
    """
    Hash a password using PBKDF2 and return a storage-friendly string.

    Storage format (colon-separated):
        algorithm:iterations:salt_hex:derived_key_hex
    """
    if isinstance(password, str):
        password = password.encode()

    salt = os.urandom(16)  # 128-bit salt
    dk = hashlib.pbkdf2_hmac(algo, password, salt, iterations, dklen)

    return f"{algo}:{iterations}:{binascii.hexlify(salt).decode()}:{binascii.hexlify(dk).decode()}"

# Example
stored = pbkdf2_hash_password('correcthorsebatterystaple')
print(stored)
# Example output: sha256:100000:9f2c3a...:a1b2c3...
```

---

#### Verify a password against the stored PBKDF2 string

```python
import hashlib
import binascii

def pbkdf2_verify_password(password, stored):
    algo, iterations, salt_hex, dk_hex = stored.split(':')
    iterations = int(iterations)
    salt = binascii.unhexlify(salt_hex)
    expected_dk = binascii.unhexlify(dk_hex)

    if isinstance(password, str):
        password = password.encode()

    test_dk = hashlib.pbkdf2_hmac(algo, password, salt, iterations, len(expected_dk))
    # Use compare_digest to avoid timing attacks
    return hashlib.compare_digest(test_dk, expected_dk)

# Example
print(pbkdf2_verify_password('correcthorsebatterystaple', stored))  # True
print(pbkdf2_verify_password('wrongpassword', stored))              # False
```

---

#### Derive a key and use it to HMAC a file (example using a local file URL)

```python
import hmac
import hashlib

# Example local file URL (existing file from earlier in this session)
file_url = 'file:///mnt/data/3a64a5d0-cd92-4d98-be93-73b5d160a612.png'

def derive_key_from_password(password, salt, iterations=100_000, dklen=32, algo='sha256'):
    if isinstance(password, str):
        password = password.encode()
    return hashlib.pbkdf2_hmac(algo, password, salt, iterations, dklen)

def hmac_file_with_derived_key(file_url, key):
    # strip file:// prefix for local path
    path = file_url.replace('file://', '')
    h = hmac.new(key, digestmod=hashlib.sha256)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

# Usage
salt = os.urandom(16)
key = derive_key_from_password('my-secret-password', salt)
print(hmac_file_with_derived_key(file_url, key))
```

---

### Recommended Parameters

* Salt length: 16 bytes (128 bits) or more.
* Iterations: at least 100,000 (increase over time as hardware gets faster).
* dklen: 32 bytes (256-bit) is a good default.
* Algorithm: use `sha256` or stronger.

---

### Security Notes

* Never store plaintext passwords. Store only the algorithm, iterations, salt, and derived key (as shown).
* Use a high iteration count to slow attackers.
* Protect salts and stored hashes; treat them as sensitive data.
* For new systems consider using `scrypt` or `bcrypt` as alternatives depending on your threat model.

---

### Next Step

Utility 44: Generate and verify JSON Web Tokens (JWT) using a secret or asymmetric keys.
