# Step 2: Comprehensions with filtering
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Given `nums`, use a comprehension to get all numbers divisible by 3.
# Store in `div_by_3`.
# Expected: [3, 6, 9, 12, 15, 18]

nums = list(range(1, 21))

div_by_3 = ...  # replace ... with a list comprehension

# --- Stub 2 ---
# Given `words`, use a comprehension to get all words that:
#   - start with a lowercase letter, AND
#   - have more than 5 characters.
# Store in `result`.
# Expected: ["cherry", "elderberry"]

words = ["apple", "Banana", "cherry", "Date", "elderberry"]

result = ...  # replace ... with a list comprehension

# --- Tests ---

# Stub 1 tests
assert div_by_3 == [3, 6, 9, 12, 15, 18], (
    f"Expected div_by_3 to be [3, 6, 9, 12, 15, 18], got {div_by_3!r}. "
    f"Filter with 'if x % 3 == 0' in the comprehension."
)
assert isinstance(div_by_3, list), (
    f"Expected div_by_3 to be a list, got {type(div_by_3).__name__}."
)

# Stub 2 tests
assert result == ["cherry", "elderberry"], (
    f"Expected result to be ['cherry', 'elderberry'], got {result!r}. "
    f"Check two conditions: w[0].islower() and len(w) > 5. "
    f"'apple' has only 5 characters (not more than 5), so it should be excluded."
)
assert isinstance(result, list), (
    f"Expected result to be a list, got {type(result).__name__}."
)

# Edge case: make sure 'apple' (exactly 5 chars) is excluded
assert "apple" not in result, (
    f"'apple' should NOT be in result — it has exactly 5 characters, not more than 5."
)

# Edge case: make sure capitalized words are excluded
assert "Banana" not in result, (
    f"'Banana' should NOT be in result — it starts with an uppercase letter."
)

print("All tests passed!")
