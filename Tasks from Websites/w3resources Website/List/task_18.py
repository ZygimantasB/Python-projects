# 18. Write a Python program to generate all permutations of a list in Python.

from itertools import permutations


def generate_permutations():
    return list(permutations([1, 2, 3]))


print(generate_permutations())


# def generate_permutations(lst):
#     if len(lst) == 0:
#         return [[]]
#     else:
#         result = []
#         for i in range(len(lst)):
#             rest = lst[:i] + lst[i+1:]
#             rest_permutations = generate_permutations(rest)
#             for perm in rest_permutations:
#                 result.append([lst[i]] + perm)
#         return result
#
# my_list = [1, 2, 3]
# permutations = generate_permutations(my_list)
# print(permutations)
