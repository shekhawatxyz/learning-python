# Step 3: Matrix ops and sliding windows
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: matrix multiplication with nested comprehensions.

A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]

product = [
    [sum(a * b for a, b in zip(row, col)) for col in zip(*B)]
    for row in A
]

print(product)
print([sum(row) for row in product])

# Your answer:

# --- Snippet 2 ---
# Explores: sliding-window moving averages.

series = [10, 12, 14, 16, 18, 20]
window = 3
moving_avg = [sum(series[i:i + window]) / window for i in range(len(series) - window + 1)]

print(moving_avg)
print(max(moving_avg) - min(moving_avg))

# Your answer:
