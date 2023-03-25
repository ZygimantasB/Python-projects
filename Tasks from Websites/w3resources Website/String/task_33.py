# 33. Write a Python program to print the following integers with zeros to the left of the specified width.


def print_decimal_number(decimal_number: float):
    return f'>**< {":0>6d" % decimal_number}'


print(print_decimal_number(7.777777))
print(print_decimal_number(7.88888888))
print(print_decimal_number(7.8051))
print(print_decimal_number(7.49))
print(print_decimal_number(7.501))
print(print_decimal_number(7.50))

