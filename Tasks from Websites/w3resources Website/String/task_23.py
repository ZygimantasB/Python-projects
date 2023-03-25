# 23. Write a Python program to remove a newline in Python.

def remove_newline(user_input):
    print(user_input)
    return user_input.rstrip()


print(remove_newline('Hello world\n'))
