# 10. Write a Python program to change a given string to a newly
# string where the first and last chars have been exchanged.

def change_symbols(entered_string):
    first_string = entered_string[0]
    last_string = entered_string[-1]
    middle_string = entered_string[1:-1]
    result = last_string + middle_string + first_string
    return result


print(change_symbols('google'))
print(change_symbols('microsoft'))
