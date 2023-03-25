# 44. Write a Python program to locate Python site-packages.

import os
import sys
import sysconfig
import platform
import site

print("Python site-packages:", site.getsitepackages())



