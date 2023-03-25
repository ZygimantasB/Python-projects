# 64. Write a Python program to get file creation and modification date/times.

import os
import pathlib
import datetime

file_name = r"D:\Google Drive All Copy\Python programing learn\w3resources Python\Part1\Part1 w3resource\main.txt"

print('File modification time')
print(datetime.datetime.fromtimestamp(os.path.getatime(file_name)))
print("Get file creation time")
print(datetime.datetime.fromtimestamp(os.path.getctime(file_name)))
print("Get file modification date")
print(datetime.datetime.fromtimestamp(pathlib.Path(file_name).stat().st_mtime))
print("Get file creation time")
print(datetime.datetime.fromtimestamp(pathlib.Path(file_name).stat().st_ctime))

print(os.stat(file_name))

print("Not my solution")

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime(file_name)))
print("Created: %s" % time.ctime(os.path.getctime(file_name)))
