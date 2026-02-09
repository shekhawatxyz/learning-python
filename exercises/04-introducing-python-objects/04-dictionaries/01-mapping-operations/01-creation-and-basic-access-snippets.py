# Step 1: Creation and basic access — Snippets
# Dictionaries: literal creation, empty creation, assignment, update, membership

# --- Snippet 1 ---
# Creating a dict with a literal and accessing its contents

d = {"name": "Alice", "age": 30, "city": "NYC"}

print(d["name"])
print(d["age"])
print(len(d))
print("name" in d)
print("email" in d)

# Your answer:


# --- Snippet 2 ---
# Creating a dict from empty, adding keys, and overwriting an existing key

d = {}
d["x"] = 10
d["y"] = 20
d["x"] = 99

print(d)
print(d["x"])
print(len(d))

# Your answer:
