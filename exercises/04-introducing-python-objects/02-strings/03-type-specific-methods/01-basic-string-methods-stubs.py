# Stub 1
# Given raw_input = "  HeLLo WoRLd  ", clean it:
# strip leading/trailing whitespace, then convert to lowercase.
# Store the result in `cleaned`.
# Expected: "hello world"

raw_input = "  HeLLo WoRLd  "
# Your code here:
cleaned = ...


# Stub 2
# Given s = "my_variable_name", check if it contains only letters,
# digits, and underscores (valid Python identifier characters).
# Approach: replace underscores with "" to get just the letters/digits,
# then check .isalnum() on the result.
# Store the boolean in `is_valid`.
# Expected: True

s = "my_variable_name"
# Your code here:
is_valid = ...


# --- Tests ---
# Do not modify below this line.

assert cleaned == "hello world", \
    f"cleaned should be 'hello world', got {cleaned!r}"

assert isinstance(is_valid, bool), \
    f"is_valid should be a bool, got {type(is_valid).__name__}"
assert is_valid is True, \
    f"is_valid should be True for 'my_variable_name', got {is_valid}"

# Additional test: a string with invalid chars
s2 = "my-variable!"
is_valid2 = s2.replace("_", "").isalnum()
assert is_valid2 is False, \
    f"'my-variable!' should not be valid (contains '-' and '!'), got {is_valid2}"

print("All tests passed.")
