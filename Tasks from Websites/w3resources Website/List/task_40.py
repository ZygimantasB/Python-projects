# 39. Write a Python program to convert a
# list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

def one_integer(user_list):
    str_number = [str(number) for number in user_list]
    result = int(''.join(str_number))
    return result


sample_list = [11, 33, 50]

print(one_integer(sample_list))
