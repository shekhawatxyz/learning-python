# Step 3: Nested comprehensions — Answer Key

## Snippet 1

**Expected output:**

```
[2, 5, 8]
[2, 4, 6, 8]
```

**Rationale:**

- `[M[row][1] for row in range(3)]`: iterates `row` over 0, 1, 2 and extracts column index 1 from each row. `M[0][1]` is 2, `M[1][1]` is 5, `M[2][1]` is 8. Result: `[2, 5, 8]`. This is the standard pattern for extracting a column from a matrix represented as a list of lists.

- `[M[row][col] for row in range(3) for col in range(3) if M[row][col] % 2 == 0]`: this has two `for` clauses, which means it iterates in a nested fashion — the outer loop is `row`, the inner loop is `col`. It visits every element in row-major order (row 0 col 0, row 0 col 1, ..., row 2 col 2) and keeps only those divisible by 2. The even elements in order are: 2 (row 0), 4, 6 (row 1), 8 (row 2). Result: `[2, 4, 6, 8]`. The two `for` clauses effectively flatten the matrix into a single iteration, and the `if` clause filters.

## Snippet 2

**Expected output:**

```
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
[1, 2, 3, 4, 5, 6]
```

**Rationale:**

- `[[i * j for j in range(1, 4)] for i in range(1, 4)]`: the outer comprehension iterates `i` over 1, 2, 3. For each `i`, the inner comprehension `[i * j for j in range(1, 4)]` produces a list. So:
  - `i=1`: `[1*1, 1*2, 1*3]` = `[1, 2, 3]`
  - `i=2`: `[2*1, 2*2, 2*3]` = `[2, 4, 6]`
  - `i=3`: `[3*1, 3*2, 3*3]` = `[3, 6, 9]`

  Result: `[[1, 2, 3], [2, 4, 6], [3, 6, 9]]`. This is a comprehension whose expression is itself a comprehension — it produces a list of lists. This is structurally different from a single comprehension with two `for` clauses.

- `[x for sublist in [[1, 2], [3, 4], [5, 6]] for x in sublist]`: this is the flattening pattern. The outer `for` iterates over sublists, the inner `for` iterates over elements within each sublist. The order of the `for` clauses reads left to right, matching how you would write nested `for` loops:
  ```
  for sublist in [[1,2],[3,4],[5,6]]:
      for x in sublist:
          result.append(x)
  ```
  Result: `[1, 2, 3, 4, 5, 6]`. This is the key distinction: a single comprehension with multiple `for` clauses produces a flat list, while a comprehension whose expression is another comprehension produces a nested list.
