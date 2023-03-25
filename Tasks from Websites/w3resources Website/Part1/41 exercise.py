# 41. Write a Python program to check whether a file exists.

import os

print(os.path.exists('main.txt'))
print(os.path.exists('1 exercise.py'))

print(50 * 'ž')

my_file = open('main.txt')
try:
    my_file.close()
    print("File found!")
except FileNotFoundError:
    print("File not found!")
