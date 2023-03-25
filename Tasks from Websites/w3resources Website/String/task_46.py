# 46. Write a Python program to convert a given string into a list of words.

def covert_to_list(user_input):
    return user_input.split()


input_string = 'The quick brown fox jumps over the lazy dog'

print(covert_to_list(input_string))

