# 22. Write a Python program to find the index of an item in a specified list.

def find_index_item(user_input, string_index):
    return user_input.index(string_index)


sample_list = ['Hello', 'World', 'Today', 'Morning']


print(find_index_item(sample_list, 'World'))


