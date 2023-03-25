# 26. Write a Python program to check whether two lists are circularly identical.


def is_circularly_identical(list1, list2):
    circular_list = list1 + list1
    return all(item in circular_list[i:i+len(list2)] for i, item in enumerate(list2))


list1 = [1, 2, 3, 4, 5]
list2 = [5, 1, 2, 3, 4]

if is_circularly_identical(list1, list2):
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")
