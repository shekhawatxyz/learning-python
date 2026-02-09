# Step 3: Core number behaviors
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Compute an order total and build a formatted summary string.
# 1) pre_tax_total = base_cost + shipping - discount
# 2) grand_total = pre_tax_total * (1 + tax_rate)
# 3) summary_line must be exactly: "total=$286.14"
# 4) within_budget should be True if grand_total <= budget

base_cost = 249.995
shipping = 12.5
discount = 20.0
tax_rate = 0.18
budget = 300.0

pre_tax_total = ...
grand_total = ...
summary_line = ...
within_budget = ...


# --- Stub 2 ---
# For integers `a` and `b`, compute:
# - true_div: a / b
# - floor_div: a // b
# - remainder: a % b
# - rebuild_ok: whether floor_div * b + remainder reconstructs a
# Also compute digit_count for huge_value = 10**80 + 1.

a, b = -73, 8

true_div = ...
floor_div = ...
remainder = ...
rebuild_ok = ...

huge_value = ...
digit_count = ...


# --- Tests ---

assert abs(pre_tax_total - 242.495) < 1e-12, (
    f"Expected pre_tax_total to be 242.495, got {pre_tax_total!r}."
)

assert abs(grand_total - 286.1441) < 1e-10, (
    f"Expected grand_total to be 286.1441, got {grand_total!r}."
)

assert summary_line == "total=$286.14", (
    f"Expected summary_line to be 'total=$286.14', got {summary_line!r}. "
    f"Use format(grand_total, '.2f') or an equivalent f-string format."
)

assert within_budget is True, (
    f"Expected within_budget to be True, got {within_budget!r}."
)

assert abs(true_div - (-9.125)) < 1e-12, (
    f"Expected true_div to be -9.125, got {true_div!r}."
)

assert floor_div == -10, (
    f"Expected floor_div to be -10, got {floor_div!r}. "
    f"Remember: // floors toward negative infinity."
)

assert remainder == 7, (
    f"Expected remainder to be 7, got {remainder!r}. "
    f"Python guarantees: a == (a // b) * b + (a % b)."
)

assert rebuild_ok is True, (
    f"Expected rebuild_ok to be True, got {rebuild_ok!r}."
)

assert huge_value == 10**80 + 1, (
    f"Expected huge_value to be 10**80 + 1, got {huge_value!r}."
)

assert digit_count == 81, (
    f"Expected digit_count to be 81, got {digit_count!r}. "
    f"Use len(str(huge_value))."
)

print("All tests passed!")
