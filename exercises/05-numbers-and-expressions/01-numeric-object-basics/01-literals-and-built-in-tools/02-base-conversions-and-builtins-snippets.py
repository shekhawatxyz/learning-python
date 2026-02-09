# Step 2: Base conversions and built-ins
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: converting strings across bases and converting back to display forms.

bits = int("1010", 2)
octs = int("77", 8)
hexs = int("2a", 16)

print(bits, octs, hexs, bits + octs + hexs)
print(bin(hexs), oct(hexs), hex(hexs))

# Your answer:

# --- Snippet 2 ---
# Explores: floor-division identity with divmod, modular exponentiation,
# and rounding gotchas.

print(divmod(-29, 6))
print(pow(7, 5, 13))
print(round(1234.567, -2), round(2.675, 2))

# Your answer:
