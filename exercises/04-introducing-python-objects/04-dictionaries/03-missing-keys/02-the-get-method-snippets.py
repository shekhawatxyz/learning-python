# Step 2: The get() method — Snippets
# Dictionaries: using .get() for safe access with defaults

# --- Snippet 1 ---
# Basic .get() usage: existing keys, missing keys, and custom defaults

d = {"a": 1, "b": 2}

print(d.get("a"))
print(d.get("c"))
print(d.get("c", 0))
print(d.get("c", "default"))

# Your answer:


# --- Snippet 2 ---
# The classic .get()-based accumulation pattern for counting

words = ["the", "cat", "sat", "on", "the", "mat"]
counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

print(counts)

# Your answer:
