# Step 3: Literal parsing and bit introspection — Answer Key

## Snippet 1

**Expected output:**

```text
[10, 57, 42]
109 47
```

**Rationale:** `int(text, 0)` auto-detects base from prefixes (`0b`, `0o`, `0x`) and also accepts underscore separators. Aggregate operations (`sum`, `max`, `min`) then operate on parsed integers.

## Snippet 2

**Expected output:**

```text
(3-4j) 5.0
-8 3 -125
16
```

**Rationale:** `abs` on a complex number returns magnitude. `divmod` preserves reconstruction: `q * divisor + r == original`. Large modular powers can be computed directly with `pow(base, exp, mod)`.
