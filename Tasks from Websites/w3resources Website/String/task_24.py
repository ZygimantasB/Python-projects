# 24. Write a Python program to check whether a string starts with specified characters

def start_specific_character(user_input, specific_symbol):
    if user_input.startswith(specific_symbol):
        result = f'{user_input} starts with {specific_symbol}'
    else:
        result = f'User input {user_input} does`t start with {specific_symbol}'
    return result


print(start_specific_character('Google', 'asdf'))
print(start_specific_character('Google', 'G'))
print(start_specific_character('Google', 'o'))
print(start_specific_character('Google', 'o'))
print(start_specific_character('Google', 'g'))
print(start_specific_character('Google', 'l'))
print(start_specific_character('Google', 'e'))
