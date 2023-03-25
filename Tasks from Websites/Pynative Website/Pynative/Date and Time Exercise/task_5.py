# Exercise 5: Find the day of the week of a given date
# Given:
# given_date = datetime(2020, 7, 26)
# Expected output:
# Sunday

from datetime import datetime

given_date = datetime(2020, 7, 26)

print(datetime.strftime(given_date, '%A'))

