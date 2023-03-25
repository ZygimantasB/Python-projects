# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
#
# Given:
#
# str1 = "James"

str1 = 'James'
first_symbol = str1[0]
word_len = len(str1)
middle_symbol = int(word_len / 2)
last_symbol = str1[-1]
first_middle_last = first_symbol + str1[middle_symbol] + last_symbol
print(first_middle_last)
