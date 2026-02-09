# Step 3: Floating-point robustness and big integers — Answer Key

## Snippet 1

**Expected output:**

```text
[2.67, 2.69, 2.69]
[Decimal('2.68'), Decimal('2.69'), Decimal('2.70')]
```

**Rationale:** Binary floats and decimal arithmetic round differently for some values. `Decimal` with explicit rounding mode gives precise, policy-controlled outcomes.

## Snippet 2

**Expected output:**

```text
51
True
True
201
```

**Rationale:** Python integers have arbitrary precision, so huge values compare and exponentiate directly. `bit_length` reports the number of bits needed for binary representation.
