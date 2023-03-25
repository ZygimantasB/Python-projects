# Exercise 6: Delete a list of keys from a dictionary
# Given:
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# # Keys to remove
# keys = ["name", "salary"]
# Expected output:
#
# {'city': 'New york', 'age': 25}

from classes.tasks import DeleteListTask6

data_structure = DeleteListTask6()

print(data_structure.delete_items())
