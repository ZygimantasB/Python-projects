# 3. Write a Python program to get the largest number from a list.

def largest_number(numbers):
    # return max(numbers)
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


sample_list = [1, 9, 12, 85, 65, 32]

print(largest_number(sample_list))
