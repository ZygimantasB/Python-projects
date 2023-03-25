# 145. Write a Python program to test if a variable is a list or tuple or a set.

new_tuple = (1, 2, 3, 4, 5, 6) # Tuple
new_list = [1, 2, 3, 4, 5, 6] # List
new_set = {1, 2, 3, 4, 5, 6} # Set

if isinstance(new_list, list):
    print("This is a list")
elif isinstance(new_list, tuple):
    print('This is a tuple')
elif isinstance(new_list, set):
    print("This is a set")

print("\n --Another solution-- \n")

#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
x = ('tuple', False, 3.2, 1)
if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')
else:
    print('Neither a list or a set or a tuple.')
