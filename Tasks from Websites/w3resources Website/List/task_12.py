# 12. Write a Python program to print a specified list after
# removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def remove_from_list(list1):
    # list1.pop(5)
    # list1.pop(4)
    # list1.pop(0)
    # return list1
    index_to_remove = [0, 4, 5]
    return [element for index, element in enumerate(list1) if index not in index_to_remove]


sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print(remove_from_list(sample_list))

