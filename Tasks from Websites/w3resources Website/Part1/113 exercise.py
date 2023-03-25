# 113. Write a Python program to input a number, if it is not a number generates an error message.

number = input("Please enter the number: ")

if isinstance(number, int):
    print(f"You entered the number {number}")
elif isinstance(number, str):
    print("You entered somthing else please enter the number")

try:
    number1 = int(input("Please enter the number: "))
    print(number1)
except ValueError:
    print("You entered something else")


if number.isdigit():
    print("You entered a number")
else:
    print("You entered something else")