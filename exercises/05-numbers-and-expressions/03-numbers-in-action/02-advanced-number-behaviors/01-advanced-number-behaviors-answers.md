# Step 4: Advanced number behaviors — Answer Key

## Snippet 1

**Expected output:**

```text
3.0 -4.0
(3+4j)
5.0
-0.927
```

**Rationale:** Complex numbers expose `.real` and `.imag`, `conjugate()` flips the imaginary sign, and `abs(z)` gives magnitude. `cmath.phase` returns the angle in radians.

## Snippet 2

**Expected output:**

```text
0x2d 0o55 0b101101
13 47 34
1000016
15 1.4142
```

**Rationale:** `hex`, `oct`, and `bin` format integers in different bases. Bitwise operators combine/manipulate bit patterns directly. Underscores in literals improve readability only; value is unchanged. With a fixed seed, `random.randint` is deterministic for reproducible exercises.
