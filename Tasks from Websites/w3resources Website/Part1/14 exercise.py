# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

import datetime

date1 = datetime.date(year=2014, month=7, day=2)
date2 = datetime.date(year=2014, month=7, day=11)

print(date2 - date1)

# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)