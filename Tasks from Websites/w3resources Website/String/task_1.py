# 1. Write a Python program to calculate the length of a string.

def count_string_len(string_input):
    # return len(string_input)
    result = sum([1 for _ in string_input])
    return result


print(count_string_len('Hello World'))
