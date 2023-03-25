# 24. Write a Python program to append a list to the second list.

def append_two_lists(list1, list2):
    # return list1 + list2
    # list1.extend(list2)
    # return list1
    # return [number1 for number2 in [list1, list1] for number1 in number2]
    return [*list1, *list2]


sample_list1 = [1, 2, 3, 4, 5]
sample_list2 = [6, 7, 8, 9, 0]


print(append_two_lists(sample_list1, sample_list2))
