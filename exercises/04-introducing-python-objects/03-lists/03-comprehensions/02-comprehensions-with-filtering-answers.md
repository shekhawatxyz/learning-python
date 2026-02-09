# Step 2: Comprehensions with filtering — Answer Key

## Snippet 1

**Expected output:**

```
[2, 4, 6, 8, 10]
[36, 49, 64, 81, 100]
```

**Rationale:**

- `[x for x in nums if x % 2 == 0]`: the `if` clause filters elements. Only those for which `x % 2 == 0` is true (even numbers) are included. Result: `[2, 4, 6, 8, 10]`. The expression part is just `x` (identity), so the even values pass through unchanged.
- `[x ** 2 for x in nums if x > 5]`: first filters to elements greater than 5 (6, 7, 8, 9, 10), then squares each. Result: `[36, 49, 64, 81, 100]`. The filter runs before the transformation: only elements passing the `if` test get the expression applied to them.

## Snippet 2

**Expected output:**

```
['Hello', 'world', 'Python', 'great']
['HELLO', 'PYTHON']
```

**Rationale:**

- `[w for w in words if len(w) > 4]`: filters to words longer than 4 characters. `"is"` has length 2, so it is excluded. All others ("Hello"=5, "world"=5, "Python"=6, "great"=5) pass. Result: `['Hello', 'world', 'Python', 'great']`. Note the condition is strictly greater than 4, not greater than or equal to 5 (which is the same thing numerically, but the conceptual framing matters).
- `[w.upper() for w in words if w[0].isupper()]`: filters to words whose first character is uppercase (`"Hello"` and `"Python"`), then applies `.upper()` to those. Result: `['HELLO', 'PYTHON']`. The filter checks the original word; the transformation produces the output. `"world"`, `"is"`, and `"great"` start with lowercase, so they are excluded before `.upper()` is ever applied to them.
