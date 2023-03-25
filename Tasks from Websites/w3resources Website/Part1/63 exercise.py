# 63. Write a Python program to get an absolute file path.

import os

file_name = r"D:\Google Drive All Copy\Python programing learn\w3resources Python\Part1\Part1 w3resource\main.txt"

print(os.path.dirname(file_name))

absolute_path = os.path.abspath("main.txt")
print(absolute_path)

def ne_abolute_path(file_name):
    new_absolute_path = os.path.abspath(file_name)
    return new_absolute_path

print(50 * "-")

from pathlib import Path
p = Path("main.txt").resolve()
print(p)