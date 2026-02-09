# Step 2: Comprehensions with filtering
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: the if clause in a list comprehension to filter elements,
# combining filtering with transformation.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x for x in nums if x % 2 == 0])
print([x ** 2 for x in nums if x > 5])

# Your answer:

# --- Snippet 2 ---
# Explores: filtering with string methods — len() and str methods
# as filter conditions, combining filter + transformation.

words = ["Hello", "world", "Python", "is", "great"]
print([w for w in words if len(w) > 4])
print([w.upper() for w in words if w[0].isupper()])

# Your answer:
