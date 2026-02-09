# Step 2: Immutability Implications — Answer Key

## Snippet 1

**Expected output:**
```
HELLO
hello
```

**Rationale:** `b = a` makes `b` reference the same string object "hello" as `a`. Then `a = a.upper()` creates a *new* string "HELLO" and rebinds `a` to it. The original "hello" object is untouched, and `b` still references it. This is the key consequence of immutability: operations on strings always produce new objects, so other references to the original are unaffected.

## Snippet 2

**Expected output:**
```
[99, 2, 3]
[99, 2, 3]
xyz
abc
```

**Rationale:** Lists are mutable. `list_b = list_a` makes both names reference the *same* list object. `list_a[0] = 99` mutates that shared object in place, so both `list_a` and `list_b` see the change. By contrast, strings are immutable. `str_b = str_a` makes both reference "abc", but `str_a = "xyz"` does not mutate "abc" -- it rebinds `str_a` to a completely new string object. `str_b` still references the original "abc". This is the fundamental mutable vs. immutable distinction.
