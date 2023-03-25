# Exercise 9: Remove items from set1 that are not common to both set1 and set2
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
#
# {40, 50, 30}

from classes.tasks import RemoveCommonItemsTask9

data_structure = RemoveCommonItemsTask9()

print(data_structure.remove_common())

