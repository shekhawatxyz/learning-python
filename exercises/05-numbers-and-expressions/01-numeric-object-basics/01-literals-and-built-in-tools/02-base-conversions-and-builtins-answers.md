# Step 2: Base conversions and built-ins — Answer Key

## Snippet 1

**Expected output:**

```text
10 63 42 115
0b101010 0o52 0x2a
```

**Rationale:** The same integer values can be parsed from strings in different bases with `int(text, base)`, and rendered back using `bin`, `oct`, and `hex`.

## Snippet 2

**Expected output:**

```text
(-5, 1)
11
1200.0 2.67
```

**Rationale:** `divmod` obeys floor-division semantics, even for negatives. Three-argument `pow` performs modular exponentiation efficiently. Rounding of binary floats can look surprising (`2.675` rounds to `2.67`).
