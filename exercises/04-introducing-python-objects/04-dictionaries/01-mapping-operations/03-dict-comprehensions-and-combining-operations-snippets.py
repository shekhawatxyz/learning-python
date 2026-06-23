# Step 3: Dict comprehensions and combining operations — Snippets
# Dictionaries: comprehension syntax, filtering, and building from sequences

# --- Snippet 1 ---
# Basic dict comprehensions: from a range and from a list of tuples

print({x: x**2 for x in range(5)})
print({k: v for k, v in [("a", 1), ("b", 2), ("c", 3)]})

# Your answer:
# {0:0,1:1,2:4,3:9,4:16}
# {"a":1,"b":2,"c":3}

# --- Snippet 2 ---
# Dict comprehensions with a real use case and with filtering

words = ["hello", "world", "python"]
print({w: len(w) for w in words})
print({k: v for k, v in {"a": 1, "b": 2, "c": 3}.items() if v > 1})

# Your answer:
# {"hello":5,"world":5,"python":5}
# {"b":2,"c":3}
