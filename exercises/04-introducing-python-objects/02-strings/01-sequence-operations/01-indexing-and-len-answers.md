# Step 1: Indexing and len() — Answer Key

## Snippet 1

**Expected output:**
```
P
n
n
o
6
```

**Rationale:** `S[0]` is the first character 'P'. `S[5]` is the last character 'n' (indices 0-5 for a 6-character string). `S[-1]` also gives the last character 'n' (negative indexing counts from the end). `S[-2]` is 'o', the second-to-last. `len(S)` returns 6, the number of characters.

## Snippet 2

**Expected output:**
```
f
a
True
```

**Rationale:** `S[len(S) - 1]` is equivalent to `S[5]`, which is 'f' -- the last character. This is the manual way to get the last element; `S[-1]` is the Pythonic shorthand. `S[-len(S)]` is `S[-6]`, which wraps around to index 0, giving 'a' -- the first character. So `S[0] == S[-len(S)]` is `'a' == 'a'`, which is `True`. This demonstrates that negative indexing wraps around by exactly `len(S)`.
