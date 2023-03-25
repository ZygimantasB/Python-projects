# 31. Write a Python program to print the following numbers up to 2 decimal places with a sign.

def print_decimal_number(decimal_number: float):
    return f'>**< {"%.2f" % decimal_number}'


print(print_decimal_number(7.777777))
print(print_decimal_number(7.88888888))
print(print_decimal_number(7.8051))