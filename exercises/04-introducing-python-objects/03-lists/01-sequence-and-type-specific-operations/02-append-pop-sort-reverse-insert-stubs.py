# Step 2: append, pop, sort, reverse, insert
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Given `nums`, sort it in ascending order and then pop the largest element
# (which will be the last element after sorting).
# Store the popped value in `largest`.
# After this, `nums` should be the sorted list without that largest element.

nums = [5, 3, 8, 1, 9, 2]

# Your code here (use list methods):


# --- Stub 2 ---
# Given `L` (already sorted), insert the value 4 at the correct position
# so the list remains sorted.
# Expected result: L == [1, 3, 4, 5, 7]
# Hint: figure out the right index to insert at.

L = [1, 3, 5, 7]

# Your code here (use list methods):


# --- Tests ---

# Stub 1 tests
assert largest == 9, (
    f"Expected largest to be 9, got {largest!r}. "
    f"After sorting [5, 3, 8, 1, 9, 2] in ascending order, the last element is the largest. "
    f"Use .pop() to remove and return it."
)
assert nums == [1, 2, 3, 5, 8], (
    f"Expected nums to be [1, 2, 3, 5, 8] after sorting and popping the largest, got {nums!r}. "
    f"First .sort() the list, then .pop() removes the last element."
)

# Stub 2 tests
assert L == [1, 3, 4, 5, 7], (
    f"Expected L to be [1, 3, 4, 5, 7], got {L!r}. "
    f"Use .insert(index, value) to place 4 at the right position. "
    f"The index is where the new element will end up."
)

print("All tests passed!")
