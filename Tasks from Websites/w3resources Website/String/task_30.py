# 30. Write a Python program to print the following numbers up to 2 decimal places.

def print_decimal_number(decimal_number: float):
    return '%.2f' % decimal_number, round(decimal_number, 2), decimal_number


print(print_decimal_number(7.777777))
print(print_decimal_number(7.88888888))
print(print_decimal_number(7.8051))
