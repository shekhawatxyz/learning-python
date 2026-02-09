# Step 2: Expression operator mechanics
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Compute the expression below in two ways:
# 1) using default precedence
# 2) using explicit parentheses to force a different grouping
# Then compute the absolute difference between the two results.

# default form: a + b * c ** d
# grouped form: ((a + b) * c) ** d

a, b, c, d = 5, 3, 2, 4

default_eval = ...
grouped_eval = ...
difference = ...


# --- Stub 2 ---
# Use the overloaded operators on Score objects to compute:
# - `team_total`: alice + bob
# - `boosted`: 3 * team_total
# - `mixed_number`: 2.5 + float(boosted)


class Score:
    def __init__(self, points):
        self.points = points

    def __add__(self, other):
        if isinstance(other, Score):
            return Score(self.points + other.points)
        return Score(self.points + other)

    __radd__ = __add__

    def __mul__(self, factor):
        return Score(self.points * factor)

    __rmul__ = __mul__

    def __float__(self):
        return float(self.points)

    def __repr__(self):
        return f"Score({self.points})"


alice = Score(18)
bob = Score(7)

team_total = ...
boosted = ...
mixed_number = ...


# --- Tests ---

assert default_eval == 53, (
    f"Expected default_eval to be 53, got {default_eval!r}. "
    f"Remember: ** first, then *, then +."
)

assert grouped_eval == 65536, (
    f"Expected grouped_eval to be 65536, got {grouped_eval!r}. "
    f"Apply the grouped form exactly: ((a + b) * c) ** d."
)

assert difference == 65483, (
    f"Expected difference to be 65483, got {difference!r}."
)

assert isinstance(team_total, Score), (
    f"Expected team_total to be a Score, got {type(team_total).__name__}."
)
assert team_total.points == 25, (
    f"Expected team_total.points to be 25, got {getattr(team_total, 'points', None)!r}."
)

assert isinstance(boosted, Score), (
    f"Expected boosted to be a Score, got {type(boosted).__name__}."
)
assert boosted.points == 75, (
    f"Expected boosted.points to be 75, got {getattr(boosted, 'points', None)!r}."
)

assert mixed_number == 77.5, (
    f"Expected mixed_number to be 77.5, got {mixed_number!r}. "
    f"Use float(boosted) to combine with 2.5."
)

print("All tests passed!")
