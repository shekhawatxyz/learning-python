# Step 5: Decimal and Fraction objects
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: float precision vs Decimal exactness and decimal arithmetic.

from decimal import Decimal, getcontext

getcontext().prec = 6

print(0.1 + 0.1 + 0.1 == 0.3)
print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") == Decimal("0.3"))

price = Decimal("19.99")
tax_rate = Decimal("0.18")
print(price * (Decimal("1") + tax_rate))

# Your answer:

# --- Snippet 2 ---
# Explores: exact rational arithmetic with Fraction.

from fractions import Fraction

a = Fraction(1, 3)
b = Fraction("2/5")
c = Fraction(0.5)

print(a + b)
print(a * b)
print(float(Fraction(7, 8)))

# Your answer:
