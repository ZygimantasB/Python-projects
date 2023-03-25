# 20. Write a Python function to reverse a string
# if its length is a multiple of 4.

def reverse_string(enter_string):
    result = enter_string[::-1] if len(enter_string) % 4 == 0 else enter_string
    return result, len(enter_string)

    # if len(enter_string) % 4 == 0:
    #     return enter_string[::-1], len(enter_string)
    # else:
    #     return enter_string, len(enter_string)


print(reverse_string('Write'))
print(reverse_string('Python'))
print(reverse_string('function'))
print(reverse_string('reverse'))
print(reverse_string('string'))
print(reverse_string('abcd'))
