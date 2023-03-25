# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

def generate_array():
    return [[['*' for number in range(6)] for number in range(4)] for number in range(3)]


print(generate_array())
