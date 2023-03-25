# 4. Write a Python program to get the smallest number from a list.

def min_number(numbers):
    # return min(numbers)
    small_number = numbers[0]
    for number in numbers:
        if number < small_number:
            small_number = number
    return small_number


sample_list = [10, 9, 12, 85, 65, 32]

print(min_number(sample_list))
