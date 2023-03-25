# 5. Write a Python program to count the
# number of strings from a given list of strings.
# The string length is 2 or more and the first and last
# characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

def count_strings(user_input):
    return sum([1 for item in user_input if len(item) > 2 and item[0] == item[
        -1]])


sample_list = ['abc', 'xyz', 'aba', '1221']

print(count_strings(sample_list))
