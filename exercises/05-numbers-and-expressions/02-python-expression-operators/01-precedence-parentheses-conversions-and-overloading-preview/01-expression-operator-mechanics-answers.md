# Step 2: Expression operator mechanics — Answer Key

## Snippet 1

**Expected output:**

```text
50
80
512
64
```

**Rationale:** `**` binds tighter than `*`, which binds tighter than `+`, so `2 + 3 * 4 ** 2` becomes `2 + 3 * 16`. Parentheses change grouping. Exponentiation is right-associative, so `2 ** 3 ** 2` is `2 ** (3 ** 2)`.

## Snippet 2

**Expected output:**

```text
Budget(1500)
Budget(2400)
7.5 (5+2.5j)
```

**Rationale:** The class overloads `+` and `*`, so numeric operators build new `Budget` objects. The final line shows numeric promotion rules: `int + float -> float`, and `int + complex -> complex`.
