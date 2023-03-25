# Exercise 3: Get Only unique items from two sets
# Write a Python program to return a new set with unique items from both sets by removing duplicates.
#
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
#
# {70, 40, 10, 50, 20, 60, 30}
# Note: set is unordered, so not necessary this will be the order of the item.


from classes.tasks import OnlyUniqueTask3

data_structure = OnlyUniqueTask3()

print(data_structure.unique_value())
