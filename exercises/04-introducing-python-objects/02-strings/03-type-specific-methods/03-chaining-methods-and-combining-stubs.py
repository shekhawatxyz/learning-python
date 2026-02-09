# Stub 1
# Given raw = "  John   Doe  ", normalize it to "John Doe":
# - Strip outer whitespace
# - Collapse any inner whitespace to a single space
# - Ensure title case (first letter of each word capitalized)
# Hint: split() with no args handles multiple spaces; join reassembles.
# Store the result in `name`.
# Expected: "John Doe"

raw = "  John   Doe  "
# Your code here:
name = ...


# Stub 2
# Given sentence = "  the Quick BROWN fox  ", produce a URL "slug":
# - Strip leading/trailing whitespace
# - Convert to lowercase
# - Replace spaces with hyphens
# Store the result in `slug`.
# Expected: "the-quick-brown-fox"

sentence = "  the Quick BROWN fox  "
# Your code here:
slug = ...


# --- Tests ---
# Do not modify below this line.

assert name == "John Doe", \
    f"name should be 'John Doe', got {name!r}"

assert slug == "the-quick-brown-fox", \
    f"slug should be 'the-quick-brown-fox', got {slug!r}"

# Additional edge case tests
raw2 = "  jANE    sMITH  "
name2 = " ".join(raw2.split()).title()
assert name2 == "Jane Smith", \
    f"Normalization should work for 'jANE    sMITH' too, got {name2!r}"

sentence2 = "  Hello World  "
slug2 = "-".join(sentence2.strip().lower().split())
assert slug2 == "hello-world", \
    f"Slug should work for '  Hello World  ' too, got {slug2!r}"

print("All tests passed.")
