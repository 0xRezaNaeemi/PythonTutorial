x = 5
y = 5

print(x is y)  # x and y are the same
print(x == y)  # values of x and y are equal
print(id(x))
print(id(y))

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
print(x is y)  # x and y are the same
print(x == y)  # values of x and y are equal
print(id(x))
print(id(y))
print(x is not y)  # x and y are not the same

