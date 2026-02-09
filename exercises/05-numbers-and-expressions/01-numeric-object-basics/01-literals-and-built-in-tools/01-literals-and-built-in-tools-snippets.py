# Step 1: Numeric literals and built-in tools
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: literal forms (decimal, binary, octal, hex, scientific notation, complex).

decimal_value = 42
binary_value = 0b101010
octal_value = 0o52
hex_value = 0x2A
scientific_value = 1.5e2
complex_value = 3 + 4j

print(decimal_value == binary_value == octal_value == hex_value)
print(scientific_value)
print(complex_value.real, complex_value.imag)

# Your answer:

# --- Snippet 2 ---
# Explores: constructors and core numeric helpers (int, float, complex, divmod, pow, round).

parsed_hex = int("ff", 16)
parsed_binary = int("1011", 2)
as_float = float("12.75")
as_complex = complex("2+5j")

print(parsed_hex + parsed_binary)
print(divmod(53, 7))
print(pow(2, 10), round(as_float), abs(as_complex))

# Your answer:
