# 47. Write a Python program to lowercase the first n characters in a string.

def lower_n_character(char_to_lower, char_index):
    if len(char_to_lower) < char_index:
        return char_to_lower.lower()
    return char_to_lower[:char_index].lower() + char_to_lower[char_index:]


print(lower_n_character('GOOGLE', 5))
