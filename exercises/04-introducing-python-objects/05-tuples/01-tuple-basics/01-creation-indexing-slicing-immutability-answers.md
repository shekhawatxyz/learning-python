# Tuples: Creation, Indexing, Slicing, Immutability — Answers

## Snippet 1

**Expected output:**
```
1
5
(2, 3)
5
True
```

**Rationale:**
- `t[0]` returns the first element: `1`. Tuples are zero-indexed, just like lists and strings.
- `t[-1]` returns the last element: `5`. Negative indexing counts from the end.
- `t[1:3]` returns a slice from index 1 up to (but not including) index 3: `(2, 3)`. Slicing a tuple yields a new tuple.
- `len(t)` returns the number of elements: `5`.
- `3 in t` tests membership and returns `True` because 3 is one of the elements.

## Snippet 2

**Expected output:**
```
hello
3
<class 'tuple'>
(1, 'hello', [3, 4], 5, 6)
(1, 'hello', [3, 4], 1, 'hello', [3, 4])
```

**Rationale:**
- `t[1]` returns `"hello"`. Tuples can hold objects of any type, including strings.
- `t[2][0]` first indexes into the tuple to get `[3, 4]` (a list), then indexes into that list to get `3`. This is nested object access — the tuple holds a reference to the list.
- `type(t)` confirms the type is `<class 'tuple'>`.
- `t + (5, 6)` concatenates two tuples, producing a new tuple `(1, 'hello', [3, 4], 5, 6)`. Tuples support `+` for concatenation. The original `t` is unchanged (tuples are immutable).
- `t * 2` repeats the tuple, producing `(1, 'hello', [3, 4], 1, 'hello', [3, 4])`. Like concatenation, this creates a new tuple.
