# --- Snippet 1 ---
# split

S = "one,two,three"
print(S.split(","))
print(S.split(",", 1))
print("hello world".split())

# Your answer:


# --- Snippet 2 ---
# join and round-tripping with split

words = ["Hello", "World"]
print(" ".join(words))
print("-".join(words))
print("".join(words))

result = "a.b.c".split(".")
print(result)
print(".".join(result))

# Your answer:
