# Stub 1
# Given s = "Hello", "change" the character at index 1 from 'e' to 'a'
# by constructing a new string.
# Do NOT try s[1] = 'a' -- strings are immutable.
# Store the result in `modified`.
# Expected: "Hallo"

s = "Hello"
# Your code here:
modified = ...


# Stub 2
# Given s = "abcdef", "insert" the string "XY" between index 2 and 3
# (i.e., after 'c' and before 'd') by constructing a new string.
# Store the result in `inserted`.
# Expected: "abcXYdef"

s = "abcdef"
# Your code here:
inserted = ...


# --- Tests ---
# Do not modify below this line.

assert modified == "Hallo", \
    f"modified should be 'Hallo', got {modified!r}"

assert inserted == "abcXYdef", \
    f"inserted should be 'abcXYdef', got {inserted!r}"

# Verify the originals weren't somehow changed (they can't be, but
# this reinforces the concept)
assert "Hello"[1] == "e", \
    "String literals are immutable; 'Hello' hasn't changed"

print("All tests passed.")
