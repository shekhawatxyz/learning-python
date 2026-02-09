# Step 4: Advanced number behaviors
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: complex numbers (parts, conjugate, magnitude, phase).

import cmath

z = 3 - 4j
print(z.real, z.imag)
print(z.conjugate())
print(abs(z))
print(round(cmath.phase(z), 3))

# Your answer:

# --- Snippet 2 ---
# Explores: base conversions, bitwise operators, underscore separators,
# and deterministic math/random calls.

import math
import random

value = 0b101101
mask = 0b001111

print(hex(value), oct(value), bin(value))
print(value & mask, value | mask, value ^ mask)

million = 1_000_000
print(million + 0x10)

random.seed(7)
print(random.randint(10, 20), round(math.sqrt(2), 4))

# Your answer:
