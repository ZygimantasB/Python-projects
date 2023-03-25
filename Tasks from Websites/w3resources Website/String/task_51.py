# 51. Write a Python program to find the first non-repeating character in a given string.

def first_not_repeated_character(user_input):
    count_list = []
    count_dict = {}
    for char in user_input:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
            count_list.append(char)
    for word in count_list:
        if count_dict[word] == 1:
            return word

    return count_dict

    # char_count = {char: string.count(char) for char in string}
    # non_repeating_chars = [char for char in string if char_count[char] == 1]
    # return non_repeating_chars[0] if non_repeating_chars else None


print(first_not_repeated_character('abcdefgtagd'))