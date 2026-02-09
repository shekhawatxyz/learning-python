# Step 2: Split and Join — Answer Key

## Snippet 1

**Expected output:**
```
['one', 'two', 'three']
['one', 'two,three']
['hello', 'world']
```

**Rationale:** `S.split(",")` splits on every comma, producing a 3-element list. `S.split(",", 1)` splits on at most 1 comma (the maxsplit argument), so it produces a 2-element list: everything before the first comma, and everything after. `"hello world".split()` with no argument splits on any whitespace (spaces, tabs, newlines) and also strips leading/trailing whitespace.

## Snippet 2

**Expected output:**
```
Hello World
Hello-World
HelloWorld
['a', 'b', 'c']
a.b.c
```

**Rationale:** `" ".join(words)` joins the list elements with a space separator. `"-".join(words)` uses a hyphen. `"".join(words)` concatenates with no separator. Splitting "a.b.c" on "." gives `['a', 'b', 'c']`, and joining that list back with "." reconstructs the original string. This split-then-join pattern is extremely common for transforming delimited data.
