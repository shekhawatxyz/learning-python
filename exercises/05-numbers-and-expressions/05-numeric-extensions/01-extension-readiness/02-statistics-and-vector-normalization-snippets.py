# Step 2: Statistics and vector normalization
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: mean and population variance in plain Python.

data = [2, 4, 4, 4, 5, 5, 7, 9]
mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)

print(mean)
print(round(variance, 2))

# Your answer:

# --- Snippet 2 ---
# Explores: L2 norm and vector normalization.

vec = [3, 4]
norm = (sum(x * x for x in vec)) ** 0.5
normalized = [round(x / norm, 3) for x in vec]

print(norm)
print(normalized)

# Your answer:
