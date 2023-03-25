# Exercise 9: Find the largest item from a given list


def largest_item(args):
    max_value = args[0]
    for check_list in args:
        if check_list > max_value:
            max_value = check_list
    return max_value


print(largest_item([4, 6, 8, 24, 12, 2]))
