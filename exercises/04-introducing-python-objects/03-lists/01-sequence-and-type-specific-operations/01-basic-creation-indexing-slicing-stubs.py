# Step 1: Basic list creation, indexing, slicing
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Given `items`, extract the second element (single value) and
# the last two elements (as a list).
# Store them in `second` and `last_two` respectively.

items = [10, 20, 30, 40, 50]

second = ...       # replace ... with your code
last_two = ...     # replace ... with your code

# --- Stub 2 ---
# Given `L`, create a new list that is L repeated 3 times,
# then get its length.
# Store in `repeated` and `rep_len` respectively.

L = [1, 2, 3]

repeated = ...     # replace ... with your code
rep_len = ...      # replace ... with your code

# --- Tests ---

# Stub 1 tests
assert second == 20, (
    f"Expected second to be 20, got {second!r}. "
    f"Remember: list indexing starts at 0, so the second element is at index 1."
)
assert last_two == [40, 50], (
    f"Expected last_two to be [40, 50], got {last_two!r}. "
    f"Hint: use a negative-index slice to grab the last two elements."
)
assert isinstance(last_two, list), (
    f"Expected last_two to be a list, got {type(last_two).__name__}. "
    f"A slice of a list returns a list, not a single element."
)

# Stub 2 tests
assert repeated == [1, 2, 3, 1, 2, 3, 1, 2, 3], (
    f"Expected repeated to be [1, 2, 3, 1, 2, 3, 1, 2, 3], got {repeated!r}. "
    f"Use the * operator to repeat a list."
)
assert rep_len == 9, (
    f"Expected rep_len to be 9, got {rep_len!r}. "
    f"Use len() on the repeated list."
)
assert L == [1, 2, 3], (
    f"Expected L to still be [1, 2, 3], got {L!r}. "
    f"Repetition creates a new list; it should not modify the original."
)

print("All tests passed!")
