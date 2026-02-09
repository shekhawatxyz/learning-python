# Step 2: The get() method — Answers

## Snippet 1

**Expected output:**
```
1
None
0
default
```

**Rationale:** `d.get("a")` finds key `"a"` and returns its value, `1`. `d.get("c")` does not find `"c"`, and since no default is specified, it returns `None`. `d.get("c", 0)` also does not find `"c"`, but this time a default of `0` is provided, so it returns `0`. `d.get("c", "default")` returns the string `"default"` for the same reason. The key insight: `.get()` never raises a `KeyError`. With one argument it returns `None` on a miss; with two arguments it returns the specified default. The dict itself is never modified by `.get()`.

## Snippet 2

**Expected output:**
```
{'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
```

**Rationale:** This is the classic `.get()`-based counting pattern. For each word `w`, `counts.get(w, 0)` returns the current count if the word has been seen before, or `0` if it has not. Adding `1` and assigning back to `counts[w]` either creates the key (with value 1) or increments it. Walking through: `"the"` starts at 0+1=1, `"cat"` at 0+1=1, `"sat"` at 0+1=1, `"on"` at 0+1=1, second `"the"` goes from 1+1=2, `"mat"` at 0+1=1. This is more concise than the `if key in d` pattern and is idiomatic Python.
