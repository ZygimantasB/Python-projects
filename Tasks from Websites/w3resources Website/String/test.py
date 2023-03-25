words_len_dict = {'run': 3, 'swim': 4, 'cycle': 5, 'jump': 4, 'dance': 5, 'longest word': 11, 'sing': 4, 'fly': 3}
max_value = max(words_len_dict.values())
for word, length in words_len_dict.items():
    if length == max_value:
        longest_word1 = word
print(longest_word1)