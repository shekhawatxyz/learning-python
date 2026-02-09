# Step 6: Set and Boolean objects
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: set algebra and subset/superset checks.

a = {1, 2, 3, 4}
b = {3, 4, 5}

print(sorted(a | b))
print(sorted(a & b))
print(sorted(a - b))
print(sorted(a ^ b))
print({1, 2} <= a, a >= b)

# Your answer:

# --- Snippet 2 ---
# Explores: frozenset as dict keys, set comprehensions, and booleans as ints.

flags = frozenset({"read", "write"})
lookup = {flags: "rw"}

print(lookup[frozenset({"write", "read"})])
print(sorted({n * n for n in [0, 1, 2, 2, 3, 4, 4, 5] if n % 2 == 0}))
print(True + True, False * 10, bool(""), bool("python"))

# Your answer:
