# 11. Write a Python program to remove characters that
# have odd index values in a given string.

def remove_odd_index(enter_string):
    return enter_string[::2]


print(remove_odd_index('for google coming dark days'))
