# Step 3: Comparing approaches (in, get, try/except) — Snippets
# Dictionaries: three ways to handle missing keys, and .get() with compound defaults

# --- Snippet 1 ---
# Three equivalent ways to safely access a missing key with a default

d = {"a": 1}

# (a) Using 'in'
if "b" in d:
    val = d["b"]
else:
    val = 0
print(val)

# (b) Using .get()
val = d.get("b", 0)
print(val)

# (c) Using try/except
try:
    val = d["b"]
except KeyError:
    val = 0
print(val)

# Your answer:


# --- Snippet 2 ---
# Using .get() with defaults that are themselves indexed or accessed further

d = {"name": "Alice", "scores": [90, 85]}

print(d.get("email", "N/A"))
print(d.get("scores", [])[0])
print(d.get("missing", [0, 0])[1])

# Your answer:
