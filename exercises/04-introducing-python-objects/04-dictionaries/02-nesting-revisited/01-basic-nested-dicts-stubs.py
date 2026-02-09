# Step 1: Basic nested dicts — Stubs
# Dictionaries: constructing nested structures and mutating them in place

# --- Stub 1 ---
# Create a nested dict `student` with the following structure:
#   "name"    -> "Alice"
#   "grades"  -> a dict: {"math": 90, "english": 85, "science": 92}
#   "hobbies" -> a list: ["reading", "chess"]
# Then extract the science grade and store it in `sci_grade`.

# Write your code here:
student = None
sci_grade = None


# --- Stub 2 ---
# Given the dict `db` below, do two things (in place, modifying db directly):
#   1. Add a new score of 95 to alice's scores list.
#   2. Change bob's age to 26.
# Do NOT reassign db itself; modify the existing nested objects.

db = {
    "alice": {"age": 30, "scores": [90, 85]},
    "bob": {"age": 25, "scores": [88, 92]}
}

# Write your code here:


# --- Tests ---

# Tests for Stub 1
assert isinstance(student, dict), \
    f"Expected student to be a dict, got {type(student).__name__}"
assert student["name"] == "Alice", \
    f"Expected student['name'] to be 'Alice', got {student.get('name', 'key missing')}"
assert student["grades"] == {"math": 90, "english": 85, "science": 92}, \
    f"Expected grades dict with math/english/science, got {student.get('grades', 'key missing')}"
assert student["hobbies"] == ["reading", "chess"], \
    f"Expected hobbies ['reading', 'chess'], got {student.get('hobbies', 'key missing')}"
assert sci_grade == 92, \
    f"Expected sci_grade to be 92, got {sci_grade}"

# Tests for Stub 2
assert db["alice"]["scores"] == [90, 85, 95], \
    f"Expected alice's scores to be [90, 85, 95] after appending 95, got {db['alice']['scores']}"
assert len(db["alice"]["scores"]) == 3, \
    f"Expected alice to have 3 scores, got {len(db['alice']['scores'])}"
assert db["bob"]["age"] == 26, \
    f"Expected bob's age to be 26, got {db['bob']['age']}"
assert db["bob"]["scores"] == [88, 92], \
    f"Expected bob's scores to be unchanged at [88, 92], got {db['bob']['scores']}"

print("All tests passed!")
