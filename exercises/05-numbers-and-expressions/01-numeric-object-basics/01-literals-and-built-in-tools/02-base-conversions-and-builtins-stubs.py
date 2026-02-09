# Step 2: Base conversions and built-ins
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Convert each (text, base) pair to an integer.
# Then compute:
# - `converted` list in the same order
# - `total` sum
# - `largest` max value
# - `largest_as_hex` via hex(largest)

raw_numbers = [
    ("101101", 2),
    ("71", 8),
    ("2f", 16),
    ("45", 10),
]

converted = ...
total = ...
largest = ...
largest_as_hex = ...


# --- Stub 2 ---
# Use built-ins to analyze integer division.
# For n=250 and d=17, compute:
# - quotient and remainder via divmod
# - `power_mod` = quotient**3 mod 10 using 3-arg pow
# - `rounded_ratio` = n/d rounded to 3 decimals
# - `reconstructed_ok` for q*d + r == n
# - `abs_offset` = abs(q*d - n)

n = 250
d = 17

quotient = ...
remainder = ...
power_mod = ...
rounded_ratio = ...
reconstructed_ok = ...
abs_offset = ...


# --- Tests ---

assert converted == [45, 57, 47, 45], (
    f"Expected converted to be [45, 57, 47, 45], got {converted!r}."
)

assert total == 194, (
    f"Expected total to be 194, got {total!r}."
)

assert largest == 57, (
    f"Expected largest to be 57, got {largest!r}."
)

assert largest_as_hex == "0x39", (
    f"Expected largest_as_hex to be '0x39', got {largest_as_hex!r}."
)

assert (quotient, remainder) == (14, 12), (
    f"Expected quotient/remainder to be (14, 12), got {(quotient, remainder)!r}."
)

assert power_mod == 4, (
    f"Expected power_mod to be 4, got {power_mod!r}."
)

assert rounded_ratio == 14.706, (
    f"Expected rounded_ratio to be 14.706, got {rounded_ratio!r}."
)

assert reconstructed_ok is True, (
    f"Expected reconstructed_ok to be True, got {reconstructed_ok!r}."
)

assert abs_offset == 12, (
    f"Expected abs_offset to be 12, got {abs_offset!r}."
)

print("All tests passed!")
