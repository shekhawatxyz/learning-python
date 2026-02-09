# Step 2: Precedence and promotion
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: arithmetic + boolean precedence with comparisons.

x = 3

print(x + 2 * 5 > 12 and x**2 == 9)
print(not x == 4 and x < 10)

# Your answer:

# --- Snippet 2 ---
# Explores: mixed-type promotion and parenthesized grouping.

print(10 + 2.5 * 4)
print((10 + 2.5) * 4)
print(5 + 2j + 3.0)
print(type(5 + 2.0).__name__, type(5 + 2j).__name__)

# Your answer:
