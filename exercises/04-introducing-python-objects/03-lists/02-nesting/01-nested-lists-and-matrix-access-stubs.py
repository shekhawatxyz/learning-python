# Step 1: Nested lists and matrix access
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Create a 3x3 matrix (list of 3 lists, each with 3 ints) where each
# element is (row * 3 + col + 1). This should produce:
#   [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Store in `matrix`.
# Then extract the middle row (index 1) and store in `middle_row`.
#
# You can build the matrix manually or with loops — your choice.

# Your code here:


# --- Stub 2 ---
# Given `matrix`, extract the second column (index 1) as a list: [2, 5, 8].
# Store in `column`.
# Use a loop or manual indexing — no comprehensions required yet.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Your code here:


# --- Tests ---

# Stub 1 tests
assert matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]], (
    f"Expected matrix to be [[1, 2, 3], [4, 5, 6], [7, 8, 9]], got {matrix!r}. "
    f"Each element should be (row * 3 + col + 1) with row and col starting at 0."
)
assert middle_row == [4, 5, 6], (
    f"Expected middle_row to be [4, 5, 6], got {middle_row!r}. "
    f"The middle row is at index 1."
)

# Stub 2 tests
assert column == [2, 5, 8], (
    f"Expected column to be [2, 5, 8], got {column!r}. "
    f"Extract element at index 1 from each row."
)
assert isinstance(column, list), (
    f"Expected column to be a list, got {type(column).__name__}."
)

print("All tests passed!")
