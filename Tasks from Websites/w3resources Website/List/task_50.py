# 50. Write a Python program to sort a list of nested dictionaries.

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
# print("Original List: ")
# print(my_list)
# my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
# print("Sorted List: ")
# print(my_list)


def sort_nested_dicts(dicts_list, key):
    return sorted(dicts_list, key=lambda x: x.get(key))


print(sort_nested_dicts(my_list, 'subkey'))
