# Step 3: Matrix ops and sliding windows — Answer Key

## Snippet 1

**Expected output:**

```text
[[4, 4], [10, 8]]
[8, 18]
```

**Rationale:** Matrix multiplication combines row/column dot products. `zip(*B)` transposes columns for clean row-by-column pairing.

## Snippet 2

**Expected output:**

```text
[12.0, 14.0, 16.0, 18.0]
6.0
```

**Rationale:** Sliding windows capture local trends over consecutive subsequences. The range of moving averages summarizes trend spread.
