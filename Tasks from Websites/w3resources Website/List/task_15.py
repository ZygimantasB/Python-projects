# 15. Write a Python program to shuffle and print a specified list.

from random import shuffle


def shuffle_list(user_input):
    shuffle(user_input)
    return user_input


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(shuffle_list(sample_list))

