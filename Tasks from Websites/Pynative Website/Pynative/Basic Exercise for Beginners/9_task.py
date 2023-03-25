number1 = input("Please enter the number: ")

check_palindrome = str(number1[::-1])

if int(number1) == int(check_palindrome):
    print(f"Original number {number1}")
    print(f"Yes. given number is palindrome {int(check_palindrome)} number")
else:
    print(f"Original number {number1}")
    print(f"No. given number is not palindrome {int(check_palindrome)} number")

print("\n-------Another solution-------\n")

import copy  # Good idea <---------------------------------

number2 = int(input("Please enter the number: "))
original_number = copy.deepcopy(number2)  # Good idea <----
reversed_number = 0

while number2 != 0:
    number_reminder = number2 % 10
    reversed_number = reversed_number * 10 + number_reminder
    number2 //= 10

if number2 == reversed_number:
    print(f"Original number {original_number}")
    print(f"Yes. given number is palindrome {reversed_number} number")
else:
    print(f"Original number {original_number}")
    print(f"No. given number is not palindrome {reversed_number} number")
