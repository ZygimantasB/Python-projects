# 16. Write a Python program to generate and print a
# list of the first and last 5 elements where the values
# are square numbers between 1 and 30 (both included).

def print_list():
    full_list = [number ** 2 for number in range(1, 31)]
    result = full_list[:5] + full_list[-5:]
    return result


print(print_list())
