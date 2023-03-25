# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# Given:

from classes.all_task import DataStructureTask6

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

data_structure = DataStructureTask6(
    {23, 42, 65, 57, 78, 83, 29},
    {57, 83, 29, 67, 73, 43, 48}
).unique_numbers_from_sets()
