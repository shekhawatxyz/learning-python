# Step 7: Numeric extensions readiness — Answer Key

## Snippet 1

**Expected output:**

```text
[11, 22, 33, 44]
300
```

**Rationale:** Pairwise operations via `zip` mirror vectorized thinking: element-wise addition and dot product are foundational patterns that numeric libraries accelerate.

## Snippet 2

**Expected output:**

```text
[-1, 2]
[1, 9, 25]
```

**Rationale:** Each row-vector dot product yields one matrix-vector output element. The comprehension on the second line filters odd values before squaring, illustrating transform pipelines common in numeric workflows.
