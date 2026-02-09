# Files: Basic Writing and Reading — Snippets

import os

# Set up the test data directory relative to this script's location
_dir = os.path.dirname(os.path.abspath(__file__))
_test_data = os.path.join(_dir, "_test_data")
os.makedirs(_test_data, exist_ok=True)

# --- Snippet 1 ---
# Writing to a file and reading it back with .read()

f = open(os.path.join(_test_data, "snippet1.txt"), "w")
f.write("Hello\n")
f.write("World\n")
f.close()

f = open(os.path.join(_test_data, "snippet1.txt"), "r")
content = f.read()
f.close()

print(repr(content))
print(content.split("\n"))

# Your answer:


# --- Snippet 2 ---
# Reading line by line with .readline() and reading all lines with .readlines()

f = open(os.path.join(_test_data, "snippet1.txt"), "r")
print(repr(f.readline()))
print(repr(f.readline()))
print(repr(f.readline()))
f.close()

f = open(os.path.join(_test_data, "snippet1.txt"), "r")
print(f.readlines())
f.close()

# Your answer:
