# 70. Write a Python program to sort files by date.

import os
import glob

directory = r"D:\Google Drive All Copy\Python programing learn\w3resources Python\Part1\Part1 w3resource"

os.chdir(directory)
files = filter(os.path.isfile, os.listdir(directory))
files = [os.path.join(directory, f) for f in files]
files.sort(key=lambda x: os.path.getmtime(x))
# files.sort(key=os.path.getmtime)


files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))
