# Step 3: Combining operations, the mutability factor
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: shared references vs. copies
# This is a critical concept: assignment does NOT copy a list.

L = [1, 2, 3]
M = L
L.append(4)
print(L)
print(M)

L = [1, 2, 3]
M = L[:]
L.append(4)
print(L)
print(M)

# Your answer:

# --- Snippet 2 ---
# Explores: sorted() (returns new list) vs. .sort() (mutates in place)

original = [3, 1, 2]
sorted_copy = sorted(original)
print(original)
print(sorted_copy)
original.sort()
print(original)

# Your answer:
