# 20. Write a Python program to access the index of a list.

def list_show_index(user_input, show_index):
    try:
        return user_input.index(show_index), show_index
    except ValueError:
        return 'Word by index not found'

    # return [f'Value {show_index} found at index -> {user_input.index(show_index} <-' if
    #         user_input.index(show_index) not in user_input else None]


sample_list = ['Hello', 'World', 'Today', 'Morning']


print(list_show_index(sample_list, 'Hello'))
