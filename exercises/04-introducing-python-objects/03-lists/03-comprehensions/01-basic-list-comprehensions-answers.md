# Step 1: Basic list comprehensions — Answer Key

## Snippet 1

**Expected output:**

```
[0, 1, 4, 9, 16, 25]
['H', 'E', 'L', 'L', 'O']
```

**Rationale:**

- `[x ** 2 for x in range(6)]`: `range(6)` produces 0, 1, 2, 3, 4, 5. The comprehension squares each one, yielding `[0, 1, 4, 9, 16, 25]`. Note that `range(6)` starts at 0 and stops before 6.
- `[c.upper() for c in "hello"]`: iterating over a string yields individual characters. `.upper()` is called on each character, producing `['H', 'E', 'L', 'L', 'O']`. The result is a list of single-character strings, not a single string. A comprehension always produces a list.

## Snippet 2

**Expected output:**

```
[10, 20, 30, 40, 50]
[1, 2, 3, 4, 5]
15
```

**Rationale:**

- `[x * 10 for x in nums]`: multiplies each element by 10, producing `[10, 20, 30, 40, 50]`. The original list `nums` is not modified; a new list is created.
- `[x for x in nums]`: the identity comprehension. It creates a new list with the same elements as `nums`: `[1, 2, 3, 4, 5]`. This is effectively a copy of the list (similar to `nums[:]`).
- `sum([x for x in nums])`: the comprehension produces `[1, 2, 3, 4, 5]`, then `sum()` adds them up: `1 + 2 + 3 + 4 + 5 = 15`.
