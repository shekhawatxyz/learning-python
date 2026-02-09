# Step 2: Slicing — Answer Key

## Snippet 1

**Expected output:**
```
Hello
World!
Hello
World!
```

**Rationale:** `S[0:5]` extracts characters at indices 0-4, giving "Hello". `S[7:]` extracts from index 7 to the end, giving "World!". `S[:5]` is shorthand for `S[0:5]`, giving "Hello". `S[-6:]` counts 6 back from the end: the string is 13 characters, so -6 maps to index 13-6 = 7, which is 'W'. So `S[-6:]` gives "World!" (the last 6 characters).

## Snippet 2

**Expected output:**
```
aceg
bdfh
hgfedcba
ce
```

**Rationale:** `S[::2]` takes every 2nd character starting from index 0: a, c, e, g. `S[1::2]` takes every 2nd character starting from index 1: b, d, f, h. `S[::-1]` reverses the string by stepping backwards. `S[2:6:2]` takes characters from index 2 to 5 (exclusive of 6) with step 2: index 2 is 'c', index 4 is 'e', giving "ce".
