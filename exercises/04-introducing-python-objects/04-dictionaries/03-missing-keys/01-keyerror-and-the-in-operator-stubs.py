# Step 1: KeyError and the 'in' operator — Stubs
# Dictionaries: safe access and building frequency dicts with 'in'

# --- Stub 1 ---
# Given a dict `d` and a `key`, safely access the key:
#   - If the key exists in d, store its value in `result`.
#   - If the key does not exist, store -1 in `result`.
# Use the `in` operator (not .get() or try/except).

d = {"a": 1, "b": 2, "c": 3}
key = "d"

# Write your code here:
result = None


# --- Stub 2 ---
# Given a list of words, build a frequency dict counting how many times
# each word appears. Use a loop and the `in` operator to check whether
# the key already exists before incrementing. Store in `freq`.

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Write your code here:
freq = None


# --- Tests ---

# Tests for Stub 1
assert result == -1, \
    f"Expected result to be -1 (key 'd' is not in the dict), got {result}"

# Also verify the logic works for a key that IS present
d2 = {"a": 1, "b": 2, "c": 3}
key2 = "b"
if key2 in d2:
    result2 = d2[key2]
else:
    result2 = -1
assert result2 == 2, \
    f"Sanity check: accessing existing key 'b' should give 2, got {result2}"

# Tests for Stub 2
assert isinstance(freq, dict), \
    f"Expected freq to be a dict, got {type(freq).__name__}"
assert freq == {"apple": 3, "banana": 2, "cherry": 1}, \
    f"Expected {{'apple': 3, 'banana': 2, 'cherry': 1}}, got {freq}"
assert freq["apple"] == 3, \
    f"Expected 'apple' to appear 3 times, got {freq.get('apple', 'key missing')}"
assert freq["banana"] == 2, \
    f"Expected 'banana' to appear 2 times, got {freq.get('banana', 'key missing')}"
assert freq["cherry"] == 1, \
    f"Expected 'cherry' to appear 1 time, got {freq.get('cherry', 'key missing')}"

print("All tests passed!")
