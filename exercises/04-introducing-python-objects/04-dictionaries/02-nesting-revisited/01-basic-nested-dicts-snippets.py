# Step 1: Basic nested dicts — Snippets
# Dictionaries: nesting dicts within dicts, mixing dicts and lists, in-place mutation

# --- Snippet 1 ---
# Accessing nested dicts and lists within a dict

person = {
    "name": "Alice",
    "address": {"street": "123 Main", "city": "NYC"},
    "scores": [90, 85, 92]
}

print(person["name"])
print(person["address"]["city"])
print(person["scores"][1])
print(person["scores"][-1])

# Your answer:


# --- Snippet 2 ---
# A dict of dicts: accessing and mutating nested values

db = {
    "alice": {"age": 30, "role": "eng"},
    "bob": {"age": 25, "role": "mgr"}
}

print(db["alice"]["role"])
print(db["bob"]["age"])

db["alice"]["age"] = 31

print(db["alice"]["age"])

# Your answer:
