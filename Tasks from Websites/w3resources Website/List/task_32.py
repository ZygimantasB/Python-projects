# 32. Write a Python program to check whether a list contains a sublist.

def contains_sublist(user_input, sublist):
    sublist_len = len(sublist)
    for number in range(len(user_input) - sublist_len + 1):
        if user_input[number:number+sublist_len] == sublist:
            return True

    return False


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublist1 = [1, 2, 3]
sublist2 = [1, 5, 3]
sublist3 = [6, 5, 3]

print(contains_sublist(sample_list, sublist1))
print(contains_sublist(sample_list, sublist2))
print(contains_sublist(sample_list, sublist3))

