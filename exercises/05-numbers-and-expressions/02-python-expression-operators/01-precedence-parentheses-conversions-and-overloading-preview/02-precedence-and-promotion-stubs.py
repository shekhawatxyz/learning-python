# Step 2: Precedence and promotion
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Compute the following expression variants:
# - expr_default: a + b // c * 3
# - expr_grouped: (a + b) // c * 3
# - power_chain: 2 ** 3 ** 2
# - power_grouped: (2 ** 3) ** 2
# - comparison_result: a < b < (c + 10) and not (b == c)

a, b, c = 4, 7, 2

expr_default = ...
expr_grouped = ...
power_chain = ...
power_grouped = ...
comparison_result = ...


# --- Stub 2 ---
# Use overloaded operators on Meter objects.
# Compute:
# - total = road + extra
# - scaled = total * 1.5
# - average = scaled / 5
# - mixed = 10 + road


class Meter:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Meter):
            return Meter(self.value + other.value)
        return Meter(self.value + other)

    __radd__ = __add__

    def __mul__(self, factor):
        return Meter(self.value * factor)

    __rmul__ = __mul__

    def __truediv__(self, divisor):
        return Meter(self.value / divisor)

    def __repr__(self):
        return f"Meter({self.value})"


road = Meter(120)
extra = Meter(35)

total = ...
scaled = ...
average = ...
mixed = ...


# --- Tests ---

assert expr_default == 13, (
    f"Expected expr_default 13, got {expr_default!r}."
)

assert expr_grouped == 15, (
    f"Expected expr_grouped 15, got {expr_grouped!r}."
)

assert power_chain == 512, (
    f"Expected power_chain 512, got {power_chain!r}."
)

assert power_grouped == 64, (
    f"Expected power_grouped 64, got {power_grouped!r}."
)

assert comparison_result is True, (
    f"Expected comparison_result True, got {comparison_result!r}."
)

assert isinstance(total, Meter) and total.value == 155, (
    f"Expected total Meter(155), got {total!r}."
)

assert isinstance(scaled, Meter) and scaled.value == 232.5, (
    f"Expected scaled Meter(232.5), got {scaled!r}."
)

assert isinstance(average, Meter) and average.value == 46.5, (
    f"Expected average Meter(46.5), got {average!r}."
)

assert isinstance(mixed, Meter) and mixed.value == 130, (
    f"Expected mixed Meter(130), got {mixed!r}."
)

print("All tests passed!")
