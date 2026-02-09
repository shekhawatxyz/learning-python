# Step 5: Decimal and Fraction objects
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Use Decimal for financial-style arithmetic.
# 1) subtotal = unit_price * quantity
# 2) discounted_subtotal = subtotal * (1 - discount_rate)
# 3) final_total = discounted_subtotal * (1 + tax_rate), quantized to cents
# 4) as_cents should be final_total in integer cents

from decimal import Decimal

unit_price = Decimal("3.45")
quantity = Decimal("7")
discount_rate = Decimal("0.075")
tax_rate = Decimal("0.12")

subtotal = ...
discounted_subtotal = ...
final_total = ...
as_cents = ...


# --- Stub 2 ---
# Use Fraction to scale a recipe exactly.
# A recipe uses 3/4 cup sugar for 6 servings.
# Compute sugar needed for 14 servings exactly as a Fraction.
# Then compute mixed-number parts:
# - whole_cups
# - remaining_fraction

from fractions import Fraction

base_sugar = Fraction(3, 4)
base_servings = 6
target_servings = 14

scaled_sugar = ...
whole_cups = ...
remaining_fraction = ...
as_float = ...


# --- Tests ---

assert subtotal == Decimal("24.15"), (
    f"Expected subtotal Decimal('24.15'), got {subtotal!r}."
)

assert discounted_subtotal == Decimal("22.33875"), (
    f"Expected discounted_subtotal Decimal('22.33875'), got {discounted_subtotal!r}."
)

assert final_total == Decimal("25.02"), (
    f"Expected final_total Decimal('25.02'), got {final_total!r}. "
    f"Quantize to cents with Decimal('0.01')."
)

assert as_cents == 2502, (
    f"Expected as_cents to be 2502, got {as_cents!r}."
)

assert scaled_sugar == Fraction(7, 4), (
    f"Expected scaled_sugar to be Fraction(7, 4), got {scaled_sugar!r}."
)

assert whole_cups == 1, (
    f"Expected whole_cups to be 1, got {whole_cups!r}."
)

assert remaining_fraction == Fraction(3, 4), (
    f"Expected remaining_fraction to be Fraction(3, 4), got {remaining_fraction!r}."
)

assert abs(as_float - 1.75) < 1e-12, (
    f"Expected as_float to be 1.75, got {as_float!r}."
)

print("All tests passed!")
