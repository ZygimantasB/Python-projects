# Exercise 6: Add a week (7 days) and 12 hours to a given date
# Given:
# # 2020-03-22 10:00:00
#
# Expected output:
# 2020-03-29 22:00:00

from datetime import timedelta, datetime

given_date = datetime(2020, 3, 22, 10, 0, 0)

result = given_date + timedelta(days=7, hours=12)
print(result)
