# Step 3: Nested comprehensions
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Given `matrix`, flatten it into a single list using a single list
# comprehension with nested for clauses.
# Store in `flat`.
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Hint: the outer for iterates over rows, the inner for iterates over
# elements within each row.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = ...  # replace ... with a list comprehension

# --- Stub 2 ---
# Using a list comprehension, generate all (x, y) pairs where
# x is from [1, 2, 3] and y is from [1, 2, 3] and x != y.
# Store in `pairs`.
# Expected: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
#
# Hint: use two for clauses and an if clause. Each element should
# be a tuple (x, y).

pairs = ...  # replace ... with a list comprehension

# --- Tests ---

# Stub 1 tests
assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9], (
    f"Expected flat to be [1, 2, 3, 4, 5, 6, 7, 8, 9], got {flat!r}. "
    f"Use nested for clauses: [elem for row in matrix for elem in row]."
)
assert isinstance(flat, list), (
    f"Expected flat to be a list, got {type(flat).__name__}."
)
assert len(flat) == 9, (
    f"Expected flat to have 9 elements, got {len(flat)}."
)

# Stub 2 tests
assert pairs == [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)], (
    f"Expected pairs to be [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)], "
    f"got {pairs!r}. "
    f"Use [(x, y) for x in [1,2,3] for y in [1,2,3] if x != y]."
)
assert isinstance(pairs, list), (
    f"Expected pairs to be a list, got {type(pairs).__name__}."
)
assert all(isinstance(p, tuple) for p in pairs), (
    f"Expected each element of pairs to be a tuple. "
    f"Got types: {[type(p).__name__ for p in pairs]}. "
    f"Use (x, y) as the expression in the comprehension."
)
assert len(pairs) == 6, (
    f"Expected 6 pairs (3 choices for x * 3 choices for y - 3 where x==y), "
    f"got {len(pairs)}."
)

print("All tests passed!")
