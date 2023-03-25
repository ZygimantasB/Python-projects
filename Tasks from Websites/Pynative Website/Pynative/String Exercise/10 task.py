# Exercise 10: Write a program to count occurrences of all characters within a string

str1 = "Apple"

char_dict = dict()

for i in str1:
    count_char = str1.count(i)
    char_dict[i] = count_char

print('Result=', char_dict)
