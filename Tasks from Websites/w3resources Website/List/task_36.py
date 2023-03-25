# 36. Write a Python program to get a variable
# with an identification number or string.

def define_variable(user_list):
    return [[index, value] for index, value in enumerate(user_list, start=1)]


# sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_list = ['Hello', ' World', ' Morning', 'Singing', 'Fly']

print(define_variable(sample_list))


def id_number_string(user_list):
    return [[id(string_id), string_id] for string_id in user_list]


print(id_number_string(sample_list))
