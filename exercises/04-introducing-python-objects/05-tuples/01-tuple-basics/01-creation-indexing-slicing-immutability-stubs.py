# Tuples: Creation, Indexing, Slicing, Immutability — Stubs

# --- Stub 1 ---
# Given the tuple t below, extract:
#   - The first element, stored in `first`
#   - The last element, stored in `last`
#   - A slice of the middle three elements (20, 30, 40), stored in `middle`

t = (10, 20, 30, 40, 50)

# Write your code here:



# --- Stub 2 ---
# Given the tuple `point` below, unpack it into variables `x` and `y`.
# Then compute the Euclidean distance from the origin: sqrt(x**2 + y**2).
# Store the result in `distance`. Use math.sqrt.

import math

point = (3, 4)

# Write your code here:



# --- Tests ---

# Tests for Stub 1
assert first == 10, f"Expected first to be 10, got {first}"
assert last == 50, f"Expected last to be 50, got {last}"
assert middle == (20, 30, 40), f"Expected middle to be (20, 30, 40), got {middle}"
assert isinstance(middle, tuple), f"Expected middle to be a tuple, got {type(middle).__name__}"

# Tests for Stub 2
assert x == 3, f"Expected x to be 3, got {x}"
assert y == 4, f"Expected y to be 4, got {y}"
assert distance == 5.0, f"Expected distance to be 5.0 (3-4-5 right triangle), got {distance}"

print("All tests passed!")
