# 46. Write a Python program to select the odd items from a list.

def odd_numbers(my_list):
    return [number for number in my_list if number % 2 == 0]


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(odd_numbers(sample_list))
