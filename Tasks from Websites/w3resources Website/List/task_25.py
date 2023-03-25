# 25. Write a Python program to select an item randomly from a list.

from random import randint, choice


def random_number(user_list):
    random_index = randint(0, len(user_list) - 1)
    return user_list[random_index]


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(random_number(sample_list))


def random_choose(user_input):
    return choice(sample_list)


print(random_choose(sample_list))
