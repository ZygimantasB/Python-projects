# 60. Write a Python program to calculate the hypotenuse of a right angled triangle.

import math

a = int(input("Please enter a: "))
b = int(input("Please enter b: "))
c = int(input("Please enter c: "))

hypotenuse = math.sqrt(pow(a * b, 2) + pow(b * c, 2))

# hypotenuse1 = math.sqrt(((a * b) ** 2) + ((b * c) ** 2))

# print(hypotenuse1)

print(hypotenuse)


# print("Input lengths of shorter triangle sides:")
# a = float(input("a: "))
# b = float(input("b: "))
# c = sqrt(a**2 + b**2)
# print("The length of the hypotenuse is:", c )