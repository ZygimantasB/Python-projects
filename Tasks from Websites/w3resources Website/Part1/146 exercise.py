# 146. Write a Python program to find the location of Python module sources.

import datetime
import os
import socket

print("Datetime " + datetime.__file__)
print("Module os " + os.__file__)
print("Socket " + socket.__file__)

import importlib

import os
print("\nList of directories in os module:")
print(os.path)
print("\nList of directories in sys module:")
import sys
print(sys.path)
