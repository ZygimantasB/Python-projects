# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"

print(str_x.count("Emma"))

print("\n--Another Solution--\n")

count_word = input("Please enter the word witch want to count in sentence: ")
zero_value = 0

for i in range(0, len(count_word) -1):
    zero_value += count_word[i: i + 4] == 'Emma'

