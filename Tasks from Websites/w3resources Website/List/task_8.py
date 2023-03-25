# 8. Write a Python program to check if a list is empty or not.

def check_list_empty(user_input):
    # return ['Empty list' if len(user_input) == 0 else 'The list not empty']
    return ['Empty list' if not user_input else 'The list not empty']


empty_list = []
list_not_empty = [8]

print(check_list_empty(empty_list))
print(check_list_empty(list_not_empty))
