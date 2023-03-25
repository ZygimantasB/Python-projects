# 44. Write a Python program to generate groups of five consecutive numbers in a list.

def enumerate_list():
    return [[5 * number + value for value in range(1, 6)] for number in range(5)]


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15]

print(enumerate_list())
