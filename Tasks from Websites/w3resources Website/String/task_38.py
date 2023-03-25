# 38. Write a Python program to count occurrences of a substring in a string.


def count_string_occurrences(input_string):
    words = input_string.split()
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    return count_dict


check_string = "Raindrops on roses and whiskers on kittens, bright copper kettles and warm woolen mittens."

print(count_string_occurrences(check_string))

str1 = 'The quick brown fox jumps over the lazy dog.'
print()
print(str1.count("fox"))
print()
