# 148. Write a Python function to find the maximum and minimum numbers
# from a sequence of numbers.
# Note: Do not use built-in functions.

new_list = [4, 5, 6, 7, 8, 9]
new_number = new_list[0]
new_new_number = new_list[0]

count_number = len(new_list)

for i in new_list:
    if i > new_number:
        new_number = i
print(f"Max value are {new_number}")

for x in new_list:
    if x < new_new_number:
        new_new_number = x
print(f"The minimum value are {new_new_number}")
