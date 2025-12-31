## Utility 115: Validate HTTP Status Code

Validates whether an HTTP response status code matches the expected value.

### Use cases
- API test assertions
- Response validation
- Contract testing checks

### Code

```python
def validate_http_status_code(actual_status, expected_status):
    """
    Returns True if actual status matches expected status.
    """
    try:
        return int(actual_status) == int(expected_status)
    except (TypeError, ValueError):
        return False
