# Step 1: Basic list creation, indexing, slicing — Answer Key

## Snippet 1

**Expected output:**

```
1
5
[2, 3]
[5, 4, 3, 2, 1]
5
```

**Rationale:**

- `L[0]` gives the first element: `1`. Python uses zero-based indexing.
- `L[-1]` gives the last element: `5`. Negative indices count from the end.
- `L[1:3]` slices from index 1 up to but not including index 3: `[2, 3]`. The upper bound is exclusive.
- `L[::-1]` reverses the list by stepping backwards through it: `[5, 4, 3, 2, 1]`. The third component of a slice is the step; -1 means go right to left.
- `len(L)` returns the number of elements: `5`.

## Snippet 2

**Expected output:**

```
['a', 'b']
['c', 'd']
['a', 'b', 'c', 'd', 1, 2]
['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']
```

**Rationale:**

- `L[0:2]` slices from index 0 to 2 (exclusive): `['a', 'b']`.
- `L[-2:]` slices from the second-to-last element to the end: `['c', 'd']`. When the end is omitted, it defaults to the end of the list.
- `L + [1, 2]` concatenates L with `[1, 2]`, producing a new list: `['a', 'b', 'c', 'd', 1, 2]`. Lists can hold mixed types. Concatenation does not mutate L.
- `L * 2` repeats L twice: `['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd']`. Repetition produces a new list and does not mutate L.
