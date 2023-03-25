# 83. Write a Python program to test whether all numbers of a list is greater than a certain number.

list_check = [71, 87, 63, 69, 14, 20, 85, 74]

number = int(input("Please enter he number for check: "))

check_value = all(i > number for i in list_check)
print(check_value)