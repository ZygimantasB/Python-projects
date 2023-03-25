# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.

def nesat_list_split(user_input):
    return '\n'.join([' '.join(str(item) for item in sublist) for sublist in user_input])


sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nesat_list_split(sample_list))
