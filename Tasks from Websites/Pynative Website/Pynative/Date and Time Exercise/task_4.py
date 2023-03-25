# Exercise 4: Print a date in a the following format
# Day_name  Day_number  Month_name  Year
# Refer: Python DateTime Format Using Strftime()
# Given:
# given_date = datetime(2020, 2, 25)
# Expected output:
# Tuesday 25 February 2020

from datetime import datetime

given_date = datetime(2020, 2, 25)

print(datetime.strftime(given_date, '%a %d %B %y'))

