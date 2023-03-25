# 3. Write a Python program to remove and print every third
# number from a list of numbers until the list becomes empty.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

list_len = len(number_list)
number_list_len = number_list[0:list_len:2]

number_list_len.append(number_list)

print(number_list_len)