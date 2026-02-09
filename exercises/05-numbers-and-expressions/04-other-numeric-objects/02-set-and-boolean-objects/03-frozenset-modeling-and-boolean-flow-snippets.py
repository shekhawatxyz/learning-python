# Step 3: Frozenset modeling and boolean flow
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: undirected edge modeling with frozenset.

edges = {
    frozenset({"A", "B"}),
    frozenset({"B", "C"}),
    frozenset({"A", "C"}),
}

print(len(edges))
print(frozenset({"B", "A"}) in edges)
print(sorted("".join(sorted(edge)) for edge in edges))

# Your answer:

# --- Snippet 2 ---
# Explores: and/or short-circuit return values and bool arithmetic.

print([] or "fallback")
print("ok" and 123)
print(0 and 5, 0 or 5)
print(bool(2) + bool(-3) + bool(0))

# Your answer:
