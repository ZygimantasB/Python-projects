# 114. Write a Python program to filter the positive numbers from a list.


new_list = [-9, 8, -7, -6, 5, 3, -5]

for i in new_list:
    if i > 0:
        print(i, end=" ")

print("\n")

filter_negative = list(filter(lambda x: x > 0, new_list))
print(sorted(filter_negative))

remove_negative = [x for x in new_list if x > 0] #  [ ] it means list
print(remove_negative)