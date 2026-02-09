# Step 1: Understanding Immutability — Answer Key

## Snippet 1

**Expected output:**
```
Hallo
Hello
HELLO
```

**Rationale:** `S[0] + "a" + S[2:]` builds a *new* string "Hallo" from "H" + "a" + "llo" and rebinds `S` to it. The original "Hello" object is not modified. This is demonstrated further: `original.upper()` returns a new string "HELLO" but `original` itself remains "Hello", proving that string methods do not mutate the string -- they return new strings.

## Snippet 2

**Expected output:**
```
spam
spam eggs
slam eggs
```

**Rationale:** First, S is "spam". Then `S = S + " eggs"` creates a new string "spam eggs" and rebinds S. Then `S = S[:1] + "l" + S[2:]` takes S[:1] which is "s", and S[2:] which is "am eggs", producing "s" + "l" + "am eggs" = "slam eggs". Each operation creates a new string object; the variable name `S` is simply rebound each time. No string object is ever modified in place.
