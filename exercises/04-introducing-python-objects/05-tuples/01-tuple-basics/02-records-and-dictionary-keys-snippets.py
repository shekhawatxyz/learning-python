# Tuples: Records and Dictionary Keys — Snippets

# --- Snippet 1 ---
# Tuple unpacking and variable swapping

record = ("Alice", 30, "Engineer")
name, age, role = record

print(name)
print(age)
print(role)

a, b = 1, 2
a, b = b, a
print(a, b)

# Your answer:


# --- Snippet 2 ---
# Tuples as dictionary keys; tuple comparison and sorting

locations = {}
locations[(0, 0)] = "origin"
locations[(1, 2)] = "point A"

print(locations[(0, 0)])
print((1, 2) in locations)

coords = [(3, 1), (1, 2), (2, 3)]
coords.sort()
print(coords)

# Your answer:
