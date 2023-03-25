# 5. Write a Python program to get a single string from two given
# strings, separated by a space and swap the first two characters of
# each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def concat_strings(string1: str, string2: str):
    combined_string = string2[:2] + string1[2:] + ' ' + string1[:2] + \
                      string2[2:]
    return combined_string


print(concat_strings('abc', 'xyz'))
