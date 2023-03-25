# 21. Write a Python program to convert a list of characters into a string.

def convert_list_string(user_input):
    return ''.join(user_input)


sample_list = ['h', 'e', 'l', 'l', 'o']


print(convert_list_string(sample_list))
