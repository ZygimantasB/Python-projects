# Exercise 7: Checks if one set is a subset or superset of another set.
# If found, delete all elements from that set

from classes.all_task import DataStructureTask7

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

data_structure = DataStructureTask7(
    {27, 43, 34},
    {34, 93, 22, 27, 43, 53, 48}
).set_superset_issubset()
