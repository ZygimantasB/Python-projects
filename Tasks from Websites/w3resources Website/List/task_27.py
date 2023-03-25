# 27. Write a Python program to find the second smallest number in a list.

def second_smallest(user_input):
    return list(sorted([number for number in user_input]))[1]


sample_list = [7, 9, 11, 1, 2, 78, 45]

print(second_smallest(sample_list))


def second_small(user_input):
    smallest = min(user_input)
    new_list = [number for number in user_input if number != smallest]
    second_small_number = min(new_list)
    return second_small_number


print(second_small(sample_list))
