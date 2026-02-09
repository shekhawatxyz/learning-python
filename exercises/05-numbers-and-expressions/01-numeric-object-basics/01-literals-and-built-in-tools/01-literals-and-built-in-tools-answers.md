# Step 1: Numeric literals and built-in tools — Answer Key

## Snippet 1

**Expected output:**

```text
True
150.0
3.0 4.0
```

**Rationale:** `42`, `0b101010`, `0o52`, and `0x2A` are the same integer in different literal forms, so the chained equality is `True`. Scientific notation `1.5e2` is `150.0`. Complex numbers expose floating-point parts via `.real` and `.imag`.

## Snippet 2

**Expected output:**

```text
266
(7, 4)
1024 13 5.385164807134504
```

**Rationale:** `int("ff", 16)` is 255 and `int("1011", 2)` is 11, so the sum is 266. `divmod(53, 7)` returns quotient and remainder `(7, 4)`. `pow(2, 10)` is 1024, `round(12.75)` is 13, and `abs(2+5j)` is the magnitude `sqrt(29)`.
