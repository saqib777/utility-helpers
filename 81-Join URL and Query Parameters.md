## Utility 81: Join URL and Query Parameters

### What It Does

Adds or replaces the query string of a URL using a dictionary of parameters.

Useful for:

* Building clean API endpoints
* Adding filters or pagination
* Replacing messy query strings with structured ones

---

### Code Example

```python
from urllib.parse import urlencode, urlparse, urlunparse

def join_url_query(url, params):
    parsed = urlparse(url)
    query = urlencode(params, doseq=True)
    updated = parsed._replace(query=query)
    return urlunparse(updated)

# Example
url = "https://example.com/products"
params = {"page": 3, "sort": "desc"}
print(join_url_query(url, params))
# https://example.com/products?page=3&sort=desc
```

---

### Notes

* Replaces any existing query string.
* Accepts multi-value parameters.

---

### Next Step

Utility 82 will follow automatically.
