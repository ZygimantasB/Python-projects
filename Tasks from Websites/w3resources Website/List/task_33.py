# 33. Write a Python program to generate all sublists of a list.

def generate_sublists(user_list):
    sublists = []
    for number1 in range(len(user_list)):
        for number2 in range(number1 + 1, len(user_list) + 1):
            sublists.append(user_list[number1:number2])
    return sublists


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(generate_sublists(sample_list))
