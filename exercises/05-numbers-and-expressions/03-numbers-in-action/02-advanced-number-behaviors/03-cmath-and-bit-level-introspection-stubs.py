# Step 3: cmath and bit-level introspection
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Implement flag helpers using bit masks.
# - grant(mask, flag): set a flag
# - revoke(mask, flag): clear a flag
# - has(mask, flag): True if set, else False

READ = 0b001
WRITE = 0b010
EXEC = 0b100


def grant(mask, flag):
    ...


def revoke(mask, flag):
    ...


def has(mask, flag):
    ...


mask = 0
mask = grant(mask, READ)
mask = grant(mask, EXEC)
mask = grant(mask, WRITE)
mask = revoke(mask, EXEC)

state = (
    has(mask, READ),
    has(mask, WRITE),
    has(mask, EXEC),
)


# --- Stub 2 ---
# Build a complex number from polar form and rotate it by 90 degrees.
# Compute:
# - z from cmath.rect(magnitude, angle)
# - real_imag_rounded as (real, imag) each rounded to 3
# - recon_polar = cmath.polar(z)
# - rotated = z * 1j
# - rotated_rounded as rounded (real, imag)

import cmath

magnitude = 5
angle = 0.9272952180016122

z = ...
real_imag_rounded = ...
recon_polar = ...
rotated = ...
rotated_rounded = ...


# --- Tests ---

assert mask == 0b011, (
    f"Expected mask to end at 0b011, got {bin(mask) if isinstance(mask, int) else mask!r}."
)

assert state == (True, True, False), (
    f"Expected state (True, True, False), got {state!r}."
)

assert real_imag_rounded == (3.0, 4.0), (
    f"Expected real_imag_rounded (3.0, 4.0), got {real_imag_rounded!r}."
)

assert abs(recon_polar[0] - 5.0) < 1e-12, (
    f"Expected polar radius near 5.0, got {recon_polar[0]!r}."
)

assert abs(recon_polar[1] - angle) < 1e-12, (
    f"Expected polar angle near {angle}, got {recon_polar[1]!r}."
)

assert rotated_rounded == (-4.0, 3.0), (
    f"Expected rotated_rounded (-4.0, 3.0), got {rotated_rounded!r}."
)

print("All tests passed!")
