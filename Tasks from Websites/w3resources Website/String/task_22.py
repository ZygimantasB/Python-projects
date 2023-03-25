# 22.Write a Python program to sort a string lexicographically.

def sort_string_lexicographically(input_string):
    order_char = sorted([char for char in input_string])
    return ''.join(order_char)


print(sort_string_lexicographically('lexicographically'))
print(sort_string_lexicographically('Write'))
print(sort_string_lexicographically('program'))
