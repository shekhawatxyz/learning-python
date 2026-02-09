# Step 2: The get() method — Stubs
# Dictionaries: using .get() for safe access and accumulation

# --- Stub 1 ---
# Given an inventory dict and an item name, use .get() to retrieve the
# count of that item, defaulting to 0 if the item is not in the inventory.
# Store the result in `count`.

inventory = {"apples": 5, "bananas": 3}
item = "oranges"

# Write your code here:
count = None


# --- Stub 2 ---
# Given a list of color names, build a frequency dict counting how many
# times each color appears. Use .get() with a default of 0 (not the 'in'
# operator, not try/except). Store in `freq`.

words = ["red", "blue", "red", "green", "blue", "red"]

# Write your code here:
freq = None


# --- Tests ---

# Tests for Stub 1
assert count == 0, \
    f"Expected count to be 0 ('oranges' is not in inventory), got {count}"
assert isinstance(count, int), \
    f"Expected count to be an int, got {type(count).__name__}"

# Verify that .get() returns the real value for existing keys
assert inventory.get("apples", 0) == 5, \
    f"Sanity check: .get('apples', 0) should return 5, got {inventory.get('apples', 0)}"

# Tests for Stub 2
assert isinstance(freq, dict), \
    f"Expected freq to be a dict, got {type(freq).__name__}"
assert freq == {"red": 3, "blue": 2, "green": 1}, \
    f"Expected {{'red': 3, 'blue': 2, 'green': 1}}, got {freq}"
assert freq["red"] == 3, \
    f"Expected 'red' to have count 3, got {freq.get('red', 'key missing')}"
assert freq["blue"] == 2, \
    f"Expected 'blue' to have count 2, got {freq.get('blue', 'key missing')}"
assert freq["green"] == 1, \
    f"Expected 'green' to have count 1, got {freq.get('green', 'key missing')}"

print("All tests passed!")
