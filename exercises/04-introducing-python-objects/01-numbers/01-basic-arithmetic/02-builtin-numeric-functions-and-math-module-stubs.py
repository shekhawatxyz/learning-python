import math

# Stub 1
# Given sides a=3 and b=4 of a right triangle,
# compute the hypotenuse c using math.sqrt.
# Formula: c = sqrt(a**2 + b**2)
# Store the result in `hypotenuse`.

a = 3
b = 4
# Your code here:
hypotenuse = ...


# Stub 2
# Given value = 3.456:
# 1. Round it to 2 decimal places. Store in `rounded_val`.
# 2. Compute math.floor of it. Store in `floored_val`.
# 3. Compute math.ceil of it. Store in `ceiled_val`.

value = 3.456
# Your code here:
rounded_val = ...
floored_val = ...
ceiled_val = ...


# --- Tests ---
# Do not modify below this line.

assert isinstance(hypotenuse, float), \
    f"hypotenuse should be a float (math.sqrt returns float), got {type(hypotenuse).__name__}"
assert abs(hypotenuse - 5.0) < 0.0001, \
    f"hypotenuse should be 5.0 for a 3-4-5 triangle, got {hypotenuse}"

assert rounded_val == 3.46, \
    f"rounded_val should be 3.46, got {rounded_val}"
assert floored_val == 3, \
    f"floored_val should be 3 (floor of 3.456), got {floored_val}"
assert isinstance(floored_val, int), \
    f"floored_val should be an int (math.floor returns int), got {type(floored_val).__name__}"
assert ceiled_val == 4, \
    f"ceiled_val should be 4 (ceil of 3.456), got {ceiled_val}"
assert isinstance(ceiled_val, int), \
    f"ceiled_val should be an int (math.ceil returns int), got {type(ceiled_val).__name__}"

print("All tests passed.")
