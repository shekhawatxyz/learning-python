# Sets: Creation and Basic Operations — Answers

## Snippet 1

**Expected output:**
```
{1, 2, 3}
3
True
False
```

**Rationale:**
- `{1, 2, 3, 2, 1}` creates a set. Sets automatically discard duplicate elements, so the set contains only `{1, 2, 3}`. (Display order for small integers in CPython is typically sorted, so you will see `{1, 2, 3}`.)
- `len(s)` returns `3` because there are three unique elements.
- `2 in s` returns `True` because 2 is a member of the set.
- `5 in s` returns `False` because 5 is not in the set.
- Membership testing (`in`) on sets is very fast (O(1) on average) compared to lists (O(n)), because sets are implemented using hash tables.

## Snippet 2

**Expected output:**
```
{3, 4}
{1, 2, 3, 4, 5, 6}
{1, 2}
{5, 6}
{1, 2, 5, 6}
```

**Rationale:**
- `a & b` (intersection): elements in both `a` and `b` = `{3, 4}`.
- `a | b` (union): all elements in either `a` or `b` (or both) = `{1, 2, 3, 4, 5, 6}`.
- `a - b` (difference): elements in `a` but not in `b` = `{1, 2}`.
- `b - a` (difference): elements in `b` but not in `a` = `{5, 6}`. Note that set difference is not commutative.
- `a ^ b` (symmetric difference): elements in either `a` or `b` but not both = `{1, 2, 5, 6}`. This is equivalent to `(a | b) - (a & b)` or equivalently `(a - b) | (b - a)`.
