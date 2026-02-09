# Step 2: Multi-level nesting and traversal — Stubs
# Dictionaries: extracting from deep nesting and computing over lists of dicts

# --- Stub 1 ---
# Given the `config` dict below:
#   1. Extract the HTTPS port and store it in `https_port`.
#   2. Change the "debug" value to True (in place on the existing dict).

config = {
    "server": {
        "host": "localhost",
        "ports": {"http": 80, "https": 443}
    },
    "debug": False
}

# Write your code here:
https_port = None


# --- Stub 2 ---
# Given a list of student records (each with "name" and "scores"),
# compute the average score for each student.
# Store the result as a dict mapping each name to its average score.
# Store in `averages`.
# Use sum() and len() to compute averages.

students = [
    {"name": "Alice", "scores": [90, 85, 88]},
    {"name": "Bob", "scores": [72, 91, 84]},
    {"name": "Charlie", "scores": [95, 88, 92]}
]

# Write your code here:
averages = None


# --- Tests ---

# Tests for Stub 1
assert https_port == 443, \
    f"Expected https_port to be 443, got {https_port}"
assert config["debug"] is True, \
    f"Expected config['debug'] to be True after modification, got {config['debug']}"
assert config["server"]["host"] == "localhost", \
    f"Expected server host to remain 'localhost', got {config['server']['host']}"

# Tests for Stub 2
assert isinstance(averages, dict), \
    f"Expected averages to be a dict, got {type(averages).__name__}"
assert len(averages) == 3, \
    f"Expected 3 entries in averages, got {len(averages)}"

assert abs(averages["Alice"] - 87.6667) < 0.01, \
    f"Expected Alice's average to be ~87.67, got {averages.get('Alice', 'key missing')}"
assert abs(averages["Bob"] - 82.3333) < 0.01, \
    f"Expected Bob's average to be ~82.33, got {averages.get('Bob', 'key missing')}"
assert abs(averages["Charlie"] - 91.6667) < 0.01, \
    f"Expected Charlie's average to be ~91.67, got {averages.get('Charlie', 'key missing')}"

print("All tests passed!")
