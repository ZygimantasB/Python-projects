# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers
# from an input string.

str1 = "Emma25 is Data scientist50 and AI Expert"

temp = str1.split()

result_list = []

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        result_list.append(item)
print(result_list)

for item in result_list:
    print(item)
    