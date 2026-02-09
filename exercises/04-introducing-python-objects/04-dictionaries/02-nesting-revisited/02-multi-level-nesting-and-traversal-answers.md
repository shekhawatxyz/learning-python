# Step 2: Multi-level nesting and traversal — Answers

## Snippet 1

**Expected output:**
```
5432
5433
True
2
```

**Rationale:** `config["db"]["ports"][0]` chains three accesses: first the `"db"` key yields the nested dict, then `"ports"` yields the list `[5432, 5433]`, then index `[0]` gives the first element, `5432`. `config["db"]["ports"][-1]` uses negative indexing to get the last port, `5433`. `config["app"]["debug"]` retrieves the boolean `True`. `len(config)` returns `2` because the top-level dict has exactly two keys: `"db"` and `"app"`. Importantly, `len()` on a dict counts only the top-level keys, not any nested contents.

## Snippet 2

**Expected output:**
```
Alice
92
['Alice', 'Bob', 'Charlie']
[90, 92]
```

**Rationale:** `records` is a list of dicts. `records[0]["name"]` gets the first dict and accesses its `"name"` key, giving `"Alice"`. `records[-1]["score"]` gets the last dict (Charlie's) and accesses `"score"`, giving `92`. The list comprehension `[r["name"] for r in records]` iterates over all dicts and collects each name into a list. The filtered comprehension `[r["score"] for r in records if r["score"] > 88]` collects only those scores greater than 88: Alice's 90 and Charlie's 92 qualify (Bob's 85 does not). This pattern of using list comprehensions to extract or filter fields from a list of dicts is extremely common in Python.
