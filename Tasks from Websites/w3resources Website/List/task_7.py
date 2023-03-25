# 7. Write a Python program to remove duplicates from a list.

def remove_duplicates(user_input):
    # return set(user_input)
    unique_list = set()
    result = ([number for number in user_input if not (number in unique_list or
                                                       unique_list.add(
                                                           number))])
    return result


sample_list = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9]

print(remove_duplicates(sample_list))
