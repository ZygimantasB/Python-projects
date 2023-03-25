# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first,
# middle, and last characters.

def sum_char(string1, string2):
    first_string1 = string1[0]
    first_string2 = string2[0]
    middle_len1 = len(string1)
    add_middle1 = int(middle_len1 / 2)
    middle_len2 = len(string2)
    add_middle2 = int(middle_len2 / 2)
    last_string1 = string1[-1]
    last_string2 = string2[-1]
    print(first_string1 + first_string2 + string1[add_middle1] + string2[add_middle2] + last_string1 + last_string2)



s1 = "America"
s2 = "Japan"

sum_char(s1, s2)
