## Utility 44: Generate and Verify JWT (JSON Web Tokens)

### What It Does

Creates and verifies JSON Web Tokens (JWTs) using symmetric (HMAC) or asymmetric (RSA) signing methods. JWTs are commonly used for authentication, API tokens, and session handling.

This utility shows:

* How to generate and verify HS256 (HMAC-SHA256) tokens.
* How to generate and verify RS256 (RSA) tokens using key files.

---

### Requirements

This example uses the `PyJWT` library. Install with:

```bash
pip install PyJWT
```

---

### HS256 (HMAC) Example

```python
import jwt
import time

SECRET = 'your-very-secret-key'

def generate_jwt_hs256(payload, secret=SECRET, expire_in=3600):
    payload = payload.copy()
    payload['exp'] = int(time.time()) + expire_in
    token = jwt.encode(payload, secret, algorithm='HS256')
    return token

def verify_jwt_hs256(token, secret=SECRET):
    try:
        data = jwt.decode(token, secret, algorithms=['HS256'])
        return True, data
    except jwt.ExpiredSignatureError:
        return False, 'Token expired'
    except jwt.InvalidTokenError as e:
        return False, str(e)

# Example usage
payload = {'sub': 'user123', 'role': 'admin'}
token = generate_jwt_hs256(payload)
print('Token:', token)
print('Verify:', verify_jwt_hs256(token))
```

---

### RS256 (RSA) Example — using key files

Note: RSA examples require a private key for signing and a public key for verification. Below shows how to load keys from local files. Replace the example file path with your actual `.pem` key file paths.

In this workspace there is a local file available at:

`file:///mnt/data/3a64a5d0-cd92-4d98-be93-73b5d160a612.png`

For RSA keys you should use `.pem` files. The path above is shown as an example of how to pass a file URL; replace it with a real key file when running these snippets.

```python
import jwt

# Example file URLs (replace with actual .pem files in real use)
private_key_file_url = 'file:///mnt/data/3a64a5d0-cd92-4d98-be93-73b5d160a612.png'  # replace with file:///path/to/private_key.pem
public_key_file_url = 'file:///mnt/data/3a64a5d0-cd92-4d98-be93-73b5d160a612.png'   # replace with file:///path/to/public_key.pem

# Helper to read local file URLs
def read_file_from_url(file_url):
    path = file_url.replace('file://', '')
    with open(path, 'rb') as f:
        return f.read()

# Load keys (in practice these should be PEM text)
# Here we read the provided local file path as an example; replace with your PEM files.
private_key = read_file_from_url(private_key_file_url)
public_key = read_file_from_url(public_key_file_url)

def generate_jwt_rs256(payload, private_key_pem, expire_in=3600):
    payload = payload.copy()
    payload['exp'] = int(time.time()) + expire_in
    token = jwt.encode(payload, private_key_pem, algorithm='RS256')
    return token

def verify_jwt_rs256(token, public_key_pem):
    try:
        data = jwt.decode(token, public_key_pem, algorithms=['RS256'])
        return True, data
    except jwt.ExpiredSignatureError:
        return False, 'Token expired'
    except jwt.InvalidTokenError as e:
        return False, str(e)

# Example usage (will only work with valid PEM key files)
# token = generate_jwt_rs256({'sub': 'user123'}, private_key)
# print('RS256 Token:', token)
# print('Verify RS256:', verify_jwt_rs256(token, public_key))
```

---

### Notes and Best Practices

* HS256 uses a shared secret; keep it secure and rotate it periodically.
* RS256 uses asymmetric keys; keep the private key secret and distribute the public key as needed.
* Always set an expiration (`exp`) claim and consider audience (`aud`) and issuer (`iss`) claims.
* Use `jwt.decode(..., options={'verify_aud': False})` if you need to skip audience verification, but do so deliberately.

---

### Next Step

Utility 45: Validate JSON structure against a schema (using `jsonschema`).
