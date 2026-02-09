# Step 6: Set and Boolean objects
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Build set-based summaries from two tag lists.
# 1) Convert to sets: unique_a, unique_b
# 2) Compute shared_tags and only_a
# 3) Build all_tags_sorted as a sorted list of the union

tags_a = ["python", "math", "debug", "python", "sets"]
tags_b = ["math", "testing", "python", "fractions"]

unique_a = ...
unique_b = ...
shared_tags = ...
only_a = ...
all_tags_sorted = ...


# --- Stub 2 ---
# Use frozenset for a permissions lookup and inspect truthiness.
# 1) role should come from permission_map for requested permissions
# 2) truth_pattern should be a list of bool(value) for each value
# 3) truth_count is number of True entries in truth_pattern
# 4) bool_sum should be True + True + False

permission_map = {
    frozenset({"read"}): "viewer",
    frozenset({"read", "write"}): "editor",
    frozenset({"read", "write", "delete"}): "admin",
}

requested = {"write", "read"}
values = [0, "", [], {}, None, 1, "ok", [1], True]

role = ...
truth_pattern = ...
truth_count = ...
bool_sum = ...


# --- Tests ---

assert unique_a == {"python", "math", "debug", "sets"}, (
    f"Expected unique_a to remove duplicates from tags_a, got {unique_a!r}."
)
assert unique_b == {"math", "testing", "python", "fractions"}, (
    f"Expected unique_b to remove duplicates from tags_b, got {unique_b!r}."
)
assert shared_tags == {"python", "math"}, (
    f"Expected shared_tags to be intersection {'python', 'math'}, got {shared_tags!r}."
)
assert only_a == {"debug", "sets"}, (
    f"Expected only_a to be tags only in A, got {only_a!r}."
)
assert all_tags_sorted == ["debug", "fractions", "math", "python", "sets", "testing"], (
    f"Expected sorted union list, got {all_tags_sorted!r}."
)

assert role == "editor", (
    f"Expected role to be 'editor', got {role!r}. "
    f"Use frozenset(requested) as the dict key."
)

assert truth_pattern == [False, False, False, False, False, True, True, True, True], (
    f"Expected truth_pattern based on bool() conversion, got {truth_pattern!r}."
)

assert truth_count == 4, (
    f"Expected truth_count to be 4, got {truth_count!r}."
)

assert bool_sum == 2, (
    f"Expected bool_sum to be 2, got {bool_sum!r}. "
    f"Booleans are subclasses of int."
)

print("All tests passed!")
