# Step 7: Numeric extensions readiness
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: vector-style operations in plain Python.

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

print([x + y for x, y in zip(a, b)])
print(sum(x * y for x, y in zip(a, b)))

# Your answer:

# --- Snippet 2 ---
# Explores: matrix-vector style computation and filtered transforms.

matrix = [[1, 2, 3], [4, 5, 6]]
vector = [2, 0, -1]

print([sum(m * v for m, v in zip(row, vector)) for row in matrix])
print([x**2 for x in [1, 2, 3, 4, 5] if x % 2 == 1])

# Your answer:
