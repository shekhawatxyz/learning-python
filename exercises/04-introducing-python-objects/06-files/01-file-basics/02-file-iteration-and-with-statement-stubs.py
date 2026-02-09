# Files: File Iteration and the with Statement — Stubs

import os

# Set up the test data directory relative to this script's location
_dir = os.path.dirname(os.path.abspath(__file__))
_test_data = os.path.join(_dir, "_test_data")
os.makedirs(_test_data, exist_ok=True)

# --- Setup ---
# Create the test file needed for Stub 1
with open(os.path.join(_test_data, "snippet2.txt"), "w") as _f:
    _f.write("Line 1\n")
    _f.write("Line 2\n")
    _f.write("Line 3\n")


# --- Stub 1 ---
# Read the file `_test_data/snippet2.txt` (created above) and find the longest
# line, stripped of its trailing newline. Store it in `longest_line`.
# Use a `with` statement and iterate over the file object directly (for line in f).
#
# The file contains:
#   Line 1
#   Line 2
#   Line 3
# All three lines are the same length (6 characters), so `longest_line` should
# be whichever is found first: "Line 1".

filepath_snippet2 = os.path.join(_test_data, "snippet2.txt")

# Write your code here:



# --- Stub 2 ---
# Given the list `source_lines` below, create a file `_test_data/numbered.txt`
# where each line is prefixed with its line number (starting from 1), in the
# format: "N: text". For example: "1: hello", "2: world", "3: python".
# Each line should end with a newline in the file.
#
# Then read the file back and store the content as a list of stripped lines
# (no trailing newline) in `numbered`.
# Use `with` statements for both writing and reading.
#
# Expected: numbered = ["1: hello", "2: world", "3: python"]

source_lines = ["hello", "world", "python"]
filepath_numbered = os.path.join(_test_data, "numbered.txt")

# Write your code here:



# --- Tests ---

# Tests for Stub 1
assert isinstance(longest_line, str), \
    f"Expected longest_line to be a str, got {type(longest_line).__name__}"
assert longest_line == "Line 1", \
    f"Expected longest_line to be 'Line 1', got {longest_line!r}. " \
    f"Did you forget to strip the newline?"
assert "\n" not in longest_line, \
    f"longest_line should not contain a newline character. Got {longest_line!r}"

# Tests for Stub 2
assert isinstance(numbered, list), \
    f"Expected numbered to be a list, got {type(numbered).__name__}"
assert numbered == ["1: hello", "2: world", "3: python"], \
    f"Expected ['1: hello', '2: world', '3: python'], got {numbered}"

# Verify the file exists and has the right raw content
with open(filepath_numbered, "r") as _f:
    _raw = _f.read()
assert _raw == "1: hello\n2: world\n3: python\n", \
    f"File content doesn't match expected. Got {_raw!r}"

print("All tests passed!")
