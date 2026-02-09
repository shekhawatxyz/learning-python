# Step 2: Set method workflows and truthiness — Answer Key

## Snippet 1

**Expected output:**

```text
4 True False
['byte', 'py']
```

**Rationale:** `set(...)` removes duplicates. Membership checks are O(1)-style lookups on average. Intersection keeps common elements only.

## Snippet 2

**Expected output:**

```text
[0, 2, 4, 6, 8]
[1, 3, 5, 7, 9]
True True
```

**Rationale:** Set comprehensions build filtered sets, and relation methods (`isdisjoint`, `issuperset`) express logical set relationships directly.
