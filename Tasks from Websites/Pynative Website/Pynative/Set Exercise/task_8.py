# Exercise 8: Update set1 by adding items from set2, except common items
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# Expected output:
#
# {70, 10, 20, 60}


from classes.tasks import UpdateListsTask8

data_structure = UpdateListsTask8()

print(data_structure.update_lists())
