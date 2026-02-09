# Step 1: Basic Arithmetic Operators — Answer Key

## Snippet 1

**Expected output:**
```
14
3
1
512
2
```

**Rationale:** `2 + 3 * 4` is 14 because `*` has higher precedence than `+`. `10 // 3` is 3 because `//` is floor division (truncates toward negative infinity, yielding an integer with integer operands). `10 % 3` is 1 (remainder). `2 ** 3 ** 2` is 512, not 64, because `**` is right-associative: it evaluates as `2 ** (3 ** 2)` = `2 ** 9` = 512. `7 - 2 * 3 + 1` is 2 because multiplication happens first (7 - 6 + 1), then left-to-right addition/subtraction.

## Snippet 2

**Expected output:**
```
5.0
3.3333333333333335
3
3.0
2.0
```

**Rationale:** `3 + 2.0` yields 5.0 because mixed int/float arithmetic promotes to float. `10 / 3` uses true division (always returns float in Python 3), giving approximately 3.333... `10 // 3` uses floor division with two ints, returning int 3. `10 // 3.0` uses floor division but with a float operand, so the result is float 3.0. `7 % 2.5` yields 2.0 because 2.5 * 2 = 5.0, and 7 - 5.0 = 2.0; the result is float because one operand is float.
