# 9. Write a Python program to remove the nth index
# character from a nonempty string.

def remove_character(print_string):
    print(f'The string "{print_string}" has {len(print_string)} '
          f'character, witch one do you want to remove ')
    remove_index = int(input('Please enter the index to remove: '))
    return print_string[:remove_index] + print_string[remove_index + 1:]


print(remove_character('google'))
