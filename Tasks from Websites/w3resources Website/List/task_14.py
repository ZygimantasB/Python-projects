# 14. Write a Python program to print the numbers of a
# specified list after removing even numbers from it.

def remove_even_number(user_input):
    odd_list = [number for number in user_input if number % 2 != 0]
    return odd_list


sample_list = [0, 1, 2, 3, 4, 56, 7, 8, 9, 10]

print(remove_even_number(sample_list))
