# Sets: Set Comprehensions and Practical Deduplication — Snippets

# --- Snippet 1 ---
# Set comprehensions

print({x ** 2 for x in range(-3, 4)})
print({c for c in "hello world" if c != " "})

# Note: Set display order is not guaranteed. The elements are deterministic
# (the same set will always be produced), but the order they appear in when
# printed may vary. For small integers, CPython typically displays them sorted.
# For characters, the order may be less predictable.

# Your answer:


# --- Snippet 2 ---
# Deduplication with sets

words = ["apple", "banana", "apple", "cherry", "banana"]
unique = set(words)
print(unique)
print(sorted(unique))
print(len(words), len(unique))

# Note: print(unique) display order is not guaranteed, but sorted(unique)
# will always be in alphabetical order.

# Your answer:
