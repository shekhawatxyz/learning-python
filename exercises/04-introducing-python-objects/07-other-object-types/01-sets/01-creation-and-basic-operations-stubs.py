# Sets: Creation and Basic Operations — Stubs

# --- Stub 1 ---
# Given the two lists below, find the elements they have in common using sets.
# Store the result as a SORTED LIST in `common`.
#
# Expected: common = [4, 5]

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

# Write your code here:



# --- Stub 2 ---
# Given the same two lists, find the elements that are in list_a but NOT
# in list_b. Store the result as a SORTED LIST in `only_a`.
#
# Expected: only_a = [1, 2, 3]

# Write your code here:



# --- Tests ---

# Tests for Stub 1
assert isinstance(common, list), \
    f"Expected common to be a list, got {type(common).__name__}. Convert the set to a sorted list."
assert common == [4, 5], \
    f"Expected common to be [4, 5], got {common}"

# Tests for Stub 2
assert isinstance(only_a, list), \
    f"Expected only_a to be a list, got {type(only_a).__name__}. Convert the set to a sorted list."
assert only_a == [1, 2, 3], \
    f"Expected only_a to be [1, 2, 3], got {only_a}"

print("All tests passed!")
