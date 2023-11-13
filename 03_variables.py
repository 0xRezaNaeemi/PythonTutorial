a = b = c = 10
print(a, b, c)

a, b, c = 2, 3, 5
print(a, b, c)

a, b = 5, 4
a, b = b, a
print(a, b)

print(id(a))
print(id(b))
