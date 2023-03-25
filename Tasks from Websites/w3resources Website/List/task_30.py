# 30. Write a Python program to get the frequency of elements in a list.
import collections


def frequency_elements(user_input):
    # frequency_dict = {}
    # for number in user_input:
    #     if number in frequency_dict:
    #         frequency_dict[number] += 1
    #     else:
    #         frequency_dict[number] = 1
    # return frequency_dict
    frequency_dict = {number: user_input.count(number) for number in user_input}
    return frequency_dict


sample_list = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9]

print(frequency_elements(sample_list))

print(collections.Counter(sample_list))
