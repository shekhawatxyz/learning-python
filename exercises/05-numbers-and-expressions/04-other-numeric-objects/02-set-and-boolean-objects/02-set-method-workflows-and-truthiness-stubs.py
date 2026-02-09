# Step 2: Set method workflows and truthiness
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Compute skill summaries from person->skills mapping:
# - all_skills: union of all skill sets
# - shared_core: skills everyone has
# - only_ana: skills Ana has that Ben does not

profiles = {
    "ana": {"python", "sql", "git"},
    "ben": {"python", "excel"},
    "cia": {"python", "sql", "ml"},
}

all_skills = ...
shared_core = ...
only_ana = ...


# --- Stub 2 ---
# Build truthiness diagnostics for `values`:
# - truthy_values: original values where bool(value) is True
# - truth_table: list of (value, bool(value))
# - truthy_count
# - any_truthy and all_truthy
# - bool_sum = sum(bool(v) for v in values)

values = [0, 1, "", "ok", [], [0], {}, {"x": 1}, None, False, True]

truthy_values = ...
truth_table = ...
truthy_count = ...
any_truthy = ...
all_truthy = ...
bool_sum = ...


# --- Tests ---

assert all_skills == {"python", "sql", "git", "excel", "ml"}, (
    f"Expected all_skills union, got {all_skills!r}."
)

assert shared_core == {"python"}, (
    f"Expected shared_core {{'python'}}, got {shared_core!r}."
)

assert only_ana == {"git", "sql"}, (
    f"Expected only_ana {{'git', 'sql'}}, got {only_ana!r}."
)

assert truthy_values == [1, "ok", [0], {"x": 1}, True], (
    f"Unexpected truthy_values: {truthy_values!r}."
)

expected_truth_table = [
    (0, False),
    (1, True),
    ("", False),
    ("ok", True),
    ([], False),
    ([0], True),
    ({}, False),
    ({"x": 1}, True),
    (None, False),
    (False, False),
    (True, True),
]
assert truth_table == expected_truth_table, (
    f"Unexpected truth_table: {truth_table!r}."
)

assert truthy_count == 5, (
    f"Expected truthy_count 5, got {truthy_count!r}."
)

assert any_truthy is True, (
    f"Expected any_truthy True, got {any_truthy!r}."
)

assert all_truthy is False, (
    f"Expected all_truthy False, got {all_truthy!r}."
)

assert bool_sum == 5, (
    f"Expected bool_sum 5, got {bool_sum!r}."
)

print("All tests passed!")
