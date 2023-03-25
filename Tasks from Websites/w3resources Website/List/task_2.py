# 2. Write a Python program to multiply all the items in a list.

def multiply_numbers(numbers):
    return [number * 2 for number in numbers]


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(multiply_numbers(sample_list))
