# Stub 1
# Given any string `word`, get its first character and last character.
# Store them in `first` and `last`.
# Use indexing (not slicing).

word = "elephant"
# Your code here:
first = ...
last = ...


# Stub 2
# Given text = "racecar", check whether the first and last characters
# are the same. Store the boolean result in `same_ends`.

text = "racecar"
# Your code here:
same_ends = ...


# --- Tests ---
# Do not modify below this line.

assert first == "e", \
    f"first should be 'e' for word='elephant', got {first!r}"
assert last == "t", \
    f"last should be 't' for word='elephant', got {last!r}"

assert isinstance(same_ends, bool), \
    f"same_ends should be a bool, got {type(same_ends).__name__}"
assert same_ends is True, \
    f"same_ends should be True for 'racecar' (both 'r'), got {same_ends}"

# Edge case: verify the approach works generally
word = "a"
first = word[0]
last = word[-1]
assert first == last == "a", \
    "Indexing should work for single-character strings too"

print("All tests passed.")
