# 102. Write a Python program to get system command output.

import subprocess

hostname_check= subprocess.check_output("hostname", shell=True, universal_newlines=True)
print(hostname_check)

# ipconfig_check = subprocess.check_output("ipconfig", shell=True, universal_newlines=True)
# print(list(ipconfig_check))

# netstat = subprocess.check_output("netstat", shell=True, universal_newlines=True)
# print(netstat)

# tracert = subprocess.check_output("tracert google.com", shell=True, universal_newlines=True)
# print(tracert)

# tasklist = subprocess.check_output("tasklist", shell=True, universal_newlines=True)
# print(tasklist)

hostname1 = subprocess.check_output("ping bbc.com", shell=True, universal_newlines=True)
print(hostname1)

print("The end")