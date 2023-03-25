# 45. Write a Python program to call an external command.

import os
import psutil
import platform

# print(os.system('dir'))

print(psutil.cpu_count())

print(os.cpu_count())

print(os.system('nslookup google.com'))
print(os.system('ping google.com'))

import subprocess
return_code = subprocess.call(['ping', 'localhost'])
print("Output of call() : ", return_code)

dt = 'date'
os.system(dt)

print (os.popen("echo Hello FINXTER!").read())