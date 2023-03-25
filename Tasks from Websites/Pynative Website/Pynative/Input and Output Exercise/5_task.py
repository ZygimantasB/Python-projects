# Exercise 5: Accept a list of 5 float numbers as an input from the user
# Refer:
#
# Take list as a input in Python.
# Python list
# Expected Output:
#
# [78.6, 78.6, 85.3, 1.2, 3.5]

empty_list = []
list_long = int(input("How long list of decimals should be: "))

for adding in range(list_long):
    add_float = float(input("Please enter a float number: "))
    empty_list.append(add_float)
print(empty_list)
