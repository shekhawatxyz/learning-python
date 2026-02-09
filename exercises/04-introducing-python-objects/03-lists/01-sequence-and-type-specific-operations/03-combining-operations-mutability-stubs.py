# Step 3: Combining operations, the mutability factor
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Given `data`, remove duplicates (use a simple loop approach — no sets)
# and sort the result.
# Store in `unique_sorted`.
# Expected: [1, 2, 3, 5]
#
# Approach: build a new list, adding only elements not already in it,
# then sort.

data = [3, 5, 3, 1, 5, 2, 1]

# Your code here:


# --- Stub 2 ---
# Given `a` and `b`, merge them into a single sorted list.
# Store in `merged`.
# Expected: [1, 2, 3, 4, 5, 6]
#
# You can use concatenation and sorted(), or build it manually.
# Important: do NOT modify `a` or `b` themselves.

a = [1, 3, 5]
b = [2, 4, 6]

# Your code here:


# --- Tests ---

# Stub 1 tests
assert unique_sorted == [1, 2, 3, 5], (
    f"Expected unique_sorted to be [1, 2, 3, 5], got {unique_sorted!r}. "
    f"Make sure you remove all duplicates and sort the result."
)
assert data == [3, 5, 3, 1, 5, 2, 1], (
    f"Expected data to be unchanged at [3, 5, 3, 1, 5, 2, 1], got {data!r}. "
    f"Build a new list rather than modifying data in place."
)

# Stub 2 tests
assert merged == [1, 2, 3, 4, 5, 6], (
    f"Expected merged to be [1, 2, 3, 4, 5, 6], got {merged!r}. "
    f"Concatenate the two lists and sort the result."
)
assert a == [1, 3, 5], (
    f"Expected a to be unchanged at [1, 3, 5], got {a!r}. "
    f"Do not modify the original lists; create a new one."
)
assert b == [2, 4, 6], (
    f"Expected b to be unchanged at [2, 4, 6], got {b!r}. "
    f"Do not modify the original lists; create a new one."
)

print("All tests passed!")
