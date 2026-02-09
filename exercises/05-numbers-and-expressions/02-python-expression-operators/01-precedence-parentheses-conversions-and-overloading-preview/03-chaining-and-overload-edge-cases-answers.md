# Step 3: Chaining and overload edge cases — Answer Key

## Snippet 1

**Expected output:**

```text
1 0
True
False
```

**Rationale:** `&` has higher precedence than `|`. Comparison chaining (`a < b == c < d`) is not the same as inserting parentheses around each comparison result; it chains shared operands.

## Snippet 2

**Expected output:**

```text
Bucket(14)
Bucket(20)
Bucket(27)
```

**Rationale:** Operator precedence applies before overloaded methods are dispatched. Grouping with parentheses changes which operations run first, even when objects define custom arithmetic.
