# 19. Write a Python program to get the last part of a
# string before a specified character. Go to the editor
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

def print_last_part_string(input_string):
    result = input_string.rsplit('/', 1)[1] if len(input_string) > 1 \
        else input_string

    return result
    # split_string = input_string.rsplit('/', 1)
    # if len(split_string) > 1:
    #     return split_string[1]
    # else:
    #     return input_string



print(print_last_part_string('https://www.w3resource.com/python-exercises'))
print(print_last_part_string('https://www.w3resource.com/python'))
