# Files: Basic Writing and Reading — Stubs

import os

# Set up the test data directory relative to this script's location
_dir = os.path.dirname(os.path.abspath(__file__))
_test_data = os.path.join(_dir, "_test_data")
os.makedirs(_test_data, exist_ok=True)

# --- Stub 1 ---
# Write the list `lines` below to a file `_test_data/stub1.txt`, one line per
# element. Each line should end with a newline character in the file.
# Then read the file back and store the entire content as a single string
# in `content`.
#
# For example, the file should look like:
#   first line
#   second line
#   third line
# (each followed by a newline)

lines = ["first line", "second line", "third line"]
filepath_stub1 = os.path.join(_test_data, "stub1.txt")

# Write your code here:



# --- Stub 2 ---
# Read the file `_test_data/stub1.txt` (created in Stub 1 above) and count
# the number of lines. Store the count in `line_count`.
# Expected: 3

# Write your code here:



# --- Tests ---

# Tests for Stub 1
assert isinstance(content, str), \
    f"Expected content to be a str, got {type(content).__name__}"
assert content == "first line\nsecond line\nthird line\n", \
    f"Expected content to be 'first line\\nsecond line\\nthird line\\n', got {content!r}"

# Verify the file actually exists and has the right content
with open(filepath_stub1, "r") as _f:
    _check = _f.read()
assert _check == "first line\nsecond line\nthird line\n", \
    f"File content doesn't match. Got {_check!r}"

# Tests for Stub 2
assert line_count == 3, \
    f"Expected line_count to be 3, got {line_count}"

print("All tests passed!")
