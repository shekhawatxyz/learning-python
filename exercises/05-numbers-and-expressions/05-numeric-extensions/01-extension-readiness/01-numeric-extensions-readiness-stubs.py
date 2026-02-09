# Step 7: Numeric extensions readiness
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Implement vector operations with plain Python.
# - vector_add(a, b): element-wise addition
# - dot(a, b): dot product


def vector_add(a, b):
    ...


def dot(a, b):
    ...


v1 = [3, -1, 4]
v2 = [2, 5, 0]

added = vector_add(v1, v2)
dot_value = dot(v1, v2)


# --- Stub 2 ---
# Implement matrix-vector multiplication.
# `matvec(matrix, vector)` should return one number per row,
# where each output is the row's dot product with vector.
# Also compute L1 norm (sum of absolute values) of the result.


def matvec(matrix, vector):
    ...


M = [
    [2, 1, 0],
    [0, -1, 3],
    [4, 0, 1],
]
v = [3, 2, -2]

result = matvec(M, v)
l1_norm = ...


# --- Tests ---

assert added == [5, 4, 4], (
    f"Expected added to be [5, 4, 4], got {added!r}."
)

assert dot_value == 1, (
    f"Expected dot_value to be 1, got {dot_value!r}. "
    f"Compute sum(x * y for x, y in zip(a, b))."
)

assert result == [8, -8, 10], (
    f"Expected matvec result [8, -8, 10], got {result!r}."
)

assert l1_norm == 26, (
    f"Expected l1_norm to be 26, got {l1_norm!r}. "
    f"Compute sum(abs(x) for x in result)."
)

print("All tests passed!")
