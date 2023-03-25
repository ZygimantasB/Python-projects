# 85. Write a Python program to check whether a file path is a file or a directory.

import os

checking = r"D:\Google Drive All Copy\Python programing learn\w3resources Python\Part1\Part1 w3resource"

isfile = os.path.isfile(checking)
# print(isfile)
isdirectory = os.path.isdir(checking)
# print(isdirectory)

if isfile:
    print("This is a file")
elif isdirectory:
    print("This is a directory")
else:
    print("Its something else")