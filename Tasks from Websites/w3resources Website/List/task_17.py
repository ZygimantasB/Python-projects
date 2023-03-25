# 17. Write a Python program to generate and
# print a list except for the first
# 5 elements, where the values are square
# numbers between 1 and 30 (both included).

def first_five_missing():
    return [number ** 2 for number in range(1, 31)[5:]]


print(first_five_missing())
