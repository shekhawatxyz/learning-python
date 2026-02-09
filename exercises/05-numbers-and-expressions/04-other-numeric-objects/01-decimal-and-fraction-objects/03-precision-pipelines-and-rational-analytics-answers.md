# Step 3: Precision pipelines and rational analytics — Answer Key

## Snippet 1

**Expected output:**

```text
False True
1.0000000000000007
```

**Rationale:** Repeated float addition accumulates binary representation error; Decimal addition on exact decimal strings preserves expected decimal arithmetic.

## Snippet 2

**Expected output:**

```text
355/113
3.1415929203539825
```

**Rationale:** `Fraction.limit_denominator` finds a close rational approximation with denominator bound. `355/113` is a classic high-quality approximation of pi.
