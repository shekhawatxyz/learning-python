# Step 1: Creation and basic access — Answers

## Snippet 1

**Expected output:**
```
Alice
30
3
True
False
```

**Rationale:** `d["name"]` retrieves the value associated with the key `"name"`, which is `"Alice"`. `d["age"]` retrieves `30`. `len(d)` returns the number of key-value pairs, which is 3. The `in` operator tests for key membership: `"name"` is a key in `d` so it returns `True`, while `"email"` is not a key so it returns `False`. Note that `in` checks keys, not values.

## Snippet 2

**Expected output:**
```
{'x': 99, 'y': 20}
99
2
```

**Rationale:** Starting from an empty dict `{}`, assigning `d["x"] = 10` creates key `"x"` with value `10`, and `d["y"] = 20` creates key `"y"` with value `20`. Then `d["x"] = 99` overwrites the existing value for key `"x"` — dictionary keys are unique, so assigning to an existing key replaces its value rather than adding a second entry. The dict has only 2 keys (`"x"` and `"y"`), so `len(d)` is `2`, and `d["x"]` is now `99`.
