# 21. Write a Python function to convert a given string
# to all uppercase if it contains at least 2 uppercase
# characters in the first 4 characters.

def convert_given_string(input_string):
    count_upper = sum(1 for char in input_string if char.isupper())
    return input_string.upper() if count_upper > 2 else input_string


print(convert_given_string("hEllo1_WORLD!"))
print(convert_given_string("hello world"))
print(convert_given_string("HEllo world"))
print(convert_given_string("HELlo world"))
