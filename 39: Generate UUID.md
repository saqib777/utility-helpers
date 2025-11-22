## Utility 39: Generate UUID

### What It Does

Generates universally unique identifiers (UUIDs) using Python’s built-in `uuid` module. UUIDs are used for identifiers in distributed systems, databases, APIs, and anywhere uniqueness must be guaranteed without coordination.

---

### Code Example (UUID4 — Random)

```python
import uuid

def generate_uuid4():
    """
    Generate a random UUID (version 4).
    """
    return str(uuid.uuid4())

print(generate_uuid4())
# Example: 'f47ac10b-58cc-4372-a567-0e02b2c3d479'
```

### Other UUID Types

#### UUID1 — Time + MAC Address

```python
def generate_uuid1():
    return str(uuid.uuid1())
```

Useful when you want time-based ordering.

#### UUID3 — Namespace + Name (MD5)

```python
def generate_uuid3(namespace, name):
    return str(uuid.uuid3(namespace, name))
```

#### UUID5 — Namespace + Name (SHA-1)

```python
def generate_uuid5(namespace, name):
    return str(uuid.uuid5(namespace, name))
```

---

### Real-Life Use Case

Assign unique identifiers in logs or API payloads:

```python
user_id = generate_uuid4()
print(user_id)
```

---

### Summary

* UUID4 is the most commonly used (random, secure).
* Useful for IDs, tokens, database keys, and tracking.

---

### Next Step

Utility 40: Hash text using SHA algorithms.
