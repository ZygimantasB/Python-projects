# 19. Write a Python program to calculate the difference between the two lists.

def difference_two_list(list_1, list_2):
    first_list = list(set(list_1) - set(list_2))
    second_list = list(set(list_2) - set(list_1))
    return second_list + first_list


sample_1 = [1, 2, 3, 4, 5, 6]
sample_2 = [4, 5, 6, 7, 8, 1, 2]

print(difference_two_list(sample_1, sample_2))
