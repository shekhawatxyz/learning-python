# Step 1: Basic list comprehensions
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Given `nums`, use a list comprehension to create a list of cubes.
# Store in `cubes`.
# Expected: [1, 8, 27, 64, 125]

nums = [1, 2, 3, 4, 5]

cubes = ...  # replace ... with a list comprehension

# --- Stub 2 ---
# Given `words`, use a list comprehension to create a list of their lengths.
# Store in `lengths`.
# Expected: [5, 5, 6]

words = ["hello", "world", "python"]

lengths = ...  # replace ... with a list comprehension

# --- Tests ---

# Stub 1 tests
assert cubes == [1, 8, 27, 64, 125], (
    f"Expected cubes to be [1, 8, 27, 64, 125], got {cubes!r}. "
    f"Use [x ** 3 for x in nums] or similar."
)
assert isinstance(cubes, list), (
    f"Expected cubes to be a list, got {type(cubes).__name__}. "
    f"A list comprehension produces a list."
)
assert nums == [1, 2, 3, 4, 5], (
    f"Expected nums to be unchanged at [1, 2, 3, 4, 5], got {nums!r}. "
    f"A list comprehension creates a new list; it does not modify the source."
)

# Stub 2 tests
assert lengths == [5, 5, 6], (
    f"Expected lengths to be [5, 5, 6], got {lengths!r}. "
    f"Use len() on each word inside the comprehension."
)
assert isinstance(lengths, list), (
    f"Expected lengths to be a list, got {type(lengths).__name__}."
)

print("All tests passed!")
