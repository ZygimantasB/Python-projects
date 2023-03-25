# 47. Write a Python program to find out the number of CPUs using.

import os
import platform
import subprocess
import psutil
import multiprocessing

print("Print CPU using:", psutil.cpu_percent(4))


print(multiprocessing.cpu_count())