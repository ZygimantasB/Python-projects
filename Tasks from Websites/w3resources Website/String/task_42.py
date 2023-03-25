# 42. Write a Python program to count repeated characters
# in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output

def count_repeated_characters(user_input):
    count_dict = {}
    for char in user_input:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    repeated_characters_only = {key: value for key, value in
                                count_dict.items() if value >= 2}
    return repeated_characters_only


sample_string = 'thequickbrownfoxjumpsoverthelazydog'
print(count_repeated_characters(sample_string))
