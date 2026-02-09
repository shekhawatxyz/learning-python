# Step 3: Core number behaviors — Answer Key

## Snippet 1

**Expected output:**

```text
59.985
59.985
59.98
True
False
```

**Rationale:** `subtotal` is computed from variables. `repr()` and plain `print()` show the same visible value here, while formatting to 2 decimals rounds for display. Chained comparisons work left-to-right logically. `0.1 + 0.2 == 0.3` is `False` due to binary floating-point representation.

## Snippet 2

**Expected output:**

```text
2.75
2 3
-3 1
True 37
```

**Rationale:** `/` performs true division, `//` floor division, and `%` gives the remainder consistent with `a == (a // b) * b + (a % b)`. Python integers have arbitrary precision, so very large powers are supported directly.
