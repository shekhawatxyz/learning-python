# Tuples: Records and Dictionary Keys — Answers

## Snippet 1

**Expected output:**
```
Alice
30
Engineer
2 1
```

**Rationale:**
- `name, age, role = record` unpacks the three-element tuple into three variables. This is tuple unpacking (also called sequence unpacking). The number of variables on the left must match the number of elements in the tuple.
- `print(name)` prints `Alice`, `print(age)` prints `30`, `print(role)` prints `Engineer`.
- `a, b = 1, 2` is itself tuple packing and unpacking: the right side `1, 2` creates a tuple `(1, 2)`, which is then unpacked into `a` and `b`.
- `a, b = b, a` swaps the values. Python evaluates the entire right side first (creating the tuple `(2, 1)`), then unpacks it. So `a` becomes `2` and `b` becomes `1`. This is the idiomatic Python swap — no temporary variable needed.
- `print(a, b)` prints `2 1`.

## Snippet 2

**Expected output:**
```
origin
True
[(1, 2), (2, 3), (3, 1)]
```

**Rationale:**
- Tuples can serve as dictionary keys because they are immutable (and thus hashable). Lists cannot be dictionary keys because they are mutable.
- `locations[(0, 0)]` retrieves the value `"origin"` associated with the key `(0, 0)`.
- `(1, 2) in locations` tests key membership and returns `True`.
- `coords.sort()` sorts the list of tuples in place. Tuples are compared element by element (lexicographic order): first by index 0, then by index 1 if index 0 is equal, and so on. So `(1, 2)` comes before `(2, 3)` which comes before `(3, 1)`.
