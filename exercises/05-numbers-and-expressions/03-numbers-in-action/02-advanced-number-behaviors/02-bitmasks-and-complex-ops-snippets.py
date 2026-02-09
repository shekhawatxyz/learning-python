# Step 2: Bitmasks and complex operations
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: permission flags and bitmask checks.

READ = 0b001
WRITE = 0b010
EXEC = 0b100

perm = READ | EXEC
print(perm, bin(perm))
print(bool(perm & WRITE), bool(perm & EXEC))
print(perm ^ EXEC)

# Your answer:

# --- Snippet 2 ---
# Explores: bit shifts and bitwise inversion with masking.

value = 0b1101_0110
print(value >> 2)
print((value << 1) & 0xFF)
print((~value) & 0xFF)

# Your answer:
