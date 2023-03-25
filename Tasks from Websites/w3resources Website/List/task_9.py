# 9. Write a Python program to clone or copy a list.

import copy

sample_list = [1, 2, 3, 4, 5, 67]

copy_list = copy.deepcopy(sample_list)
print(sample_list)
print(copy_list)