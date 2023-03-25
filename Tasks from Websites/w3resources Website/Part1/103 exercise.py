# 103. Write a Python program to extract the filename from a given path.

import os

file_path = r"D:\Google Drive All Copy\Python programing learn\w3resources Python\Part1\Part1 w3resource\1 exercises.py"
file_path1 = r"D:\Google Drive All Copy\Python programing learn\w3resources Python\Part1\Part1 w3resource\main.txt"

print(os.path.basename(file_path))