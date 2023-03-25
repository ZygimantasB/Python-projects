# 23. Write a Python program to flatten a shallow list.
from itertools import chain


def flatten_shallow_list(user_list):
    return [number for item in user_list for number in item]


shallow_list = [[1, 2], [3, 4], [5, 6]]

print(flatten_shallow_list(shallow_list))


def chain_flatten_shallow_list(user_input):
    return list(chain(*user_input))


print(chain_flatten_shallow_list(shallow_list))
