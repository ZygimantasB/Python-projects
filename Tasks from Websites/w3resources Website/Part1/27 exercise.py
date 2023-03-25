# 27. Write a Python program to concatenate all elements in a list into a string and return it.

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

print(concatenate_list_data([1, 5, 12, 2]))

print(50 * "-")

numbers_list = [1, 2, 4, 6, 7, 8, 98]
numbers = ""

for i in numbers_list:
    numbers += str(i)
print(numbers)

print(50 * "-")

def concatenate_list_numbers(list_numbers):
    answer = ''
    for i in list_numbers:
        answer += str(i)
    return answer

print(concatenate_list_numbers(numbers_list))