# Step 3: cmath and bit-level introspection — Answer Key

## Snippet 1

**Expected output:**

```text
1j
(-1+1.2246467991473532e-16j)
(1.4142135623730951+1.414213562373095j)
```

**Rationale:** `cmath` extends math operations to the complex plane. Some results include tiny floating-point residuals from trigonometric/exponential representation.

## Snippet 2

**Expected output:**

```text
16 8
1111000010100101
1
```

**Rationale:** `bit_length` and `bit_count` summarize binary representation size and density. `n & -n` isolates the least significant set bit.
