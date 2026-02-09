# Step 3: Literal parsing and bit introspection
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: automatic base detection with int(..., 0) and underscore-friendly literals.

parts = ["0b1_010", "0o7_1", "0x2_A"]
parsed = [int(text, 0) for text in parts]

print(parsed)
print(sum(parsed), max(parsed) - min(parsed))

# Your answer:

# --- Snippet 2 ---
# Explores: complex construction, divmod reconstruction identity,
# and large modular exponentiation.

z = complex("3-4j")
q, r = divmod(-125, 16)

print(z, abs(z))
print(q, r, q * 16 + r)
print(pow(3, 40, 17))

# Your answer:
