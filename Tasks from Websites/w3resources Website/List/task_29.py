# 29. Write a Python program to get unique values from a list.

def unique_values(user_input):
    return list(set(user_input))


sample_list = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9]

print(unique_values(sample_list))


def unique_values_num(user_input):
    new_list = []
    [new_list.append(number) for number in user_input if number not in new_list]
    return new_list


print(unique_values_num(sample_list))
