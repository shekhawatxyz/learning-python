# Step 3: Chaining Methods and Combining — Answer Key

## Snippet 1

**Expected output:**
```
['hello', 'world']
```

**Rationale:** The chain works left to right. `S.strip()` yields `"Hello, World!"`. `.lower()` yields `"hello, world!"`. `.replace(",", "")` yields `"hello world!"`. `.replace("!", "")` yields `"hello world"`. `.split()` splits on whitespace, yielding `['hello', 'world']`. Each method returns a new string (or in the case of split, a list), and the next method call operates on that return value. This is possible because each intermediate result is itself a string with the same methods available.

## Snippet 2

**Expected output:**
```
['python', 'is', 'great']
python-is-great
python_is_great
```

**Rationale:** `S.lower().split()` lowercases then splits, giving a list of three words. `"-".join(S.lower().split())` takes that list and joins with hyphens, producing a slug-like string. `S.replace(" ", "_").lower()` first replaces spaces with underscores (giving "Python_Is_Great"), then lowercases (giving "python_is_great"). Note the order matters: replacing spaces before lowering vs. after gives the same result here, but the intermediate strings differ.
