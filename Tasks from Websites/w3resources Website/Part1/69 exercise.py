# 69. Write a Python program to sort three integers without using conditional statements and loops.

number1 = int(input("Please enter the number 1: "))
number2 = int(input("Please enter the number 2: "))
number3 = int(input("Please enter the number 3: "))

min_number = min(number1, number2, number3)
max_number = max(number1, number2, number3)

mid_numbers = (number1 + number2 + number3) - min_number - max_number

print(f"All numbers are sorted: {min_number, mid_numbers, max_number}")

all_sorted = number1, number2, number3

sorted_numbers = sorted(all_sorted)

print(sorted_numbers)

