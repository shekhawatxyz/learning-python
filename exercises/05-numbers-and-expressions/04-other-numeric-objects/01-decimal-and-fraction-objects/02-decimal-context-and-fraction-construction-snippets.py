# Step 2: Decimal context and Fraction construction
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: Decimal context precision and explicit quantization.

from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 4
x = Decimal("1") / Decimal("7")

print(x)
print(x.quantize(Decimal("0.000"), rounding=ROUND_HALF_UP))

# Your answer:

# --- Snippet 2 ---
# Explores: Fraction from exact inputs vs binary-float inputs.

from fractions import Fraction

print(Fraction(1, 10) + Fraction(2, 10))
print(Fraction(0.1))
print(Fraction("0.1"))

# Your answer:
