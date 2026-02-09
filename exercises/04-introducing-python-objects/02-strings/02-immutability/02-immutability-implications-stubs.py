# Stub 1
# Given s = "banana", replace ALL occurrences of 'a' with 'o'
# by iterating through the string and building a new string
# character by character.
# Store the result in `result`.
# Expected: "bonono"
# NOTE: Do NOT use s.replace() -- build the string manually
# to practice working with immutability.

s = "banana"
# Your code here:
result = ...


# Stub 2
# Given s = "Hello, World!", remove all characters that are NOT letters.
# No spaces, commas, exclamation marks, or other punctuation.
# Build a new string character by character.
# Use the .isalpha() method to check if a character is a letter.
# Store the result in `letters_only`.
# Expected: "HelloWorld"

s = "Hello, World!"
# Your code here:
letters_only = ...


# --- Tests ---
# Do not modify below this line.

assert result == "bonono", \
    f"result should be 'bonono', got {result!r}"
assert isinstance(result, str), \
    f"result should be a str, got {type(result).__name__}"

assert letters_only == "HelloWorld", \
    f"letters_only should be 'HelloWorld', got {letters_only!r}"
assert isinstance(letters_only, str), \
    f"letters_only should be a str, got {type(letters_only).__name__}"

# Verify original strings weren't changed (immutability)
assert s == "Hello, World!", \
    f"Original string s should still be 'Hello, World!', got {s!r}"

print("All tests passed.")
