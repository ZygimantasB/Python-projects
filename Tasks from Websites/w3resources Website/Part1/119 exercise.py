# 119. Write a Python program to round a floating-point number to specified number decimal places.

number = 7.89654321

round_number = round(number, 3)

print(round_number)

new_float = "{:.2f}".format(number)

print(new_float)