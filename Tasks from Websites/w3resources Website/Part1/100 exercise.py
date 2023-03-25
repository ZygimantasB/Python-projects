# 100. Write a Python program to get the name of the host on which the routine is running.

import os
import socket
import platform

os.system("hostname")
# os.system("name")
# os.system("winver")

host_name = socket.gethostname()
print(host_name)

host_name1 = platform.uname()[1]
print("Host name:", host_name1 )


