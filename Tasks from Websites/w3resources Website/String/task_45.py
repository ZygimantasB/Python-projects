# 45. Write a Python program to check whether a string contains all letters of the alphabet.

def check_if_string_contains_letters(user_input):
    result = ['Word contains only alpha' if user_input.isalpha() else 'Not alpha']
    return result


print(check_if_string_contains_letters('alphabet'))
print(check_if_string_contains_letters('alphabet1'))
print(check_if_string_contains_letters('alphabet1.'))
print(check_if_string_contains_letters('alphabe'))
