# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

number = int(input("Please enter the number: "))

# if number % 2 == 0:
#     print("The number are even")
# elif number % 2 != 0:
#     print("The number are odd")

# else:
#     print("the number are odd")


def number_check(number1):
    if number1 % 2 == 0:
        return print("the number are even: ")
    elif number1 % 2 != 0:
        return print("Then number are odd: ")


print(number_check(number))

# not my solution

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")