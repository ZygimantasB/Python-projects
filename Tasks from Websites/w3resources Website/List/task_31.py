# 31. Write a Python program to count
# the number of elements in a list
# within a specified range.

def elements_in_range(user_input):
    element_range = {number: user_input.count(number)
                     for number in user_input if number in range(1, 5)}
    return element_range


sample_list = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9]


print(elements_in_range(sample_list))
