# --- Snippet 1 ---
# Method chaining

S = "  Hello, World!  "
print(S.strip().lower().replace(",", "").replace("!", "").split())

# Your answer:
# ["hello","world"]

# --- Snippet 2 ---
# More chaining patterns

S = "Python Is Great"
print(S.lower().split())
print("-".join(S.lower().split()))
print(S.replace(" ", "_").lower())

# Your answer:
# ["python","is","great"]
# python-is-great
# python_is_great
