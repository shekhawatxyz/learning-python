# Step 2: Formatting, comparisons, and rounding
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: display formats and tolerance-based floating-point comparison.

import math

x = 1 / 3
print(x)
print(format(x, ".4f"))
print(f"{x:.2%}")
print(math.isclose(0.1 + 0.2, 0.3))

# Your answer:

# --- Snippet 2 ---
# Explores: round, floor, ceil, trunc, and min/max.

print(round(-12.75), math.floor(-12.75), math.ceil(-12.75), math.trunc(-12.75))
print(min(3, 7, -2), max(3, 7, -2))

# Your answer:
