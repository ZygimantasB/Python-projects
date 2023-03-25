# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

year_choose = int(input("Please enter the year: "))
month_choose = int(input("Please enter the month: "))

my_calendor = calendar.month(year_choose, month_choose)

print(my_calendor)

# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))