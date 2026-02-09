# Step 2: keys(), values(), items() and iteration — Answers

## Snippet 1

**Expected output:**
```
['a', 'b', 'c']
[1, 2, 3]
[('a', 1), ('b', 2), ('c', 3)]
['a', 'b', 'c']
```

**Rationale:** `d.keys()`, `d.values()`, and `d.items()` return view objects; wrapping them in `list()` produces a list. `.keys()` gives the keys, `.values()` gives the values, and `.items()` gives tuples of (key, value) pairs. `sorted(d.keys())` returns a new sorted list of the keys. Since Python 3.7+, dicts maintain insertion order, so the keys come out in the order they were defined: `"a"`, `"b"`, `"c"`. Here `sorted()` happens to produce the same order since the keys are already alphabetical.

## Snippet 2

**Expected output:**
```
x 10
y 20
z 30
x = 10
y = 20
z = 30
```

**Rationale:** The first loop (`for k in d`) iterates directly over the dict's keys. Inside the loop, `d[k]` is used to look up the corresponding value. The second loop (`for k, v in d.items()`) unpacks each (key, value) tuple from `.items()` into `k` and `v`, giving direct access to both without a separate lookup. Both approaches produce the same result; the `.items()` style is often preferred when you need both key and value. The f-string `f"{k} = {v}"` formats the output with the equals sign.
