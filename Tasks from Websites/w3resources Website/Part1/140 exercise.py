# 140. Write a Python program to convert an integer to binary keep leading zeros.
# Sample data : x=12
# Expected output : 00001100
# 0000001100

integer = 12
binary1 = format(integer, "0100b")
print(binary1)
print(bin(integer))
print('{0:b}'.format(integer))