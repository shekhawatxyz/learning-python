# Step 1: KeyError and the 'in' operator — Answers

## Snippet 1

**Expected output:**
```
True
False
not found
```

**Rationale:** `"a" in d` checks whether `"a"` is a key in the dict and returns `True` (it is). `"c" in d` returns `False` because `"c"` is not a key. The `in` operator on dicts tests for key membership, not value membership. The if/else block then checks `"c" in d`, which is `False`, so the `else` branch executes and prints `"not found"`. Without the `in` check, `d["c"]` would raise a `KeyError`. This is the fundamental pattern for safe dict access using `in`.

## Snippet 2

**Expected output:**
```
x: 10
y: 20
z: missing
```

**Rationale:** The loop iterates over `["x", "y", "z"]`. For `"x"`: it is in `d`, so `f"{k}: {d[k]}"` produces `"x: 10"`. For `"y"`: also in `d`, producing `"y: 20"`. For `"z"`: not in `d`, so the else branch produces `"z: missing"`. This pattern -- iterating over a collection of keys and checking each against a dict -- is very common when you need to look up values that may or may not exist.
