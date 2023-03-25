# 87. Write a Python program to get the size of a file.

import os

size_of_the_file = r"D:\Google Drive All Copy\Python programing learn\
w3resources Python\Part1\Part1 w3resource\main.txt"

size_file = os.path.getsize(size_of_the_file)

print(size_file)

