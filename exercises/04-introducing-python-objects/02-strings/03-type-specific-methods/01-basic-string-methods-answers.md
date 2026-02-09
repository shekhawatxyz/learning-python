# Step 1: Basic String Methods — Answer Key

## Snippet 1

**Expected output:**
```
7
-1
Hello, Python!
HELLO, WORLD!
hello, world!
```

**Rationale:** `S.find("World")` returns 7, the index where "World" starts. `S.find("xyz")` returns -1 because the substring is not found (find returns -1 on failure, unlike index which raises an exception). `S.replace("World", "Python")` returns a new string with the substitution. `S.upper()` and `S.lower()` return new strings in the respective cases. None of these modify the original string S.

## Snippet 2

**Expected output:**
```
'Hello'
'Hello  '
'  Hello'
True
False
False
True
```

**Rationale:** `strip()` removes whitespace from both ends, `lstrip()` from the left only, `rstrip()` from the right only. `repr()` is used to make the remaining spaces visible in the output. `startswith("hello")` is True. `endswith("planet")` is False. `"hello world".isalpha()` is False because the space character is not alphabetic. `"hello".isalpha()` is True because all characters are letters.
