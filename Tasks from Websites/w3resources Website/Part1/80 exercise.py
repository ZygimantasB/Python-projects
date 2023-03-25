# 80. Write a Python program to get the current value of the recursion limit.

import sys

print("The current value of recursion limit: ")

recursion_limit = sys.getrecursionlimit()

print(recursion_limit)

# new_recursion_limit = sys.setrecursionlimit(5000)
#
# print(sys.getrecursionlimit())

print("Recursion limit")

