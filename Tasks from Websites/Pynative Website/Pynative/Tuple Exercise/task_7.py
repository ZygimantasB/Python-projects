# Exercise 7: Modify the tuple
# Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
#
# Given:
#
# tuple1 = (11, [22, 33], 44, 55)
# Expected output:
#
# tuple1: (11, [222, 33], 44, 55)

from classes.tasks import ModifyTheTupleTask7

data_structure = ModifyTheTupleTask7()

print(data_structure.modify_tuple())
