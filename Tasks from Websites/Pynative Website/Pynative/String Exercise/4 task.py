# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a p

str1 = 'PyNaTive'

append_lower = []
append_upper = []
for check in str1:
    if check == check.lower():
        new_list = append_lower.append(check)
    elif check == check.upper():
        append_upper.append(check)

combine_list = ''.join(append_lower + append_upper)
print(combine_list)

