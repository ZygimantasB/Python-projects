# 131. Write a Python program to split a variable length string into variables.

new_string = ["I want to learn Python"]

a, b, c = new_string + [None] * 2

print(a, b, c)

print("--Another solution--")

var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z)
var_list = [100, 20.25]
x, y = (var_list + [None] * 2)[:2]
print(x, y)

print("--Another solution--")

var_list = ['a', 'b', 'c', 'd', 'e']
v, w, x, y, z = var_list
print(v, w, x, y, z)
