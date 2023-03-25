# Exercise 8: Print list in reverse order using a loop
# Given:
#
list1 = [10, 20, 30, 40, 50]

empty_list = []
for i in range(len(list1)):
    empty_list.append(list1[::-1])
    print(i)
print(empty_list[4])


# list1 = [10, 20, 30, 40, 50]
# # reverse list
# new_list = reversed(list1)
# # iterate reversed list
# for item in new_list:
#     print(item)
