# --- Snippet 1 ---
# Rebinding vs. in-place change with strings

a = "hello"
b = a
a = a.upper()
print(a)
print(b)

# Your answer:


# --- Snippet 2 ---
# Mutable (list) vs. immutable (string) behavior

list_a = [1, 2, 3]
list_b = list_a
list_a[0] = 99
print(list_a)
print(list_b)

str_a = "abc"
str_b = str_a
str_a = "xyz"
print(str_a)
print(str_b)

# Your answer:
