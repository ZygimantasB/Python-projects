# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string,
# ignoring all other characters.

# str1 = "PYnative29@#8496"
#
# sum_digit = 0
# number_count = 0
#
# for number in str1:
#     if number.isdigit():
#         number_count += 1
#         sum_digit += int(number)
# print(f'Sum is: {sum_digit} Averange is: {sum_digit / number_count}')

import re

input_str = "PYnative29@#8496"

match = re.findall('tive', input_str)
print(match)


# digit_list = [int(num) for num in re.findall(r'\d', input_str)]
# print('Digits:', digit_list)
#
# # use the built-in function sum
# total = sum(digit_list)
#
# # average = sum / count of digits
# avg = total / len(digit_list)
# print("Sum is:", total, "Average is ", avg)


