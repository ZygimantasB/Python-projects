# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
# Given:
str1 = "Emma is a data scientist who knows Python. Emma works at google."

print(str1.index('Emma'))
last_index = str1.rfind('Emma')
print(last_index)

# print(len(str1.split(' ')))
