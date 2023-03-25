# Exercise 6: Copy specific elements from one tuple to a new tuple
# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
#
# Given:
#
# tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:
#
# tuple2: (44, 55)


from classes.tasks import CopyFromAnotherTask6

data_structure = CopyFromAnotherTask6()

print(data_structure.copy_data())
