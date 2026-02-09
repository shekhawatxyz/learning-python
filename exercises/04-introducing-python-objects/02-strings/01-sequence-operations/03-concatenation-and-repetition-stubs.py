# Stub 1
# Given name = "Alice", create a greeting string that says:
# "Hello, Alice! Hello, Alice! Hello, Alice!"
# Use concatenation to build "Hello, Alice! " and repetition to repeat it,
# then strip the trailing space.
# Store the result in `greeting`.

name = "Alice"
# Your code here:
greeting = ...


# Stub 2
# Given word = "abcd", create a string that is:
# the first character, then " - ", then the last character,
# then " - ", then the whole word reversed.
# Expected: "a - d - dcba"
# Store in `pattern`.

word = "abcd"
# Your code here:
pattern = ...


# --- Tests ---
# Do not modify below this line.

assert greeting == "Hello, Alice! Hello, Alice! Hello, Alice!", \
    f"greeting should be 'Hello, Alice! Hello, Alice! Hello, Alice!', got {greeting!r}"

assert pattern == "a - d - dcba", \
    f"pattern should be 'a - d - dcba', got {pattern!r}"

print("All tests passed.")
