# Step 1: Basic list creation, indexing, slicing
# Work through each snippet and predict the output before running.

# --- Snippet 1 ---
# Explores: list creation, positive/negative indexing, slicing, reverse, len

L = [1, 2, 3, 4, 5]
print(L[0])
print(L[-1])
print(L[1:3])
print(L[::-1])
print(len(L))

# Your answer:
# 1
# 5
# 2,3
# 5,4,3,2,1
# 5

# --- Snippet 2 ---
# Explores: slicing variants, negative-index slicing, concatenation, repetition

L = ["a", "b", "c", "d"]
print(L[0:2])
print(L[-2:])
print(L + [1, 2])
print(L * 2)

# Your answer:
# ["a","b"]
# ["c","d"]
# ['a','b','c','d',1,2]
# ["a","b","c","d","a","b","c","d"]
