# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

given_number = int(input("Please enter the number: "))

if given_number <= 17:
    print(17 - given_number)
elif given_number > 17:
    print(abs(17 - given_number) * 2)

# def difference(given_number):
#     if given_number <= 17:
#         return print(given_number - 17)
#     elif given_number > 17:
#         return print(abs((given_number - 17) * 2))
#
# given_number1 = int(input("Please enter the number: "))
#
# difference(given_number1)
