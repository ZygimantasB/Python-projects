# 128. Write a Python program to check whether lowercase letters exist in a string.

new_string = "JLKHioutobgjkbhgoIUYOIUHNjokn"
new_string1 = "HFDGSJFSJDLKFHGSDLFJKG"

try_any = any(i.islower() for i in new_string)
print(try_any)

try_any1 = any(x.islower() for x in new_string1)
print(try_any1)