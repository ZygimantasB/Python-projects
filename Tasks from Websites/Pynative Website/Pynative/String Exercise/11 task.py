# Exercise 11: Reverse a given string
# Given:

str1 = "PYnative"

print(str1[::-1])

reversed_in_list = list(reversed(str1))
print(reversed_in_list)

reversed_in_join = ''.join(reversed(str1))
print(reversed_in_join)

reversed_string = reversed(str1)
for i in reversed_string:
    print(i, end='')
print('\n')

