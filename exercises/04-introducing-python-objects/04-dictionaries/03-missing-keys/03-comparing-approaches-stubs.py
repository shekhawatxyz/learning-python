# Step 3: Comparing approaches (in, get, try/except) — Stubs
# Dictionaries: implementing safe access and using it on real data

# --- Stub 1 ---
# Write a function `safe_get(d, key, default=None)` that mimics the
# behavior of dict.get(). It should:
#   - Try to return d[key].
#   - If a KeyError is raised, return `default` instead.
# Use a try/except block.

# Write your code here:


# --- Stub 2 ---
# Given a list of person records (dicts), extract each person's email.
# Some records have an "email" key and some do not. For those missing it,
# use "no email" as the default. Use .get() on each record.
# Store the result as a list of email strings in `emails`.

records = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob"},
    {"name": "Charlie", "email": "charlie@example.com"}
]

# Write your code here:
emails = None


# --- Tests ---

# Tests for Stub 1 — safe_get
assert safe_get({"a": 1}, "a") == 1, \
    f"Expected safe_get({{'a': 1}}, 'a') to return 1, got {safe_get({'a': 1}, 'a')}"
assert safe_get({"a": 1}, "b") is None, \
    f"Expected safe_get({{'a': 1}}, 'b') to return None (default), got {safe_get({'a': 1}, 'b')}"
assert safe_get({"a": 1}, "b", 0) == 0, \
    f"Expected safe_get({{'a': 1}}, 'b', 0) to return 0, got {safe_get({'a': 1}, 'b', 0)}"
assert safe_get({"a": 1}, "b", "missing") == "missing", \
    f"Expected safe_get({{'a': 1}}, 'b', 'missing') to return 'missing', got {safe_get({'a': 1}, 'b', 'missing')}"
assert safe_get({}, "x", []) == [], \
    f"Expected safe_get({{}}, 'x', []) to return [], got {safe_get({}, 'x', [])}"

# Tests for Stub 2 — emails
assert isinstance(emails, list), \
    f"Expected emails to be a list, got {type(emails).__name__}"
assert emails == ["alice@example.com", "no email", "charlie@example.com"], \
    f"Expected ['alice@example.com', 'no email', 'charlie@example.com'], got {emails}"
assert len(emails) == 3, \
    f"Expected 3 emails, got {len(emails)}"
assert emails[1] == "no email", \
    f"Expected Bob's email to be 'no email' (missing key), got '{emails[1]}'"

print("All tests passed!")
