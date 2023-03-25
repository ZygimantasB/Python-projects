# 136. Write a Python program to find files and skip directories of a given directory.

file_path = r"D:\Google Drive All Copy\Python programing learn\w3resources Python\Part1\Part1 w3resource"

import os
print([f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))])

print("\n--Another solution-- \n")

user_path = 'c:/'
for fname in os.listdir(user_path):
    path = os.path.join(user_path, fname)
    if os.path.isdir(path):
        # skip directories
        continue
    # print the file names
    print(fname)
