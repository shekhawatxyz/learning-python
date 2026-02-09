# Stub 1
# Given s = "Hello, World!", extract just the word "World" using slicing.
# Store the result in `extracted`.

s = "Hello, World!"
# Your code here:
extracted = ...


# Stub 2
# Given s = "stressed", produce "desserts" (the string reversed) using slicing.
# Store the result in `reversed_s`.

s = "stressed"
# Your code here:
reversed_s = ...


# --- Tests ---
# Do not modify below this line.

assert extracted == "World", \
    f"extracted should be 'World', got {extracted!r}"

assert reversed_s == "desserts", \
    f"reversed_s should be 'desserts', got {reversed_s!r}"

# Verify slicing was used (result is a string, not a list)
assert isinstance(extracted, str), \
    f"extracted should be a str, got {type(extracted).__name__}"
assert isinstance(reversed_s, str), \
    f"reversed_s should be a str, got {type(reversed_s).__name__}"

print("All tests passed.")
