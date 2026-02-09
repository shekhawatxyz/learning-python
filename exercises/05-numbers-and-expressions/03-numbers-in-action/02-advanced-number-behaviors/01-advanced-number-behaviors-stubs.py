# Step 4: Advanced number behaviors
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Parse hex strings and apply bitwise operators.
# 1) Convert raw strings to integers.
# 2) Compute intersection (AND), union (OR), and toggled (XOR with toggle).
# 3) Store an 8-bit binary string representation of value in `as_binary`.

raw_value = "2d"    # 45
raw_mask = "0f"     # 15
raw_toggle = "30"   # 48

value = ...
mask = ...
toggle = ...

intersection = ...
union = ...
toggled = ...
as_binary = ...


# --- Stub 2 ---
# For complex number z = 5 - 12j, compute:
# - magnitude using abs
# - phase rounded to 3 decimals
# - polar tuple via cmath.polar
# Also seed RNG and generate 4 deterministic choices from the provided list.
# Compute `root_sum` as sqrt(9) + sqrt(16) + sqrt(25).

import cmath
import math
import random

z = 5 - 12j

magnitude = ...
phase = ...
polar = ...

random.seed(11)
samples = ...

root_sum = ...


# --- Tests ---

assert value == 45, (
    f"Expected value to be 45, got {value!r}. Use int(raw_value, 16)."
)
assert mask == 15, (
    f"Expected mask to be 15, got {mask!r}."
)
assert toggle == 48, (
    f"Expected toggle to be 48, got {toggle!r}."
)

assert intersection == 13, (
    f"Expected intersection (value & mask) to be 13, got {intersection!r}."
)
assert union == 47, (
    f"Expected union (value | mask) to be 47, got {union!r}."
)
assert toggled == 29, (
    f"Expected toggled (value ^ toggle) to be 29, got {toggled!r}."
)
assert as_binary == "00101101", (
    f"Expected as_binary to be '00101101', got {as_binary!r}. "
    f"Use format(value, '08b')."
)

assert magnitude == 13.0, (
    f"Expected magnitude to be 13.0, got {magnitude!r}."
)
assert phase == -1.176, (
    f"Expected phase to be -1.176, got {phase!r}. "
    f"Use round(cmath.phase(z), 3)."
)
assert isinstance(polar, tuple) and len(polar) == 2, (
    f"Expected polar to be a 2-item tuple, got {polar!r}."
)
assert abs(polar[0] - 13.0) < 1e-12, (
    f"Expected polar[0] to be 13.0, got {polar[0]!r}."
)
assert samples == [40, 40, 40, 20], (
    f"Expected deterministic samples [40, 40, 40, 20], got {samples!r}. "
    f"Use random.choice inside a loop/comprehension after random.seed(11)."
)
assert root_sum == 12.0, (
    f"Expected root_sum to be 12.0, got {root_sum!r}."
)

print("All tests passed!")
