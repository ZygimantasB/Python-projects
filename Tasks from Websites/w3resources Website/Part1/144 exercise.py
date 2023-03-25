# 144. Write a Python program to check whether variable is integer or string.

integer = 32
string = "32"
string1 = "Hello World"

print(f"integer: {type(integer)}")
print(f"string: {type(string)}")
print(f"string1: {type(string1)}")

try:
    integer = int(string1)
    print("This is a integer")
except ValueError:
    print("This is something else")
    pass


if isinstance(integer, int):
    print("This is a integer")
elif isinstance(integer, str):
    print("This is a string")
