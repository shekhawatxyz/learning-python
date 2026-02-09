# Step 2: Built-in Numeric Functions and Math Module — Answer Key

## Snippet 1

**Expected output:**
```
7
3.6
2
1024
1
5
```

**Rationale:** `abs(-7)` returns 7. `round(3.567, 1)` rounds to 1 decimal place, giving 3.6. `round(2.5)` returns 2 (not 3) because Python uses banker's rounding (round half to even): since 2 is even, it rounds down. This is a common gotcha. `pow(2, 10)` is 1024. `min` and `max` return the smallest and largest of their arguments respectively.

## Snippet 2

**Expected output:**
```
12.0
3
4
6.283185307179586
```

**Rationale:** `math.sqrt(144)` returns 12.0 (a float, since sqrt always returns float). `math.floor(3.7)` returns 3 (an int in Python 3 -- math.floor and math.ceil return int, not float). `math.ceil(3.2)` returns 4. `math.pi * 2` computes 2*pi, approximately 6.283185307179586.
