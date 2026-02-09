# Step 2: Mixed nesting and deeper access — Answer Key

## Snippet 1

**Expected output:**

```
Alice
95
91
A
```

**Rationale:**

- `record[0]` is `"Alice"` — the first element of the outer list, which happens to be a string.
- `record[1][0]` first gets `record[1]` which is the list `[95, 87, 91]`, then indexes at 0 to get `95`. The outer list holds heterogeneous types; the second element is itself a list.
- `record[1][-1]` gets the last element of `[95, 87, 91]`, which is `91`. Negative indexing works within the nested list.
- `record[2]["grade"]` first gets `record[2]` which is the dictionary `{"grade": "A"}`, then uses key-based access to get `"A"`. This previews dictionary access: you use the key in brackets rather than a numeric index. The outer list can hold any object type, including dictionaries.

## Snippet 2

**Expected output:**

```
3
6
2
2
2
```

**Rationale:**

- `grid[0][1][0]`: `grid[0]` is `[[1, 2], [3, 4]]`; then `[1]` gives `[3, 4]`; then `[0]` gives `3`. Triple indexing: each index peels away one layer of nesting.
- `grid[1][0][1]`: `grid[1]` is `[[5, 6], [7, 8]]`; then `[0]` gives `[5, 6]`; then `[1]` gives `6`.
- `len(grid)` is `2` — the outer list has 2 elements (each is a 2x2 "sub-grid").
- `len(grid[0])` is `2` — `grid[0]` is `[[1, 2], [3, 4]]`, which has 2 elements (rows).
- `len(grid[0][0])` is `2` — `grid[0][0]` is `[1, 2]`, which has 2 elements. `len()` always counts the elements at the level it is applied to; it does not recurse into nested structures.
