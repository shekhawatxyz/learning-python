# Step 3: Matrix ops and sliding windows
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Implement generic matrix multiplication matmul(A, B).
# Assume dimensions are valid.


def matmul(A, B):
    ...


A = [
    [1, 2, 3],
    [4, 5, 6],
]

B = [
    [7, 8],
    [9, 10],
    [11, 12],
]

matmul_result = matmul(A, B)
row_sums = ...


# --- Stub 2 ---
# Compute z-scores for the full series using population std deviation.
# z = (x - mean) / std
# Build:
# - z_scores rounded to 3 decimals
# - extreme_count = number of entries with abs(z) >= 1

import math

series = [3, 5, 7, 9, 11]

mean = ...
variance = ...
std = ...
z_scores = ...
extreme_count = ...


# --- Tests ---

assert matmul_result == [[58, 64], [139, 154]], (
    f"Expected matmul_result [[58, 64], [139, 154]], got {matmul_result!r}."
)

assert row_sums == [122, 293], (
    f"Expected row_sums [122, 293], got {row_sums!r}."
)

assert mean == 7.0, (
    f"Expected mean 7.0, got {mean!r}."
)

assert variance == 8.0, (
    f"Expected variance 8.0, got {variance!r}."
)

assert abs(std - 2.8284271247461903) < 1e-12, (
    f"Expected std about 2.8284271247461903, got {std!r}."
)

assert z_scores == [-1.414, -0.707, 0.0, 0.707, 1.414], (
    f"Expected z_scores [-1.414, -0.707, 0.0, 0.707, 1.414], got {z_scores!r}."
)

assert extreme_count == 2, (
    f"Expected extreme_count 2, got {extreme_count!r}."
)

print("All tests passed!")
