# Step 3: Frozenset modeling and boolean flow
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Compute tag-overlap recommendation scores.
# For each article, score = number of shared tags with user_tags.
# Then build `recommended` as article names with score > 0,
# sorted by (descending score, then article name).

user_tags = {"python", "math", "testing"}
articles = {
    "a-basics": {"python", "syntax"},
    "b-numerics": {"python", "math", "fractions"},
    "c-devops": {"docker", "linux"},
    "d-quality": {"testing", "python"},
}

scores = ...
recommended = ...


# --- Stub 2 ---
# Compute publishing gates:
# can_publish = is_author and (is_editor or has_approval) and not is_blocked
# priority = (is_urgent and can_publish) or is_editor
# signal_score = True/False arithmetic:
#   3*is_author + 2*is_editor + 2*has_approval + 1*is_urgent - 4*is_blocked

is_author = True
is_editor = False
has_approval = True
is_blocked = False
is_urgent = True

can_publish = ...
priority = ...
signal_score = ...


# --- Tests ---

assert scores == {
    "a-basics": 1,
    "b-numerics": 2,
    "c-devops": 0,
    "d-quality": 2,
}, (
    f"Unexpected scores: {scores!r}."
)

assert recommended == ["b-numerics", "d-quality", "a-basics"], (
    f"Expected recommended order ['b-numerics', 'd-quality', 'a-basics'], got {recommended!r}."
)

assert can_publish is True, (
    f"Expected can_publish True, got {can_publish!r}."
)

assert priority is True, (
    f"Expected priority True, got {priority!r}."
)

assert signal_score == 8, (
    f"Expected signal_score 8, got {signal_score!r}."
)

print("All tests passed!")
