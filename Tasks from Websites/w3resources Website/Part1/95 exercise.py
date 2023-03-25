# 95. Write a Python program to check whether a string is numeric.

# a = "abc"
a = 8

# print(a.isnumeric())
#
# print(a.isdigit())
#
# print(isinstance(a, str))

# if a.isnumeric():
if isinstance(a, int):
    print("Its a number")
elif isinstance(a, str):
    print("Its a string")
else:
    print("Its something else")


str = 'a123'
#str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()

# Doesn't work for floats
text = input("Input a word or numbers: ")
if text.isdigit():
    print("The input value is numbers.")
else:
    print("The input value is string.")
