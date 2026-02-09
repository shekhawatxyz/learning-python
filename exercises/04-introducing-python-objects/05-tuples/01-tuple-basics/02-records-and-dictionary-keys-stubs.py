# Tuples: Records and Dictionary Keys — Stubs

# --- Stub 1 ---
# Given the list of tuples `pairs` below, sort them by their first element
# (the default tuple sort does this). Store the sorted result in `sorted_pairs`.
# Then unpack the FIRST pair in `sorted_pairs` into `num` and `fruit`.
#
# Expected: sorted_pairs = [(1, "apple"), (2, "banana"), (3, "cherry")]
#           num = 1, fruit = "apple"

pairs = [(2, "banana"), (1, "apple"), (3, "cherry")]

# Write your code here:



# --- Stub 2 ---
# Given the list of (x, y) coordinate tuples below, create a dictionary
# `distances` that maps each tuple to its Euclidean distance from the origin.
# Distance from origin = sqrt(x**2 + y**2). Use math.sqrt.
#
# Example: distances[(1, 2)] should be math.sqrt(1**2 + 2**2) = math.sqrt(5)

import math

points = [(1, 2), (3, 4), (0, 0), (5, 1)]

# Write your code here:



# --- Tests ---

# Tests for Stub 1
assert sorted_pairs == [(1, "apple"), (2, "banana"), (3, "cherry")], \
    f"Expected sorted_pairs to be [(1, 'apple'), (2, 'banana'), (3, 'cherry')], got {sorted_pairs}"
assert num == 1, f"Expected num to be 1, got {num}"
assert fruit == "apple", f"Expected fruit to be 'apple', got {fruit!r}"

# Verify original list is unchanged (sorted() returns new list vs .sort() in place)
# Either approach is fine, but sorted_pairs must have the right value.

# Tests for Stub 2
assert isinstance(distances, dict), f"Expected distances to be a dict, got {type(distances).__name__}"
assert len(distances) == 4, f"Expected 4 entries in distances, got {len(distances)}"

expected_distances = {
    (1, 2): math.sqrt(5),
    (3, 4): math.sqrt(25),
    (0, 0): 0.0,
    (5, 1): math.sqrt(26),
}

for point, expected_dist in expected_distances.items():
    assert point in distances, f"Expected {point} to be a key in distances, but it's missing"
    assert abs(distances[point] - expected_dist) < 1e-9, \
        f"Expected distances[{point}] to be {expected_dist}, got {distances[point]}"

print("All tests passed!")
