# Step 5: Decimal and Fraction objects — Answer Key

## Snippet 1

**Expected output:**

```text
False
True
23.5882
```

**Rationale:** Binary floats cannot represent many decimals exactly, so repeated `0.1` addition can miss exact equality. `Decimal` uses decimal arithmetic, so exact tenths compare as expected. Decimal multiplication follows the current context precision.

## Snippet 2

**Expected output:**

```text
11/15
2/15
0.875
```

**Rationale:** `Fraction` keeps rational values exact through arithmetic and simplifies automatically. Converting to float gives an approximation suitable for display or interoperability.
