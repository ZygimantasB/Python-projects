# 35. Write a Python program to create a list by concatenating
# a given list with a range from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

def concat_list(user_list):
    # result = []
    # for number in range(1, 6):
    #     for item in user_list:
    #         result.append(f'{item}{number}')
    # return result
    return [f'{item}{number}' for number in range(1, 6) for item in user_list]


sample_list = ['p', 'q']

print(concat_list(sample_list))
