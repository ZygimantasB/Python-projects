# 38. Write a Python program to change the
# position of every n-th value to the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

def change_position(user_list, list_index):
    for i in range(len(user_list)-1):
        if (i+1) % list_index == 0:
            user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
    return user_list


sample_list = [0, 1, 2, 3, 4, 5]

print(change_position(sample_list, 1))
