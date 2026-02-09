# Step 3: Literal parsing and bit introspection
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Parse all entries with int(text, 0) and compute:
# - `values`: parsed integers
# - `even_values`: only even parsed values
# - `weighted_sum`: sum((index+1) * value)
# - `as_binary_map`: dict mapping original literal text -> binary string

literals = ["0b1010", "0x1f", "0o77", "42", "1_000", "0xFF"]

values = ...
even_values = ...
weighted_sum = ...
as_binary_map = ...


# --- Stub 2 ---
# For n = 0xAB_CD, compute byte-level and bit-level properties:
# - high_byte and low_byte
# - repacked from bytes
# - one_count via bit_count
# - bit_width via bit_length

n = 0xAB_CD

high_byte = ...
low_byte = ...
repacked = ...
one_count = ...
bit_width = ...


# --- Tests ---

assert values == [10, 31, 63, 42, 1000, 255], (
    f"Expected values [10, 31, 63, 42, 1000, 255], got {values!r}."
)

assert even_values == [10, 42, 1000], (
    f"Expected even_values [10, 42, 1000], got {even_values!r}."
)

assert weighted_sum == 6959, (
    f"Expected weighted_sum 6959, got {weighted_sum!r}."
)

assert as_binary_map == {
    "0b1010": "0b1010",
    "0x1f": "0b11111",
    "0o77": "0b111111",
    "42": "0b101010",
    "1_000": "0b1111101000",
    "0xFF": "0b11111111",
}, (
    f"Unexpected as_binary_map: {as_binary_map!r}."
)

assert high_byte == 171, (
    f"Expected high_byte 171, got {high_byte!r}."
)

assert low_byte == 205, (
    f"Expected low_byte 205, got {low_byte!r}."
)

assert repacked == n, (
    f"Expected repacked == n ({n}), got {repacked!r}."
)

assert one_count == 10, (
    f"Expected one_count 10, got {one_count!r}."
)

assert bit_width == 16, (
    f"Expected bit_width 16, got {bit_width!r}."
)

print("All tests passed!")
