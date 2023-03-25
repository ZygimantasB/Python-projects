# 30. Write a Python program that will accept the base and height of a triangle and compute the area.

a = int(input("Write a: "))
b = int(input("Write b: "))
height = int(input("Write h: "))
base = int(input("Write b: "))

diagonal_triangle = a * b

print(diagonal_triangle)

print("-" * 50)

area = 2 / (base * height)

print(area)

b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)