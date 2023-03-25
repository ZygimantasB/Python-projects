# Exercise 1B: Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.

def print_middle_symbols(string):
    string_len = len(string)
    middle_char = int(string_len / 2)
    fist_char = string[middle_char - 1]
    last_char = string[middle_char + 1]
    print(fist_char + string[middle_char] + last_char)


str1 = "JhonDipPeta"
str2 = "JaSonAy"

print_middle_symbols(str1)
print_middle_symbols(str2)


