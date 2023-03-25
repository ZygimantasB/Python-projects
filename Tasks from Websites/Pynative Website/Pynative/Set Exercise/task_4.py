# Exercise 5: Remove items from the set at once
# Write a Python program to remove items 10, 20, 30 from the following set at once.
#
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# Expected output:
#
# {40, 50}

from classes.tasks import RemoveItemsTask4

data_structure = RemoveItemsTask4()

print(data_structure.remove_items())
