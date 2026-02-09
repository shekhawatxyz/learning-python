# Step 3: Chaining and overload edge cases
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: bitwise precedence and comparison chaining subtleties.

print(1 | 2 & 4, (1 | 2) & 4)
print(3 < 4 == 4 < 10)
print(3 < (4 == 4) < 10)

# Your answer:

# --- Snippet 2 ---
# Explores: overloaded operators plus precedence and grouping.


class Bucket:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Bucket):
            return Bucket(self.amount + other.amount)
        return Bucket(self.amount + other)

    __radd__ = __add__

    def __mul__(self, factor):
        return Bucket(self.amount * factor)

    __rmul__ = __mul__

    def __pow__(self, power):
        return Bucket(self.amount**power)

    def __repr__(self):
        return f"Bucket({self.amount})"


print(Bucket(2) + Bucket(3) * 4)
print((Bucket(2) + Bucket(3)) * 4)
print(2 + Bucket(5) ** 2)

# Your answer:
