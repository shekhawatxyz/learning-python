# Step 3: Floating-point robustness and big integers
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: float rounding behavior vs Decimal half-up rounding.

from decimal import Decimal, ROUND_HALF_UP

amounts = [2.675, 2.685, 2.695]
print([round(x, 2) for x in amounts])

d_amounts = [Decimal("2.675"), Decimal("2.685"), Decimal("2.695")]
print([x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP) for x in d_amounts])

# Your answer:

# --- Snippet 2 ---
# Explores: huge integer comparisons and bit-level introspection.

n = 10**50 + 12345
print(len(str(n)))
print((10**30 + 1) > 10**30)
print((10**20) ** 2 == 10**40)
print((2**200).bit_length())

# Your answer:
