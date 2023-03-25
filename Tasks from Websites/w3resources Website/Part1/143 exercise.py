# 143. Write a Python program to determine if
# the python shell is executing in 32bit or 64bit mode on operating system.

import platform

python_bit = platform.architecture()

print(python_bit[0])

import struct
print(struct.calcsize("P") * 8)