# Step 3: cmath and bit-level introspection
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: complex sqrt/exp/rect from cmath.

import cmath

z = -1 + 0j
print(cmath.sqrt(z))
print(cmath.exp(1j * cmath.pi))
print(cmath.rect(2, cmath.pi / 4))

# Your answer:

# --- Snippet 2 ---
# Explores: bit_length, bit_count, and lowest-set-bit trick.

n = 0b1111_0000_1010_0101
print(n.bit_length(), n.bit_count())
print(format(n, "016b"))
print(n & -n)

# Your answer:
