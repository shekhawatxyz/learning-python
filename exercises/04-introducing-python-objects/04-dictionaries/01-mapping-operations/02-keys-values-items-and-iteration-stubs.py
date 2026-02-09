# Step 2: keys(), values(), items() and iteration — Stubs
# Dictionaries: merging dicts and inverting key-value pairs using iteration

# --- Stub 1 ---
# Given two dicts d1 and d2, merge them into a new dict called `merged`.
# If a key exists in both dicts, use the value from d2.
# Use a loop over .items() — do not use dict unpacking (**) or
# the | operator or dict.update().

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Write your code here:
merged = None


# --- Stub 2 ---
# Given a dict `d`, create a new dict `inverted` where the keys and values
# are swapped: each value in `d` becomes a key in `inverted`, and each key
# in `d` becomes the corresponding value. Use a loop over .items().

d = {"a": 1, "b": 2, "c": 3}

# Write your code here:
inverted = None


# --- Tests ---

# Tests for Stub 1
assert isinstance(merged, dict), \
    f"Expected merged to be a dict, got {type(merged).__name__}"
assert merged == {"a": 1, "b": 3, "c": 4}, \
    f"Expected {{'a': 1, 'b': 3, 'c': 4}}, got {merged}"
assert merged["b"] == 3, \
    f"Expected key 'b' to have value 3 (from d2), got {merged.get('b', 'key missing')}"
assert len(merged) == 3, \
    f"Expected 3 key-value pairs in merged, got {len(merged)}"

# Tests for Stub 2
assert isinstance(inverted, dict), \
    f"Expected inverted to be a dict, got {type(inverted).__name__}"
assert inverted == {1: "a", 2: "b", 3: "c"}, \
    f"Expected {{1: 'a', 2: 'b', 3: 'c'}}, got {inverted}"
assert inverted[1] == "a", \
    f"Expected inverted[1] to be 'a', got {inverted.get(1, 'key missing')}"
assert len(inverted) == 3, \
    f"Expected 3 key-value pairs in inverted, got {len(inverted)}"

print("All tests passed!")
