# Exercise 11: Write a Program to extract each digit from an integer in
# the reverse order.

# For example, If the given int is 7536, the output shall be “6 3 5 7“,
# with a space separating the digits.

# number = input("Please enter the number: ")
#
# palindrome_number = number[::-1]
#
# for reverse_number in palindrome_number:
#     print(int(reverse_number), end=" ")

number1 = int(input("Please enter the number: "))
number_reminder = 0

while number1 != 0:
    number_reminder = number1 % 10
    number1 = number1 // 10
    print(number_reminder, end=" ")