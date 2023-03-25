# 62. Write a Python program to convert all units of time into seconds.

time_in_minutes = int(input("Please enter the time in minutes for conversion: "))
time_in_hours = int(input("Please enter the time in hours for conversion: "))
time_in_days = int(input("Please enter the time in days for conversion: "))
time_in_week = int(input("Please enter the time in week for conversion: "))
time_in_years = int(input("Please enter the time in years for conversion: "))

time_minutes = time_in_minutes * 60
time_hours = time_in_days * 3600
time_day = time_in_days * 86400
time_week = time_in_week * 604800
time_years = time_in_years * 31536000

print(f"Minutes to seconds: {time_minutes}")
print(f"Hours to seconds: {time_hours}")
print(f"Days to seconds: {time_day}")
print(f"Week to seconds: {time_week}")
print(f"Years to seconds: {time_years}")

print(50 * "-")

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds

print("The  amounts of seconds", time)