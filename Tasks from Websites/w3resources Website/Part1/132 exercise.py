# 132. Write a Python program to list home directory without absolute path.

import os
from pathlib import Path

home_directory1 = os.path.expanduser("~")
print(home_directory1)

home_directory2 = Path.home()
print(home_directory2)