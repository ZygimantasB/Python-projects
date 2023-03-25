# 98. Write a Python program to get the system time.

# Note : The system time is important for debugging, network information,
# random number seeds, or something as simple as program performance.

import datetime
import time

system_time = datetime.datetime.now()

print(system_time)

system_time1 = time.ctime()
print(system_time1)