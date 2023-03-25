# 28. Write a Python program to find the second largest number in a list.

def second_largest(user_input):
    return list(sorted(number for number in user_input))[-2]


sample_list = [7, 9, 11, 1, 2, 78, 45]

print(second_largest(sample_list))


def sec_largest_num(user_input):
    largest_num = max(user_input)
    new_list = [number for number in user_input if number != largest_num]
    sec_largest = max(new_list)
    return sec_largest


print(sec_largest_num(sample_list))
