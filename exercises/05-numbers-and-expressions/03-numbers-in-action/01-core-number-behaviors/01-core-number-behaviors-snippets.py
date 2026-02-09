# Step 3: Core number behaviors
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: variable-based expressions, display formatting, chained comparisons,
# and floating-point equality pitfalls.

price = 19.995
quantity = 3
subtotal = price * quantity

print(subtotal)
print(repr(subtotal))
print(format(subtotal, ".2f"))
print(10 < subtotal < 100)
print(0.1 + 0.2 == 0.3)

# Your answer:

# --- Snippet 2 ---
# Explores: true/floor division, modulus with negatives, and big-int precision.

print(11 / 4)
print(11 // 4, 11 % 4)
print(-11 // 4, -11 % 4)

huge_int = 2**120
print(huge_int > 10**30, len(str(huge_int)))

# Your answer:
