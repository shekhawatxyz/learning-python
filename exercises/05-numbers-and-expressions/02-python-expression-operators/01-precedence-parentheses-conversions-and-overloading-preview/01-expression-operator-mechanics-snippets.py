# Step 2: Expression operator mechanics
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: precedence, grouping with parentheses, and right-associativity of **.

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(2 ** 3 ** 2)
print((2 ** 3) ** 2)

# Your answer:

# --- Snippet 2 ---
# Explores: mixed-type promotion and a preview of operator overloading.


class Budget:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Budget):
            return Budget(self.amount + other.amount)
        return Budget(self.amount + other)

    __radd__ = __add__

    def __mul__(self, factor):
        return Budget(self.amount * factor)

    __rmul__ = __mul__

    def __repr__(self):
        return f"Budget({self.amount})"


monthly = Budget(1200)
print(monthly + 300)
print(2 * monthly)
print(5 + 2.5, 5 + 2.5j)

# Your answer:
