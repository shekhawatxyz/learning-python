# Step 3: Floating-point robustness and big integers
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Implement close_enough using math.isclose.
# Then evaluate two tolerance profiles over the provided pairs:
# - default_results with rel_tol=1e-9, abs_tol=0.0
# - strict_results with rel_tol=0.0, abs_tol=1e-9

import math


def close_enough(a, b, rel_tol=1e-9, abs_tol=0.0):
    ...


pairs = [
    (0.1 + 0.2, 0.3),
    (10_000_000_001.0, 10_000_000_000.0),
    (1e-12, 0.0),
]

default_results = ...
strict_results = ...


# --- Stub 2 ---
# For n = 10**60 + 2**80, compute:
# - decimal_digits (len(str(n)))
# - bit_len (n.bit_length())
# - prefix first 5 decimal digits as string
# - suffix last 5 decimal digits as string
# - mod_check = n % 1_000_000

n = ...

decimal_digits = ...
bit_len = ...
prefix = ...
suffix = ...
mod_check = ...


# --- Tests ---

assert default_results == [True, True, False], (
    f"Expected default_results [True, True, False], got {default_results!r}."
)

assert strict_results == [True, False, True], (
    f"Expected strict_results [True, False, True], got {strict_results!r}."
)

assert n == 10**60 + 2**80, (
    f"Expected n to be 10**60 + 2**80, got {n!r}."
)

assert decimal_digits == 61, (
    f"Expected decimal_digits 61, got {decimal_digits!r}."
)

assert bit_len == 200, (
    f"Expected bit_len 200, got {bit_len!r}."
)

assert prefix == "10000", (
    f"Expected prefix '10000', got {prefix!r}."
)

assert suffix == "06176", (
    f"Expected suffix '06176', got {suffix!r}."
)

assert mod_check == 706176, (
    f"Expected mod_check 706176, got {mod_check!r}."
)

print("All tests passed!")
