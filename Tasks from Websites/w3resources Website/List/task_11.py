# 11. Write a Python function that takes two lists and returns True if
# they have at least one common member.

def compare_list(list1, list2):
    return [True if number in list2 else False for number in list1]


sample_list1 = [1, 2, 3, 4, 5]
sample_list2 = [1, 6, 7, 8, 9]
sample_list3 = [10, 11, 12, 23]


print(compare_list(sample_list1, sample_list2))
print(compare_list(sample_list1, sample_list3))
