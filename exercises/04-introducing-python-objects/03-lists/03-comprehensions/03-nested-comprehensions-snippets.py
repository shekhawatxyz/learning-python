# Step 3: Nested comprehensions
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: extracting a column from a matrix with a comprehension,
# and nested for clauses with filtering (flattening + filter).

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([M[row][1] for row in range(3)])
print([M[row][col] for row in range(3) for col in range(3) if M[row][col] % 2 == 0])

# Your answer:

# --- Snippet 2 ---
# Explores: comprehension that produces a list of lists (nested result),
# and a comprehension with nested for clauses that flattens.
# Key distinction: outer brackets create the nesting structure.

print([[i * j for j in range(1, 4)] for i in range(1, 4)])
print([x for sublist in [[1, 2], [3, 4], [5, 6]] for x in sublist])

# Your answer:
