# Step 2: append, pop, sort, reverse, insert
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: append, sort, reverse (all in-place), and pop

L = [3, 1, 4, 1, 5]
L.append(9)
print(L)
L.sort()
print(L)
L.reverse()
print(L)
print(L.pop())

# Your answer:

# --- Snippet 2 ---
# Explores: the return value of append (None!), insert positioning
# Key gotcha: in-place methods return None, not the modified list.

L = [10, 20, 30]
result = L.append(40)
print(result)
print(L)
L.insert(1, 15)
print(L)

# Your answer:
