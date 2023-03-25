# 4. Write a Python program to get a string from a given string
# where all occurrences of its first char have been changed to '$',
# except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'

word = 'restart'
part_word = word[1:]
changed_word = word.replace('r', '$')
print('r' + changed_word)
