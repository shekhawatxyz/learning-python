# --- Snippet 1 ---
# Building a new string instead of mutating

S = "Hello"
S = S[0] + "a" + S[2:]
print(S)

original = "Hello"
new = original.upper()
print(original)
print(new)

# Your answer:


# --- Snippet 2 ---
# Rebinding vs. mutating

S = "spam"
print(S)
S = S + " eggs"
print(S)
S = S[:1] + "l" + S[2:]
print(S)

# Your answer:
