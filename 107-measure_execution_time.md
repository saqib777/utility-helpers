
---

### 📄 `utility_107_measure_execution_time.md`

```md
## Utility 107: Measure Function Execution Time

Measures how long a function takes to execute.
Helps identify slow operations during tests.

### Use cases
- Performance checks
- Debugging slow tests
- Benchmarking utilities

### Code

```python
import time

def measure_execution_time(func, *args, **kwargs):
    """
    Returns execution time and function result.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()

    return result, end_time - start_time
