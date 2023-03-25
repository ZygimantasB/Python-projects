# Exercise 14: Reverse a given integer number
# Given:
#
# 76542
#
# Expected output:
#
# 24567

# number = 76542
# str_number = str(number)
# reverse_number = reversed(str_number)
# for i in reverse_number:
#     print(i, end='')


# def reverse_string(enter_number: int=123456):
#     enter_number = str(enter_number)
#     reverse_number = reversed(enter_number)
#     for i in reverse_number:
#         print(i, end='')


# reverse_string()

import copy



number = 76542
same_value = copy.deepcopy(number)
reversed_number = 0

while number > 0:
    reminder_number = number % 10
    reversed_number = reversed_number * 10 + reminder_number
    number = number // 10
print(reversed_number)

