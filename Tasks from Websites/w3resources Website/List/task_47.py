# 47. Write a Python program to insert an element before each element of a list.

def insert_element(my_list, element):
    new_list = [element] * (len(my_list) * 2 - 1)
    new_list[::2] = my_list
    return new_list


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(insert_element(sample_list, 'a'))
