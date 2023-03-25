# Exercise 7: Check if a value exists in a dictionary
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.
#
# Write a Python program to check if value 200 exists in the following dictionary.
#
# Given:
#
# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:
#
# 200 present in a dict

from classes.tasks import CheckIfExistsTask7

data_structure = CheckIfExistsTask7()

print(data_structure.check_if_exists())
