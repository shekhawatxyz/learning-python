# Sets: Set Comprehensions and Practical Deduplication — Stubs

# --- Stub 1 ---
# Given the list `items` below, remove duplicates while preserving the order
# of first occurrence. Store the result in `unique_ordered` as a list.
#
# Hint: iterate through items, use a set to track what you've already seen,
# and build a list of items you haven't seen before.
#
# Expected: unique_ordered = [3, 1, 4, 5, 9, 2, 6]

items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Write your code here:



# --- Stub 2 ---
# Given two words below, check whether they are anagrams of each other.
# Two words are anagrams if they contain exactly the same letters with the
# same counts (e.g., "listen" and "silent").
#
# Store the boolean result in `are_anagrams`.
#
# Hint: sorting the letters of each word and comparing is the simplest
# approach at this point.
#
# Expected: are_anagrams = True

word1 = "listen"
word2 = "silent"

# Write your code here:



# --- Tests ---

# Tests for Stub 1
assert isinstance(unique_ordered, list), \
    f"Expected unique_ordered to be a list, got {type(unique_ordered).__name__}"
assert unique_ordered == [3, 1, 4, 5, 9, 2, 6], \
    f"Expected [3, 1, 4, 5, 9, 2, 6], got {unique_ordered}. " \
    f"Make sure you preserve the order of first occurrence."
# Verify no duplicates
assert len(unique_ordered) == len(set(unique_ordered)), \
    f"unique_ordered still contains duplicates: {unique_ordered}"

# Tests for Stub 2
assert isinstance(are_anagrams, bool), \
    f"Expected are_anagrams to be a bool, got {type(are_anagrams).__name__}"
assert are_anagrams is True, \
    f"Expected are_anagrams to be True for 'listen' and 'silent', got {are_anagrams}"

# Additional anagram checks to verify the logic is general
_test_word1, _test_word2 = "hello", "world"
_test_result = sorted(_test_word1) == sorted(_test_word2)
assert _test_result is False, \
    "Sanity check failed: 'hello' and 'world' should NOT be anagrams"

print("All tests passed!")
