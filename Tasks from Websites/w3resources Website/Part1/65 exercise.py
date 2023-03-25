# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.

seconds_for_convert = int(input("Please enter the second to convert: "))

seconds_days = seconds_for_convert // (60 * 60 * 24)
seconds_for_convert = seconds_for_convert % (60 * 60 * 24)
seconds_hour = seconds_for_convert // (60 * 60)
seconds_for_convert %= 3600
seconds_minutes = seconds_for_convert // 60
seconds_for_convert %= 60
seconds_seconds = seconds_for_convert

print("d:h:m:s-> %d:%d:%d:%d" % (seconds_days, seconds_hour, seconds_minutes, seconds_seconds))

# print(f"Second to second: {seconds_seconds}")
# print(f"Second to minute: {seconds_minutes}")
# print(f"Second to hour: {seconds_hour}")
# print(f"Second to day: {seconds_days}")

print("Other solution ----")

time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
