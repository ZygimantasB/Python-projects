# Exercise 3: Subtract a week (7 days)  from a given date in Python
# Refer: TimeDelta in Python
# Given:
# given_date = datetime(2020, 2, 25)
# Expected output:
# 2020-02-18
from datetime import timedelta, datetime

given_date = datetime(2020, 2, 25)

datetime_result = given_date - timedelta(days=7)
print(datetime_result)


