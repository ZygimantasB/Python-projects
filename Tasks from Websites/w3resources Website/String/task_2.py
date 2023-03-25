# 2. Write a Python program to count the number of characters
# (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1

count_char_in_string = 'google.com'


def count_characters(enter_string):
    char_dict = {}
    for char in enter_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


print(count_characters(count_char_in_string))

result = {char: count_char_in_string.count(char) for char
          in count_char_in_string}
print(result)
