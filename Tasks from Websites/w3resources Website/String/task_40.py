# 40. Write a Python program to reverse words in a string.

def reverse_string_words(user_input):
    split_user_input = user_input.split()[::-1]
    result = ' '.join(split_user_input)
    return result


user_sentence = 'pop os shortcut minimizes all open windows and shows the desktop.'
print(reverse_string_words(user_input=user_sentence))
