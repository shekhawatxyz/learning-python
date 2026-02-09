# Step 1: Numeric literals and built-in tools
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Convert each value in `raw_values` to base-10 integers and compute the total.
# Store the final sum in `total_base10`.

raw_values = {
    "hex": "2f",    # base 16 -> 47
    "bin": "1101",  # base 2  -> 13
    "oct": "17",    # base 8  -> 15
}

total_base10 = ...


# --- Stub 2 ---
# Use divmod to split `distance_m` into chunks of size `chunk_size`.
# Store quotient in `chunks` and remainder in `leftover`.
# Then rebuild the original number in `rebuilt` and compute:
# - `rounded_km`: distance in kilometers rounded to 2 decimals
# - `power_check`: 2 raised to the power of `chunks`

distance_m = 987
chunk_size = 64

chunks = ...
leftover = ...
rebuilt = ...
rounded_km = ...
power_check = ...


# --- Tests ---

assert total_base10 == 75, (
    f"Expected total_base10 to be 75, got {total_base10!r}. "
    f"Use int(value, base) for each literal string."
)

assert (chunks, leftover) == (15, 27), (
    f"Expected (chunks, leftover) to be (15, 27), got {(chunks, leftover)!r}. "
    f"Use divmod(distance_m, chunk_size)."
)

assert rebuilt == distance_m, (
    f"Expected rebuilt == {distance_m}, got {rebuilt!r}. "
    f"Rebuild as chunks * chunk_size + leftover."
)

assert rounded_km == 0.99, (
    f"Expected rounded_km to be 0.99, got {rounded_km!r}. "
    f"Compute round(distance_m / 1000, 2)."
)

assert power_check == 32768, (
    f"Expected power_check to be 32768, got {power_check!r}. "
    f"Compute pow(2, chunks) or 2 ** chunks."
)

print("All tests passed!")
