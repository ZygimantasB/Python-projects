# Exercise 8: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.
#
# Given:
#
# sample_dict = {
#     "name": "Kelly",
#     "age":25,
#     "salary": 8000,
#     "city": "New york"
# }
# Expected output:
#
# {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}

from classes.tasks import RenameKeyTask8

data_structure = RenameKeyTask8()

print(data_structure.sample_dict)

