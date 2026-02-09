# Step 3: Dict comprehensions and combining operations — Answers

## Snippet 1

**Expected output:**
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
{'a': 1, 'b': 2, 'c': 3}
```

**Rationale:** The first comprehension `{x: x ** 2 for x in range(5)}` iterates over 0 through 4 and maps each number to its square. The second comprehension `{k: v for k, v in [("a", 1), ("b", 2), ("c", 3)]}` unpacks each 2-tuple from the list into `k` and `v`, building a dict from a list of pairs. This is a common pattern for converting a sequence of pairs into a dict (though `dict(...)` on the list would also work).

## Snippet 2

**Expected output:**
```
{'hello': 5, 'world': 5, 'python': 6}
{'b': 2, 'c': 3}
```

**Rationale:** The first comprehension maps each word to its length via `len(w)`: `"hello"` and `"world"` are both 5 characters, `"python"` is 6. The second comprehension iterates over the items of `{"a": 1, "b": 2, "c": 3}` but includes the `if v > 1` filter, so only pairs where the value exceeds 1 are kept. This excludes `"a": 1`, leaving `"b": 2` and `"c": 3`. The `if` clause in a dict comprehension works the same way as in a list comprehension — it filters which elements are included.
