# Step 3: Comparing approaches (in, get, try/except) — Answers

## Snippet 1

**Expected output:**
```
0
0
0
```

**Rationale:** All three approaches achieve the same result -- safely accessing a missing key `"b"` and falling back to `0`. Method (a) uses `"b" in d` to check before accessing; since `"b"` is not in `d`, the else branch sets `val = 0`. Method (b) uses `d.get("b", 0)`, which returns the default `0` directly because `"b"` is missing. Method (c) uses `try/except`: attempting `d["b"]` raises `KeyError`, which the `except` block catches, setting `val = 0`. All three print `0`. In practice, `.get()` is the most concise for simple defaults; `in` is clear when you need to do different things based on presence; `try/except` follows the "easier to ask forgiveness than permission" (EAFP) idiom and is preferred when the key is expected to exist most of the time.

## Snippet 2

**Expected output:**
```
N/A
90
0
```

**Rationale:** `d.get("email", "N/A")` returns `"N/A"` because `"email"` is not a key in `d`. `d.get("scores", [])[0]` first retrieves the existing `"scores"` list `[90, 85]`, then indexes `[0]` to get `90`. The default `[]` is never used here because the key exists. `d.get("missing", [0, 0])[1]` does not find `"missing"`, so it returns the default `[0, 0]`, then indexes `[1]` to get `0`. The key subtlety: the return value of `.get()` -- whether the real value or the default -- can be immediately operated on (indexed, called, etc.), which is a powerful and compact pattern. You must ensure the default is of a compatible type for whatever operation follows.
