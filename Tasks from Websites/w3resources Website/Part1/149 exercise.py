# 149. Write a Python function that takes a positive integer and
# returns the sum of the cube of all the positive integers smaller
# than the specified number.

# some_list = [7, 8, 9, 4, 5, 6]
#
# number1 = int(input("Please enter teh positive number: "))
#
# new_value = 0
#
# for i in some_list:
#     if i > number1:
#         new_value += i
# sum_cube = (new_value + new_value) ** 2
#
# print(sum_cube)

import math

print("\n --Another Solution-- \n")

number2 = float(input("Please enter the number: "))

sum_value = 0

infinity_value = math.inf

for i in range(0, 500):
    if i < number2:
        sum_value += i

sum_cube1 = sum_value ** 2


print(f"{sum_value} * {sum_value} = {sum_cube1}")