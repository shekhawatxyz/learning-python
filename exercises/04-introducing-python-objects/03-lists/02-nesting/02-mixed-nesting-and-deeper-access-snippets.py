# Step 2: Mixed nesting and deeper access
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: lists containing different types (string, list, dict),
# chained indexing across different container types.
# Note: dictionary access with ["key"] is previewed here.

record = ["Alice", [95, 87, 91], {"grade": "A"}]
print(record[0])
print(record[1][0])
print(record[1][-1])
print(record[2]["grade"])

# Your answer:

# --- Snippet 2 ---
# Explores: 3D nesting (list of lists of lists), triple indexing,
# and len() at different nesting levels.

grid = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(grid[0][1][0])
print(grid[1][0][1])
print(len(grid))
print(len(grid[0]))
print(len(grid[0][0]))

# Your answer:
