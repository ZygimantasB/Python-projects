# 41. Write a Python program to strip a set of characters from a string.

def strip_character(user_input, strip_chars):
    # return ''.join(char for char in user_input if char not in strip_chars)
    result = ''
    for char in user_input:
        if char not in strip_chars:
            result += char
        else:
            continue
    return result


user_sentence = 'pop os shortcut minimizes all open windows and shows the desktop.'
strip_char = 'abcdefghp'
print(strip_character(user_sentence, strip_char))

