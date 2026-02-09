# Step 2: Decimal context and Fraction construction — Answer Key

## Snippet 1

**Expected output:**

```text
0.1429
0.143
```

**Rationale:** Decimal context precision controls arithmetic result precision. `quantize` applies explicit target precision and rounding mode.

## Snippet 2

**Expected output:**

```text
3/10
3602879701896397/36028797018963968
1/10
```

**Rationale:** Fractions built from exact rational/string inputs preserve intended values, while fractions built from binary floats preserve the float's exact binary value (which may look unexpected).
