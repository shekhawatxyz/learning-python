# Step 2: Formatting, comparisons, and rounding
# Complete each stub according to the requirements.

# --- Stub 1 ---
# For the given scores, compute:
# - best score and average score
# - best_label exactly as "best=91.2" (1 decimal place)
# - within_band: list of booleans for 80 <= score < 90
# - rounded_scores: list rounded to 1 decimal place

scores = [88.5, 91.25, 79.0, 91.249]

best = ...
average = ...
best_label = ...
within_band = ...
rounded_scores = ...


# --- Stub 2 ---
# For each (a, b) pair, compute a tuple:
# (true_division, floor_division, modulus, reconstruction_ok)
# where reconstruction_ok checks: a == (a // b) * b + (a % b)

pairs = [(19, 4), (-19, 4), (19, -4), (-19, -4)]

results = ...


# --- Tests ---

assert best == 91.25, (
    f"Expected best 91.25, got {best!r}."
)

assert abs(average - 87.49975) < 1e-12, (
    f"Expected average 87.49975, got {average!r}."
)

assert best_label == "best=91.2", (
    f"Expected best_label 'best=91.2', got {best_label!r}."
)

assert within_band == [True, False, False, False], (
    f"Expected within_band [True, False, False, False], got {within_band!r}."
)

assert rounded_scores == [88.5, 91.2, 79.0, 91.2], (
    f"Expected rounded_scores [88.5, 91.2, 79.0, 91.2], got {rounded_scores!r}."
)

expected_results = [
    (4.75, 4, 3, True),
    (-4.75, -5, 1, True),
    (-4.75, -5, -1, True),
    (4.75, 4, -3, True),
]
assert results == expected_results, (
    f"Expected results {expected_results!r}, got {results!r}."
)

print("All tests passed!")
