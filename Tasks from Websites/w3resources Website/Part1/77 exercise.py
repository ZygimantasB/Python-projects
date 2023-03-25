# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()
