# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

s1 = "Ault"
s2 = "Kelly"

# first_two_char = s1[0:2]
# last_two_char = s1[2:4]
# full_word = first_two_char + s2 + last_two_char
# print(full_word)

s1_len = len(s1)
middle_char = int(s1_len / 2)
first_two = s1[:middle_char:]
last_two = s1[middle_char:]
result = first_two + s2 + last_two
print(result)


