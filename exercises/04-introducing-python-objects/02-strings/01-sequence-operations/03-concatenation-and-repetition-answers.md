# Step 3: Concatenation and Repetition — Answer Key

## Snippet 1

**Expected output:**
```
Hello World
HelloHelloHello
Hello! Hello!
```

**Rationale:** `a + " " + b` concatenates "Hello", " ", and "World". `a * 3` repeats "Hello" three times with no separator. `(a + "! ") * 2` first builds "Hello! " then repeats it twice, giving "Hello! Hello! " (note the trailing space).

## Snippet 2

**Expected output:**
```
python
--------------------
pn
```

**Rationale:** Concatenating the three list elements "py" + "th" + "on" gives "python". `"-" * 20` produces a string of 20 dashes. `result[0] + result[-1]` is "p" + "n" = "pn". This demonstrates that concatenation works on any string expressions, including those obtained by indexing, and that `*` with an integer repeats the string.
