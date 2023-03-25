# 109. Write a Python program to check if a number is positive, negative or zero.

number = int(input("Please enter the number: "))

if number < 0:
    print("Number are negative")
elif number == 0:
    print("Number are equal to zero")
elif number > 0:
    print("Number are positive")