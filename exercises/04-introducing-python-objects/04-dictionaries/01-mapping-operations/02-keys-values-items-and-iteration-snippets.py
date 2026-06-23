# Step 2: keys(), values(), items() and iteration — Snippets
# Dictionaries: view objects, sorted(), and two styles of iteration

# --- Snippet 1 ---
# Extracting keys, values, and items as lists; sorting keys

d = {"a": 1, "b": 2, "c": 3}

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
print(sorted(d.keys()))

# Your answer:
# ["a", "b", "c"]
# [1, 2, 3]
# [("a", 1), ("b", 2), ("c", 3)]
# ["a", "b", "c"]
# --- Snippet 2 ---
# Two styles of iterating over a dict

d = {"x": 10, "y": 20, "z": 30}

for k in d:
    print(k, d[k])

for k, v in d.items():
    print(f"{k} = {v}")

# Your answer:
# x 10
# y 20
# z 30
# x = 10
# y = 20
# z = 30
