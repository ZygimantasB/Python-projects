# 125. Write a Python program to sum of all counts in a collections
import collections

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# values_count = len(new_list)
sum_count = sum(collections.Counter(new_list).values())

# print(values_count)
print(sum_count)