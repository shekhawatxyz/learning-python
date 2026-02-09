# Step 2: Set method workflows and truthiness
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: deduplication, membership, and set intersection.

words = ["python", "py", "thon", "python", "byte", "py"]
s = set(words)

print(len(s), "python" in s, "java" in s)
print(sorted(s.intersection({"py", "java", "byte"})))

# Your answer:

# --- Snippet 2 ---
# Explores: set comprehensions and relation checks.

evens = {n for n in range(10) if n % 2 == 0}
odds = set(range(10)) - evens

print(sorted(evens))
print(sorted(odds))
print(evens.isdisjoint(odds), evens.issuperset({0, 2, 4}))

# Your answer:
