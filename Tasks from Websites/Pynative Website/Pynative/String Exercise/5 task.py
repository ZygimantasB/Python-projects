# Exercise 5: Count all letters, digits, and special symbols from a given string

def count_digit_symbol_char(string):
    count_digit = 0
    count_symbol = 0
    count_char = 0
    for checking_value in string:
        if checking_value.isalpha():
            count_char += 1
        elif checking_value.isdigit():
            count_digit += 1
        else:
            count_symbol += 1
    print(f'''Chars = {count_char}
Digits = {count_digit}
Symbol = {count_symbol}''')

str1 = "P@#yn26at^&i5ve"

count_digit_symbol_char(str1)

# count_digit = 0
# count_symbol = 0
# count_char = 0
# for i in str1:
#     if i in '1234567890':
#         count_digit += 1
#     elif i in ',./;"][/*-+!@#$%^&*()_-=+':
#         count_symbol += 1
#     else:
#         count_char += 1
#
# print(f'''Char = {count_char}
# Digits = {count_digit}
# Symbol = {count_symbol}''')
