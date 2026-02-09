# Step 1: Basic list comprehensions
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: basic list comprehension syntax, range(), and applying
# an expression to each element; comprehension over a string.

print([x ** 2 for x in range(6)])
print([c.upper() for c in "hello"])

# Your answer:

# --- Snippet 2 ---
# Explores: comprehension as transformation of an existing list,
# identity comprehension (copying), and using sum() with a comprehension.

nums = [1, 2, 3, 4, 5]
print([x * 10 for x in nums])
print([x for x in nums])
print(sum([x for x in nums]))

# Your answer:
