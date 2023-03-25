# 18. Write a Python function to get a string
# made of the first three characters of a
# specified string. If the length of the string
# is less than 3, return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt

def fixed_string(input_string):
    if len(input_string) <= 3:
        return input_string
    else:
        return input_string[:3]


print(fixed_string('ipy'))
print(fixed_string('python'))


def fixed_string_list_comprehension(input_string):
    result = input_string[:3] if len(input_string) > 3 else input_string
    return result


print(fixed_string_list_comprehension('ipy'))
print(fixed_string_list_comprehension('python'))
