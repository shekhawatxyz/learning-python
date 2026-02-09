# Stub 1
# Given radius = 5, compute the area of a circle.
# Use the value 3.14159 for pi (no imports).
# Formula: area = pi * radius ** 2
# Store the result in `area`.

radius = 5
# Your code here:
area = 3.14159 * (radius**2)


# Stub 2
# Given temp_c = 37 (degrees Celsius), convert it to Fahrenheit.
# Formula: F = C * 9/5 + 32
# Store the result in `temp_f`.

temp_c = 37
# Your code here:
temp_f = (temp_c * (9 / 5)) + 32


# --- Tests ---
# Do not modify below this line.

assert isinstance(area, float), f"area should be a float, got {type(area).__name__}"
assert abs(area - 78.53975) < 0.0001, (
    f"area should be 78.53975 for radius=5, got {area}"
)

assert isinstance(temp_f, (int, float)), (
    f"temp_f should be a number, got {type(temp_f).__name__}"
)
assert abs(temp_f - 98.6) < 0.0001, f"temp_f should be 98.6 for temp_c=37, got {temp_f}"

print("All tests passed.")
