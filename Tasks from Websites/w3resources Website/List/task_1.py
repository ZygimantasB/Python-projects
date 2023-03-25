# 1. Write a Python program to sum all the items in a list.

def sum_numbers_list(numbers):
    # return sum(numbers)
    # return sum(number for number in numbers)
    sum_number = 0
    for number in numbers:
        sum_number += number
    return sum_number


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum_numbers_list(sample_list))
