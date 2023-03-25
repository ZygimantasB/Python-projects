# 115. Write a Python program to compute the product of a list of integers (without using for loop).

from functools import reduce
import math


def multiplay(a, b):
    return a * b


new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_value = 1

for i in new_list:
    new_value *= i
print(f"I used for -- {new_value} --")

try_reduce = reduce(multiplay, new_list)

print(f"I used only reduce method -- {try_reduce} --")

lambda_reduce = reduce(lambda a, b: a * b, new_list)
print(f"I used lambda + reduce -- {lambda_reduce} --")

math_prod = math.prod(new_list)
print(f"I used math module -- {math_prod} --")

