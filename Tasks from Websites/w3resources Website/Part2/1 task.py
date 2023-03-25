# 1. Write a Python function that takes a sequence
# of numbers and determines whether all the numbers
# are different from each other.

def sequence_check(checking_numbers):
    if len(checking_numbers) == len(set(checking_numbers)):
        print(f"{sorted(checking_numbers)} my sequence are equal to {sorted(checking_numbers)}")
    elif len(checking_numbers) != len(set(checking_numbers)):
        print(f"{sorted(checking_numbers)} are not equal to {sorted(set(checking_numbers))}")


some_list = [1, 2, 3]
another_list = [9, 8, 7, 6, 6]

some_tuple = (9, 8, 5, 4, 7)
another_tuple = (7, 9, 8, 9, 9, 9)


some_dict = {
    1: "Value1",
    2: "Value2",
    3: "Value3"
}

another_dict = {
    1: "Value1",
    1: "Value6",
    3: "Value3",
    4: "Value4",
    4: "Value5"
}

sequence_check(some_list)
sequence_check(another_list)
sequence_check(some_tuple)
sequence_check(another_tuple)
sequence_check(some_dict)
sequence_check(another_dict)
