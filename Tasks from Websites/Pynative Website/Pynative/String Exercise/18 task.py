# Exercise 18: Replace each special symbol with # in the following string
import string

str1 = '/*Jon is @developer & musician!!/*-'

replace_symbol = '#'

# for char in string.punctuation:
#     str1 = str1.replace(char, replace_symbol)
# print(str1)
for char in string.punctuation:
    str1 = str1.replace(char, replace_symbol)
print(str1)