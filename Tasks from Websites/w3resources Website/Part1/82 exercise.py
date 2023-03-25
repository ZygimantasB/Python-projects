# 82. Write a Python program to calculate the sum
# of all items of a container (tuple, list, set, dictionary).

# tuple

tuple_int = (7, 8, 11, 14)

# list

list_int = [9, 45, 89, 78, 96]

# set

set_int = {78, 96, 45, 78, 125, 789}

# dictionary

dictionary_int = {
    "value1": 1,
    "value2:": 78,
    "value3": 97,
    "value4": 98,
    "value5": 145
}

print("Tuple sum")
print(sum(tuple_int))
print("list sum")
print(sum(list_int))
print("set sum")
print(sum(set_int))
print("dictionary sum")
print(sum(dictionary_int.values()))

nums = [10,20,30]
print("Original container:")
print(nums)
print(type(nums))
print("Sum of all items of the said container:", sum(nums))
