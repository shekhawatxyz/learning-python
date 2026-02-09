# --- Snippet 1 ---
# find, replace, upper, lower

S = "Hello, World!"
print(S.find("World"))
print(S.find("xyz"))
print(S.replace("World", "Python"))
print(S.upper())
print(S.lower())

# Your answer:


# --- Snippet 2 ---
# strip variants, startswith, endswith, isalpha

S = "  Hello  "
print(repr(S.strip()))
print(repr(S.lstrip()))
print(repr(S.rstrip()))

T = "hello world"
print(T.startswith("hello"))
print(T.endswith("planet"))
print(T.isalpha())
print("hello".isalpha())

# Your answer:
