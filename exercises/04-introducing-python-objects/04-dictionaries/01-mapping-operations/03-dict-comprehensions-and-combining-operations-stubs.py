# Step 3: Dict comprehensions and combining operations — Stubs
# Dictionaries: comprehensions for mapping and filtering

# --- Stub 1 ---
# Given a list of words, create a dict mapping each word to its length
# using a dict comprehension. Store in `word_lengths`.

words = ["apple", "banana", "cherry", "avocado", "blueberry"]

# Write your code here:
word_lengths = None


# --- Stub 2 ---
# Part A: Given a list of words, create a frequency dict using a loop.
# Store in `freq`.
# Part B: Then, create a dict of only those words whose frequency is > 1,
# using a dict comprehension over `freq`. Store in `common`.

words = ["the", "cat", "sat", "on", "the", "mat", "the", "cat"]

# Write your code here:
freq = None
common = None


# --- Tests ---

# Tests for Stub 1
assert isinstance(word_lengths, dict), \
    f"Expected word_lengths to be a dict, got {type(word_lengths).__name__}"
assert word_lengths == {"apple": 5, "banana": 6, "cherry": 6, "avocado": 7, "blueberry": 9}, \
    f"Expected {{'apple': 5, 'banana': 6, 'cherry': 6, 'avocado': 7, 'blueberry': 9}}, got {word_lengths}"
assert word_lengths["blueberry"] == 9, \
    f"Expected 'blueberry' to map to 9, got {word_lengths.get('blueberry', 'key missing')}"
assert len(word_lengths) == 5, \
    f"Expected 5 entries, got {len(word_lengths)}"

# Tests for Stub 2 — freq
assert isinstance(freq, dict), \
    f"Expected freq to be a dict, got {type(freq).__name__}"
assert freq == {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}, \
    f"Expected {{'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}}, got {freq}"
assert freq["the"] == 3, \
    f"Expected 'the' to have frequency 3, got {freq.get('the', 'key missing')}"

# Tests for Stub 2 — common
assert isinstance(common, dict), \
    f"Expected common to be a dict, got {type(common).__name__}"
assert common == {"the": 3, "cat": 2}, \
    f"Expected {{'the': 3, 'cat': 2}}, got {common}"
assert "sat" not in common, \
    f"Expected 'sat' (frequency 1) to be excluded from common, but it was present"
assert len(common) == 2, \
    f"Expected 2 entries in common, got {len(common)}"

print("All tests passed!")
