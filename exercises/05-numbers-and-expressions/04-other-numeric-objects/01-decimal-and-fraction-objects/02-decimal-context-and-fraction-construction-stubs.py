# Step 2: Decimal context and Fraction construction
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Use Decimal for a checkout computation:
# - subtotal = sum(prices)
# - after_discount = subtotal * (1 - discount)
# - total = after_discount * (1 + tax), quantized to cents
# - total_cents as int

from decimal import Decimal

prices = [Decimal("1.99"), Decimal("3.50"), Decimal("10.00")]
discount = Decimal("0.10")
tax = Decimal("0.07")

subtotal = ...
after_discount = ...
total = ...
total_cents = ...


# --- Stub 2 ---
# Scale a Fraction ratio and split into mixed-number components.
# - scaled = recipe_ratio * scale
# - whole_part and fractional_part
# - as_decimal rounded to 4 decimal places (float)

from fractions import Fraction

recipe_ratio = Fraction(5, 8)
scale = Fraction(9, 4)

scaled = ...
whole_part = ...
fractional_part = ...
as_decimal = ...


# --- Tests ---

assert subtotal == Decimal("15.49"), (
    f"Expected subtotal Decimal('15.49'), got {subtotal!r}."
)

assert after_discount == Decimal("13.941"), (
    f"Expected after_discount Decimal('13.941'), got {after_discount!r}."
)

assert total == Decimal("14.92"), (
    f"Expected total Decimal('14.92'), got {total!r}."
)

assert total_cents == 1492, (
    f"Expected total_cents 1492, got {total_cents!r}."
)

assert scaled == Fraction(45, 32), (
    f"Expected scaled Fraction(45, 32), got {scaled!r}."
)

assert whole_part == 1, (
    f"Expected whole_part 1, got {whole_part!r}."
)

assert fractional_part == Fraction(13, 32), (
    f"Expected fractional_part Fraction(13, 32), got {fractional_part!r}."
)

assert as_decimal == 1.4062, (
    f"Expected as_decimal 1.4062, got {as_decimal!r}."
)

print("All tests passed!")
