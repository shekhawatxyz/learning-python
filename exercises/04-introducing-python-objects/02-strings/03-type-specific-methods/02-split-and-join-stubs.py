# Stub 1
# Given csv_line = "Alice,30,Engineer", split it into a list of fields
# using the comma as a delimiter.
# Store the result in `fields`.
# Expected: ['Alice', '30', 'Engineer']

csv_line = "Alice,30,Engineer"
# Your code here:
fields = ...


# Stub 2
# Given data = "one::two::three", convert it to "one--two--three"
# using split and join.
# Store the result in `converted`.

data = "one::two::three"
# Your code here:
converted = ...


# --- Tests ---
# Do not modify below this line.

assert fields == ['Alice', '30', 'Engineer'], \
    f"fields should be ['Alice', '30', 'Engineer'], got {fields!r}"
assert isinstance(fields, list), \
    f"fields should be a list, got {type(fields).__name__}"
assert len(fields) == 3, \
    f"fields should have 3 elements, got {len(fields)}"

assert converted == "one--two--three", \
    f"converted should be 'one--two--three', got {converted!r}"
assert isinstance(converted, str), \
    f"converted should be a str, got {type(converted).__name__}"

print("All tests passed.")
