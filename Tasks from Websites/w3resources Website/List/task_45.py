# 45. Write a Python program to convert a pair of values into a sorted unique array.

values = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]

print(sorted(set().union(*values)))
