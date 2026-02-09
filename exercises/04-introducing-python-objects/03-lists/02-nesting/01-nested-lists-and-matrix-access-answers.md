# Step 1: Nested lists and matrix access — Answer Key

## Snippet 1

**Expected output:**

```
[1, 2, 3]
6
9
10
```

**Rationale:**

- `M[0]` accesses the first element of the outer list, which is the sublist `[1, 2, 3]`. A "matrix" in Python is just a list of lists; `M[0]` gives the entire first row.
- `M[1][2]` first gets `M[1]` which is `[4, 5, 6]`, then indexes into it at position 2, giving `6`. Double indexing chains: the first index selects the row, the second selects the column within that row.
- `M[2][-1]` gets the last element of the third row `[7, 8, 9]`, which is `9`. Negative indexing works within nested lists just as it does in flat ones.
- `M[0][0] + M[2][2]` is `1 + 9 = 10`. You can use nested-indexed elements in expressions just like any other values.

## Snippet 2

**Expected output:**

```
['Bob', 85]
Bob
92
175
```

**Rationale:**

- `data[1]` returns the entire second record: `['Bob', 85]`. Each element of the outer list is itself a list representing a record.
- `data[1][0]` is `'Bob'` — the first element (name) of the second record.
- `data[2][1]` is `92` — the second element (score) of the third record ("Charlie").
- `data[0][1] + data[1][1]` is `90 + 85 = 175`. The scores (at index 1 within each record) are integers, so `+` performs arithmetic addition.
