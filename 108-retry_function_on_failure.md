
---

### 📄 `utility_108_retry_function_on_failure.md`

```md
## Utility 108: Retry a Function on Failure

Retries a function multiple times if it raises an exception.
Stops early if the function succeeds.

### Use cases
- Handling flaky APIs
- Retrying unstable operations
- Making tests more resilient

### Code

```python
import time

def retry_function_on_failure(func, retries=3, delay=1):
    """
    Retries a function if it raises an exception.
    """
    last_exception = None

    for _ in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            time.sleep(delay)

    raise last_exception
