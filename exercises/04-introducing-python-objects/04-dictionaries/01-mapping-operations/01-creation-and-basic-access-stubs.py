# Step 1: Creation and basic access — Stubs
# Dictionaries: building dicts from other data using loops

# --- Stub 1 ---
# Given two lists of equal length, create a dict mapping each key to its
# corresponding value (by index). Use a loop — do not use dict(zip(...)) or
# a comprehension. Store the result in `result`.

keys = ["a", "b", "c"]
values = [1, 2, 3]

# Write your code here:
result = None


# --- Stub 2 ---
# Given a string `text`, create a dict where each unique character maps to
# the number of times it appears in the string. Use a loop.
# Store the result in `char_counts`.

text = "hello"

# Write your code here:
char_counts = None


# --- Tests ---

# Tests for Stub 1
assert isinstance(result, dict), \
    f"Expected result to be a dict, got {type(result).__name__}"
assert result == {"a": 1, "b": 2, "c": 3}, \
    f"Expected {{'a': 1, 'b': 2, 'c': 3}}, got {result}"
assert len(result) == 3, \
    f"Expected 3 key-value pairs, got {len(result)}"

# Tests for Stub 2
assert isinstance(char_counts, dict), \
    f"Expected char_counts to be a dict, got {type(char_counts).__name__}"
assert char_counts == {"h": 1, "e": 1, "l": 2, "o": 1}, \
    f"Expected {{'h': 1, 'e': 1, 'l': 2, 'o': 1}}, got {char_counts}"
assert char_counts["l"] == 2, \
    f"Expected 'l' to have count 2, got {char_counts.get('l', 'key missing')}"
assert len(char_counts) == 4, \
    f"Expected 4 unique characters, got {len(char_counts)}"

print("All tests passed!")
