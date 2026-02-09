# Step 1: Basic nested dicts — Answers

## Snippet 1

**Expected output:**
```
Alice
NYC
85
92
```

**Rationale:** `person["name"]` accesses the top-level key, yielding `"Alice"`. `person["address"]["city"]` chains two key accesses: first retrieving the nested dict `{"street": "123 Main", "city": "NYC"}`, then accessing `"city"` within it to get `"NYC"`. `person["scores"][1]` first retrieves the list `[90, 85, 92]`, then indexes it at position 1 (the second element), giving `85`. `person["scores"][-1]` uses negative indexing to get the last element of the list, which is `92`. This snippet demonstrates that dict values can be other dicts or lists, and you chain indexing operations to reach nested data.

## Snippet 2

**Expected output:**
```
eng
25
31
```

**Rationale:** `db["alice"]["role"]` navigates into alice's nested dict to get `"eng"`. `db["bob"]["age"]` gets `25`. The assignment `db["alice"]["age"] = 31` mutates the nested dict in place -- it changes the value associated with `"age"` inside alice's dict from `30` to `31`. The final print confirms the change. This works because dicts are mutable objects; the nested dict is a shared object that can be modified through the reference held in the outer dict.
