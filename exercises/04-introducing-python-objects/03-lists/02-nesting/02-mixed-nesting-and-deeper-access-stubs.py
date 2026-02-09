# Step 2: Mixed nesting and deeper access
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Given `matrix`, flatten it into a single list containing all elements
# in row-major order: [1, 2, 3, 4, 5, 6, 7, 8, 9].
# Store in `flat`.
# Use nested loops (a for loop inside a for loop).

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Your code here:


# --- Stub 2 ---
# Given `matrix`, compute the sum of each row and store the sums as a list.
# Store in `row_sums`.
# Expected: [6, 15, 24]
# Use a loop. You may use the built-in sum() function on each row,
# or sum manually.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Your code here:


# --- Tests ---

# Stub 1 tests
assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9], (
    f"Expected flat to be [1, 2, 3, 4, 5, 6, 7, 8, 9], got {flat!r}. "
    f"Iterate over each row, then over each element in that row, appending to flat."
)
assert isinstance(flat, list), (
    f"Expected flat to be a list, got {type(flat).__name__}."
)
assert len(flat) == 9, (
    f"Expected flat to have 9 elements, got {len(flat)}. "
    f"A 3x3 matrix should flatten to 9 elements."
)

# Stub 2 tests
assert row_sums == [6, 15, 24], (
    f"Expected row_sums to be [6, 15, 24], got {row_sums!r}. "
    f"Sum each row: 1+2+3=6, 4+5+6=15, 7+8+9=24."
)
assert isinstance(row_sums, list), (
    f"Expected row_sums to be a list, got {type(row_sums).__name__}."
)
assert len(row_sums) == 3, (
    f"Expected row_sums to have 3 elements (one per row), got {len(row_sums)}."
)

print("All tests passed!")
