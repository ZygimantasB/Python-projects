# 120. Write a Python program to format a specified string limiting the length of a string.

very_long_string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

limit_len = f"{very_long_string:3.3}"

print(limit_len)

limit_len1 = very_long_string[:4]
print(limit_len1)


str_num = "1234567890"
print("Original string:",str_num)
print('%.6s' % str_num)
print('%.9s' % str_num)
print('%.10s' % str_num)