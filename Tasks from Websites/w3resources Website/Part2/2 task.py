# 2. Write a Python program to create all possible strings
# by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import random


def shufle_list(a):
    random.shuffle(a)
    random_list = "".join(a)
    return print(random_list)


char_list = ['a', 'e', 'i', 'o', 'u']

shufle_list(char_list)