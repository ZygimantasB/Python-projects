# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
#
# Given dictionary:
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# # Keys to extract
# keys = ["name", "salary"]

from classes.tasks import CreateDictionaryTask5

data_structure = CreateDictionaryTask5()

print(data_structure.create_dictionary())
