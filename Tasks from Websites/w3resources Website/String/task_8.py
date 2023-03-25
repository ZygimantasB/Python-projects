# 8. Write a Python function that takes a list of
# words and return the longest word and the length
# of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

words = ['run', 'swim', 'cycle', 'jump', 'dance', 'Exercises', 'sing',
         'fly']

dict_with_len_value = {word: len(word) for word in words}

result = dict_with_len_value['jump']
max_value = max(dict_with_len_value.values())
for word, length in dict_with_len_value.items():
    if length == max_value:
        longest_word = word
print(longest_word, max_value)


