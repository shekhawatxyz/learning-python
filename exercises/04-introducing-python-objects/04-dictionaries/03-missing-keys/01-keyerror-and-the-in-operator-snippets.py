# Step 1: KeyError and the 'in' operator — Snippets
# Dictionaries: safe key access using membership testing with 'in'

# --- Snippet 1 ---
# Using 'in' to test for key existence before accessing

d = {"a": 1, "b": 2}

print("a" in d)
print("c" in d)

if "c" in d:
    print(d["c"])
else:
    print("not found")

# Your answer:


# --- Snippet 2 ---
# Iterating over a list of keys and checking each against a dict

d = {"x": 10, "y": 20}
keys_to_check = ["x", "y", "z"]

for k in keys_to_check:
    if k in d:
        print(f"{k}: {d[k]}")
    else:
        print(f"{k}: missing")

# Your answer:
