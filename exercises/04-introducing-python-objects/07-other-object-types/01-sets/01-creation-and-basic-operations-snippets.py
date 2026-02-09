# Sets: Creation and Basic Operations — Snippets

# --- Snippet 1 ---
# Set creation and basic properties: duplicates removed, membership testing

s = {1, 2, 3, 2, 1}

print(s)
print(len(s))
print(2 in s)
print(5 in s)

# Note: Sets are unordered. The print(s) output will contain {1, 2, 3} but
# the display order is not guaranteed. For small integers, CPython typically
# displays them in ascending order, but this is an implementation detail.

# Your answer:


# --- Snippet 2 ---
# Set operations: intersection, union, difference, symmetric difference

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
print(a | b)
print(a - b)
print(b - a)
print(a ^ b)

# Note: Again, display order within each set is not guaranteed, but for small
# integers CPython typically shows them sorted.

# Your answer:
