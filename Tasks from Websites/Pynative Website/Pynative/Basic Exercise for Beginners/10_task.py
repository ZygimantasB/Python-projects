# Exercise 10: Create a new list from a two list using the following condition

# Create a new list from a two list using the following condition
# Given a two list of numbers, write a program to create a new list such that the new
# list should contain odd numbers from the first list and even numbers from the second lis

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result_list = []


for combined_list in list1:
    if combined_list % 2 != 0:
        result_list.append(combined_list)

for combined_list in list2:
    if combined_list % 2 == 0:
        result_list.append(combined_list)

print(result_list)