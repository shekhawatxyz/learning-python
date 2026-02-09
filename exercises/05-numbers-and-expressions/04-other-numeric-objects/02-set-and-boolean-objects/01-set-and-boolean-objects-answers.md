# Step 6: Set and Boolean objects — Answer Key

## Snippet 1

**Expected output:**

```text
[1, 2, 3, 4, 5]
[3, 4]
[1, 2]
[1, 2, 5]
True False
```

**Rationale:** Set operators implement union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`). Subset/superset checks return booleans. Sorting is used only for stable display order.

## Snippet 2

**Expected output:**

```text
rw
[0, 4, 16]
2 0 False True
```

**Rationale:** `frozenset` is hashable, so it can be a dictionary key. Set comprehensions remove duplicates naturally. Booleans behave numerically (`True == 1`, `False == 0`) while still representing truth values.
