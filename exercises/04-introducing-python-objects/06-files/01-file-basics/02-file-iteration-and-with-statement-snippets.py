# Files: File Iteration and the with Statement — Snippets

import os

# Set up the test data directory relative to this script's location
_dir = os.path.dirname(os.path.abspath(__file__))
_test_data = os.path.join(_dir, "_test_data")
os.makedirs(_test_data, exist_ok=True)

# --- Snippet 1 ---
# Writing with a loop, then iterating over a file to find the longest line

with open(os.path.join(_test_data, "snippet2.txt"), "w") as f:
    for i in range(1, 4):
        f.write(f"Line {i}\n")

longest = ""
with open(os.path.join(_test_data, "snippet2.txt")) as f:
    for line in f:
        stripped = line.rstrip("\n")
        if len(stripped) > len(longest):
            longest = stripped

print(longest)
print(len(longest))

# Your answer:


# --- Snippet 2 ---
# The with statement ensures file closing

with open(os.path.join(_test_data, "snippet2.txt")) as f:
    lines = f.readlines()

print(lines)
print(f.closed)

# Your answer:
