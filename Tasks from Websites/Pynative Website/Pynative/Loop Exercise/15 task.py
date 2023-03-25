# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Given:
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note: list index always starts at 0
#
# Expected output:
#
# 20 40 60 80 100

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# for i in my_list[1::2]:
#     print(i)
#
# new_value = [x for x in my_list[1::2]]
# print(new_value)

my_list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def slice_list(*args: list):
    # some_value = [a for a in args[1::2]]
    some_value = slice(1, len(args), 2)
    print(args[some_value])


some_value = slice(1, len(my_list1), 2)
print(my_list1[some_value])
