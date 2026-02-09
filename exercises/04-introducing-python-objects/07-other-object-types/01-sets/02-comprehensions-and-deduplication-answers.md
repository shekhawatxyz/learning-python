# Sets: Set Comprehensions and Practical Deduplication — Answers

## Snippet 1

**Expected output (element order within sets may vary):**
```
{0, 1, 4, 9}
{'h', 'e', 'l', 'o', 'w', 'r', 'd'}
```

**Rationale:**
- `{x ** 2 for x in range(-3, 4)}` is a set comprehension. `range(-3, 4)` produces `-3, -2, -1, 0, 1, 2, 3`. Squaring these gives `9, 4, 1, 0, 1, 4, 9`. As a set, duplicates are removed, yielding `{0, 1, 4, 9}`. Note that `(-3)**2` and `3**2` both give `9`, `(-2)**2` and `2**2` both give `4`, etc. The set comprehension syntax `{expr for var in iterable}` mirrors list comprehension syntax `[expr for var in iterable]` but produces a set.
- `{c for c in "hello world" if c != " "}` iterates over each character in `"hello world"`, filters out spaces, and collects the rest into a set. The unique non-space characters are `{'h', 'e', 'l', 'o', 'w', 'r', 'd'}` (7 characters). The `l` appears three times in the source string but only once in the set. Display order is not guaranteed for characters.

## Snippet 2

**Expected output (first line order may vary):**
```
{'apple', 'banana', 'cherry'}
['apple', 'banana', 'cherry']
5 3
```

**Rationale:**
- `set(words)` converts the list to a set, removing duplicates. The unique words are `{'apple', 'banana', 'cherry'}`. Display order when printing the set directly is not guaranteed.
- `sorted(unique)` returns a new sorted list of the set's elements. Strings are sorted lexicographically (alphabetically), giving `['apple', 'banana', 'cherry']`. This output is deterministic because `sorted()` always returns a list in ascending order.
- `len(words)` is `5` (the original list has 5 elements including duplicates). `len(unique)` is `3` (only 3 distinct words). The `print` with two arguments separates them with a space: `5 3`.
