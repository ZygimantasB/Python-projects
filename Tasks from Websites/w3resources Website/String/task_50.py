# 50. Write a Python program to split a string on the last occurrence of the delimiter.

def split_by_choose_string(user_input, delimiter):
    # result = ''.join([char[0] for char in user_input.split()])
    # return result
    index = user_input.rfind(delimiter)
    if index == -1:
        return user_input, ''
    return user_input[:index], user_input[index+len(delimiter):]


sample_string = 'Python,program'
print(split_by_choose_string(sample_string, ',+'))
