# Exercise 2: Convert string into a datetime object
# For example, You received the following date in string format. Please convert it into Python’s DateTime object.
# Refer: Python String to DateTime
# Given:
# date_string = "Feb 25 2020 4:20PM"
# Expected output:
# 2020-02-25 16:20:00

from datetime import datetime

date_string = "Feb 25 2020 4:20PM"

print(datetime.strptime(date_string, '%b %d %Y %I:%M%p'))
