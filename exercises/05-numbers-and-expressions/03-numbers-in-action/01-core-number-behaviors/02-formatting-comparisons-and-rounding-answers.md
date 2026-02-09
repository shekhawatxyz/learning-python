# Step 2: Formatting, comparisons, and rounding — Answer Key

## Snippet 1

**Expected output:**

```text
0.3333333333333333
0.3333
33.33%
True
```

**Rationale:** Numeric display formats can emphasize different representations (`str`, fixed decimals, percent style). `math.isclose` compares within tolerances and is usually better than exact `==` for float math.

## Snippet 2

**Expected output:**

```text
-13 -13 -12 -12
-2 7
```

**Rationale:** `floor` and `ceil` move toward negative/positive infinity respectively, while `trunc` drops the fractional part toward zero. `round` applies standard rounding rules on the float value provided.
