# Step 2: Bitmasks and complex operations
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Extract RGB channels from a 24-bit pixel and produce a darkened version.
# pixel format: 0xRRGGBB
# Darken by integer division by 3 for each channel, then repack.

pixel = 0x33CC99

r = ...
g = ...
b = ...

dark_r = ...
dark_g = ...
dark_b = ...

dark_pixel = ...


# --- Stub 2 ---
# For z1 and z2, compute:
# - sum_z
# - product_z
# - quotient_components as (real, imag) rounded to 3 decimals for z1 / z2
# - magnitude_ratio = abs(z2) / abs(z1), rounded to 3 decimals

z1 = 2 + 3j
z2 = -1 + 4j

sum_z = ...
product_z = ...
quotient_components = ...
magnitude_ratio = ...


# --- Tests ---

assert (r, g, b) == (51, 204, 153), (
    f"Expected channels (51, 204, 153), got {(r, g, b)!r}."
)

assert (dark_r, dark_g, dark_b) == (17, 68, 51), (
    f"Expected dark channels (17, 68, 51), got {(dark_r, dark_g, dark_b)!r}."
)

assert dark_pixel == 0x114433, (
    f"Expected dark_pixel 0x114433, got {hex(dark_pixel) if isinstance(dark_pixel, int) else dark_pixel!r}."
)

assert sum_z == (1 + 7j), (
    f"Expected sum_z (1+7j), got {sum_z!r}."
)

assert product_z == (-14 + 5j), (
    f"Expected product_z (-14+5j), got {product_z!r}."
)

assert quotient_components == (0.588, -0.647), (
    f"Expected quotient_components (0.588, -0.647), got {quotient_components!r}."
)

assert magnitude_ratio == 1.144, (
    f"Expected magnitude_ratio 1.144, got {magnitude_ratio!r}."
)

print("All tests passed!")
