# Step 3: Chaining and overload edge cases
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Compute each expression exactly as written.

x, y, z = 9, 4, 3

result1 = ...  # x + y * z ** 2
result2 = ...  # (x + y) * z ** 2
result3 = ...  # x // y + z % 2
logic = ...    # x > y and y > z or x == 0
bitwise = ...  # x ^ y & z
bitwise_grouped = ...  # (x ^ y) & z


# --- Stub 2 ---
# Use overloaded operators on Scalar objects.
# Compute:
# - hyp_sq = a**2 + b**2
# - scaled = 0.5 * hyp_sq
# - numeric = float(scaled) / 2
# - combined = 10 + a * 2


class Scalar:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Scalar):
            return Scalar(self.value + other.value)
        return Scalar(self.value + other)

    __radd__ = __add__

    def __mul__(self, factor):
        return Scalar(self.value * factor)

    __rmul__ = __mul__

    def __pow__(self, power):
        return Scalar(self.value**power)

    def __float__(self):
        return float(self.value)

    def __repr__(self):
        return f"Scalar({self.value})"


a = Scalar(3)
b = Scalar(4)

hyp_sq = ...
scaled = ...
numeric = ...
combined = ...


# --- Tests ---

assert result1 == 45, (
    f"Expected result1 45, got {result1!r}."
)

assert result2 == 117, (
    f"Expected result2 117, got {result2!r}."
)

assert result3 == 3, (
    f"Expected result3 3, got {result3!r}."
)

assert logic is True, (
    f"Expected logic True, got {logic!r}."
)

assert bitwise == 9, (
    f"Expected bitwise 9, got {bitwise!r}."
)

assert bitwise_grouped == 1, (
    f"Expected bitwise_grouped 1, got {bitwise_grouped!r}."
)

assert isinstance(hyp_sq, Scalar) and hyp_sq.value == 25, (
    f"Expected hyp_sq Scalar(25), got {hyp_sq!r}."
)

assert isinstance(scaled, Scalar) and scaled.value == 12.5, (
    f"Expected scaled Scalar(12.5), got {scaled!r}."
)

assert numeric == 6.25, (
    f"Expected numeric 6.25, got {numeric!r}."
)

assert isinstance(combined, Scalar) and combined.value == 16, (
    f"Expected combined Scalar(16), got {combined!r}."
)

print("All tests passed!")
