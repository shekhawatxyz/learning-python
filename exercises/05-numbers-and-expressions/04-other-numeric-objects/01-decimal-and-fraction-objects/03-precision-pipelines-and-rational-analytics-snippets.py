# Step 3: Precision pipelines and rational analytics
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: repeated float addition vs Decimal addition.

from decimal import Decimal

float_sum = 0.0
for _ in range(100):
    float_sum += 0.01
decimal_sum = sum([Decimal("0.01")] * 100)

print(float_sum == 1.0, decimal_sum == Decimal("1.00"))
print(round(float_sum, 20))

# Your answer:

# --- Snippet 2 ---
# Explores: rational approximation with limit_denominator.

from fractions import Fraction

pi_approx = Fraction(3.14159265).limit_denominator(1000)
print(pi_approx)
print(float(pi_approx))

# Your answer:
