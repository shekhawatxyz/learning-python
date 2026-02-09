# Step 2: Multi-level nesting and traversal — Snippets
# Dictionaries: deeper nesting, lists of dicts, and comprehensions over nested structures

# --- Snippet 1 ---
# A config-style nested dict with dicts containing lists

config = {
    "db": {"host": "localhost", "ports": [5432, 5433]},
    "app": {"debug": True, "name": "myapp"}
}

print(config["db"]["ports"][0])
print(config["db"]["ports"][-1])
print(config["app"]["debug"])
print(len(config))

# Your answer:


# --- Snippet 2 ---
# A list of dicts: indexing, field access, and comprehensions over records

records = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 92}
]

print(records[0]["name"])
print(records[-1]["score"])
print([r["name"] for r in records])
print([r["score"] for r in records if r["score"] > 88])

# Your answer:
