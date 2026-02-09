# Step 3: Frozenset modeling and boolean flow — Answer Key

## Snippet 1

**Expected output:**

```text
3
True
['AB', 'AC', 'BC']
```

**Rationale:** `frozenset` ignores element order and is hashable, so it works for representing undirected edges in a set.

## Snippet 2

**Expected output:**

```text
fallback
123
0 5
2
```

**Rationale:** `and`/`or` return operands, not coerced booleans. `bool(...)` values also participate in integer arithmetic because `bool` subclasses `int`.
