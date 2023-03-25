# 22. Write a Python program to count the number 4 in a given list.

def number_counter(numbers):
    counter = 0
    for nums in numbers:
        if nums == 4:
            counter += 1

    return counter


num_list = [1, 2, 3, 4, 5, 6, 4, 5, 7, 4]

count = 0

for num in num_list:
    if num == 4:
        count += 1
print(count)

print(50 * "-")

information_check = number_counter(num_list)
print(information_check)


