# 6. Write a Python program to get a list, sorted in
# increasing order by the last element in each tuple
# from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def sort_list(user_input):
    return sorted(user_input, key=lambda x: x[-1])


sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

print(sort_list(sample_list))
